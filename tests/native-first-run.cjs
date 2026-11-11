'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {spawn, spawnSync} = require('node:child_process');
const readline = require('node:readline');
const {once} = require('node:events');
const {inflateSync} = require('node:zlib');

const platform = process.platform;
const bootstrap = process.argv.includes('--bootstrap');
const project = path.resolve(__dirname, '..');
const temporary = fs.mkdtempSync(path.join(os.tmpdir(), 'reyrun-first-run-'));
const user = path.join(temporary, 'Fixture user');
const workspace = path.join(user, 'REYRUN Bridge');
const localApp = path.join(user, 'AppData', 'Local');
const roaming = path.join(user, 'AppData', 'Roaming');
const client = path.join(user, 'Fake Claude Desktop');
const configPath = path.join(client, 'claude_desktop_config.json');
const original = {
  preferences: {displayLanguage: 'lv'},
  mcpServers: {'unrelated-fixture': {command: 'sentinel-only', args: ['keep me']}}
};
const environment = {
  ...process.env,
  HOME: user,
  USERPROFILE: user,
  LOCALAPPDATA: localApp,
  APPDATA: roaming,
  REYRUN_WORKSPACE: workspace,
  REYRUN_TEST_CLIENT: client,
  REYRUN_TEST_MODE: '1'
};
if (bootstrap) {
  assert.ok(platform === 'win32' || platform === 'darwin', 'Portable runtimes target Windows/macOS only');
  for (const key of Object.keys(environment)) {
    if (key.toLowerCase() === 'path') delete environment[key];
  }
  const windows = process.env.SystemRoot || 'C:\\Windows';
  environment.PATH = platform === 'win32'
    ? [windows, path.join(windows, 'System32'), path.join(windows, 'System32', 'WindowsPowerShell', 'v1.0')].join(path.delimiter)
    : '/usr/bin:/bin:/usr/sbin:/sbin';
}
for (const directory of [user, localApp, roaming, client]) {
  fs.mkdirSync(directory, {recursive: true});
}
const initialText = JSON.stringify(original, null, 2) + '\n';
fs.writeFileSync(configPath, initialText);

function readConfig() {
  return JSON.parse(fs.readFileSync(configPath, 'utf8').replace(/^\uFEFF/, ''));
}

function launch(wrapper) {
  assert.ok(fs.statSync(wrapper).isFile(), 'published launcher is missing');
  const args = platform === 'win32'
    ? ['/d', '/s', '/c', 'call "%REYRUN_CI_LAUNCHER%"']
    : [wrapper];
  const result = spawnSync(platform === 'win32' ? 'cmd.exe' : '/bin/bash', args, {
    cwd: temporary,
    env: {...environment, REYRUN_CI_LAUNCHER: wrapper},
    encoding: 'utf8',
    input: '\n',
    windowsVerbatimArguments: platform === 'win32',
    windowsHide: true,
    timeout: 240000
  });
  assert.ifError(result.error);
  assert.equal(result.status, 0, 'launcher failed: ' + (result.stderr || result.stdout));
}

// Start exactly the command saved by the launcher in the user's fake MCP config.
// Nothing in the runner's own desktop client, repository or personal profile is attached.
async function connect(entry) {
  assert.ok(path.isAbsolute(entry.command), 'installer must pin the node executable');
  const proc = spawn(entry.command, entry.args, {
    env: {...environment, ...entry.env},
    stdio: ['pipe', 'pipe', 'pipe'],
    windowsHide: true
  });
  let errorLog = '';
  proc.stderr.on('data', data => { errorLog = (errorLog + data.toString()).slice(-2000); });
  const lines = readline.createInterface({input: proc.stdout});
  const waiting = new Map();
  let nextId = 0;

  function rejectAll(reason) {
    for (const request of waiting.values()) {
      clearTimeout(request.timer);
      request.reject(reason);
    }
    waiting.clear();
  }

  proc.once('error', rejectAll);
  proc.once('exit', (code, signal) => rejectAll(new Error('Bridge stopped: ' + (signal || code) + ' ' + errorLog)));
  lines.on('line', line => {
    let message;
    try { message = JSON.parse(line); }
    catch { rejectAll(new Error('Unexpected non-JSON line on the MCP stdout stream')); return; }
    const pending = waiting.get(message.id);
    if (!pending) return;
    waiting.delete(message.id);
    clearTimeout(pending.timer);
    if (message.error) pending.reject(new Error(JSON.stringify(message.error)));
    else pending.resolve(message.result);
  });

  function send(message) {
    proc.stdin.write(JSON.stringify({jsonrpc: '2.0', ...message}) + '\n');
  }

  function rpc(method, params) {
    const id = ++nextId;
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        waiting.delete(id);
        reject(new Error('MCP request timed out: ' + method + ' ' + errorLog));
      }, 20000);
      waiting.set(id, {resolve, reject, timer});
      send({id, method, params});
    });
  }

  async function close() {
    if (proc.exitCode !== null || proc.signalCode) return;
    const stopped = once(proc, 'exit');
    proc.stdin.end();
    const timer = setTimeout(() => proc.kill(), 3000);
    try { await stopped; }
    finally { clearTimeout(timer); lines.close(); }
  }

  try {
    const handshake = await rpc('initialize', {
      protocolVersion: '2025-11-25',
      clientInfo: {name: 'reyrun-native-check', version: '1.0'},
      capabilities: {}
    });
    assert.equal(handshake.protocolVersion, '2025-11-25');
    send({method: 'notifications/initialized'});
  } catch (err) {
    await close();
    throw err;
  }
  return {rpc, close};
}

async function call(clientSession, name, args = {}) {
  const response = await clientSession.rpc('tools/call', {name, arguments: args});
  assert.ok(!response.isError, JSON.stringify(response.content));
  return JSON.parse(response.content[0].text);
}

async function exercise(wrapper) {
  launch(wrapper);
  const first = readConfig();
  assert.deepEqual(first.preferences, original.preferences);
  assert.deepEqual(first.mcpServers['unrelated-fixture'], original.mcpServers['unrelated-fixture']);
  const entry = first.mcpServers['reyrun-jobs'];
  assert.ok(entry, 'first run did not add the jobs profile');
  if (bootstrap) {
    const runtime = fs.realpathSync(path.join(workspace, 'runtime'));
    const binary = fs.realpathSync(entry.command);
    assert.ok(binary.startsWith(runtime + path.sep), 'clean install must use the private runtime');
    const version = spawnSync(binary, ['--version'], {encoding: 'utf8'});
    assert.ifError(version.error);
    assert.equal(version.status, 0);
    assert.match(version.stdout.trim(), /^v24\./);
  }
  const backups = () => fs.readdirSync(client).filter(f => f.includes('.reyrun-backup-'));
  assert.equal(backups().length, 1);
  assert.equal(fs.readFileSync(path.join(client, backups()[0]), 'utf8'), initialText);

  const firstSession = await connect(entry);
  try {
    const {tools} = await firstSession.rpc('tools/list', {});
    assert.deepEqual(tools.map(t => t.name).sort(), ['bridge_status','list_jobs','read_checkpoint','save_checkpoint']);
    const status = await call(firstSession, 'bridge_status');
    assert.equal(status.platform, platform);
    const before = await call(firstSession, 'read_checkpoint', {job:'native-ci'});
    assert.equal(before.revision, 0);
    const saved = await call(firstSession, 'save_checkpoint', {
      job:'native-ci', revision:0, done:'Pārbaudīts — проверено', next:'Resume in a fresh process'
    });
    assert.equal(saved.revision, 1);
  } finally { await firstSession.close(); }

  launch(wrapper);
  assert.deepEqual(readConfig(), first, 'repeated launcher must preserve existing config');
  assert.equal(backups().length, 1, 'repeated unchanged install should not create another backup');
  const nextSession = await connect(readConfig().mcpServers['reyrun-jobs']);
  try {
    const current = await call(nextSession, 'read_checkpoint', {job:'native-ci'});
    assert.equal(current.revision, 1);
    assert.equal(current.done, 'Pārbaudīts — проверено');
    assert.equal(current.next, 'Resume in a fresh process');
    const stale = await nextSession.rpc('tools/call', {name:'save_checkpoint',arguments:{
      job:'native-ci',revision:0,done:'stale attempt',next:'must not overwrite'
    }});
    assert.equal(stale.isError, true);
    assert.deepEqual(await call(nextSession, 'read_checkpoint', {job:'native-ci'}), current);
  } finally { await nextSession.close(); }
  console.log('PASS: native launcher, preserved config and original backup, idempotent rerun, Unicode checkpoint after process restart, stale update refused.');
}


function wrapperFor(mode) {
  const suffix = platform === 'win32' ? 'Windows.cmd' : 'macOS.command';
  return path.join(project, 'launchers', 'REYRUN-' + mode + '-' + suffix);
}

function verifyRenderedPng(result) {
  assert.ok(!result.isError, JSON.stringify(result.content).slice(0,1200));
  const image = result.content.find(item => item.type === 'image' && item.mimeType === 'image/png');
  assert.ok(image?.data, 'MCP client must receive PNG pixels');
  const png = Buffer.from(image.data, 'base64');
  assert.equal(png.subarray(0,8).toString('hex'), '89504e470d0a1a0a');
  assert.equal(png.readUInt32BE(8), 13);
  assert.equal(png.toString('ascii',12,16), 'IHDR');
  const width = png.readUInt32BE(16), height = png.readUInt32BE(20);
  assert.ok(width >= 64 && height >= 64, 'expected a browser viewport');
  assert.equal(png.subarray(-12).toString('hex'), '0000000049454e44ae426082');
  const data = [];
  for (let offset = 8; offset < png.length;) {
    const length = png.readUInt32BE(offset);
    assert.ok(offset + length + 12 <= png.length, 'truncated PNG chunk');
    if (png.toString('ascii', offset + 4, offset + 8) === 'IDAT') {
      data.push(png.subarray(offset + 8, offset + 8 + length));
    }
    offset += 12 + length;
  }
  const pixels = inflateSync(Buffer.concat(data), {maxOutputLength:128*1024*1024});
  assert.ok(pixels.length >= height * (1 + Math.ceil(width / 8)), 'incomplete image scanlines');
}

async function optionalProfiles() {
  for (const mode of ['filesystem','playwright','devtools']) {
    launch(wrapperFor(mode));
    const config = readConfig();
    assert.deepEqual(config.mcpServers['unrelated-fixture'], original.mcpServers['unrelated-fixture']);
    const session = await connect(config.mcpServers['reyrun-' + mode]);
    try {
      const names = (await session.rpc('tools/list', {})).tools.map(t => t.name).sort();
      const invoke = (name, args) => session.rpc('tools/call', {name, arguments: args});
      if (mode === 'filesystem') {
        const scope = path.join(workspace, 'Workspace');
        const note = path.join(scope, 'file with spaces.txt');
        assert.ok(names.includes('list_allowed_directories'));
        const allowed = await invoke('list_allowed_directories', {});
        assert.ok(!allowed.isError);
        assert.ok(allowed.content.some(c => String(c.text).includes(scope)));
        assert.ok(!(await invoke('write_file', {path:note, content:'Vārdi, слова.'})).isError);
        assert.equal(fs.readFileSync(note, 'utf8'), 'Vārdi, слова.');
        const refused = await invoke('get_file_info', {path:configPath});
        assert.equal(refused.isError, true);
      } else {
        const expected = mode === 'playwright'
          ? ['browser_navigate','browser_snapshot','browser_take_screenshot']
          : ['navigate','screenshot'];
        assert.deepEqual(names, expected.toSorted());
        const navigate = mode === 'playwright' ? 'browser_navigate' : 'navigate';
        const refused = await invoke(navigate, {url:'https://example.invalid/'});
        assert.equal(refused.isError, true);
        // The initial blank page exercises the real renderer without sending user data or browsing a live site.
        const capture = mode === 'playwright' ? 'browser_take_screenshot' : 'screenshot';
        const image = await invoke(capture, {});
        verifyRenderedPng(image);
      }
      console.log('PASS: ' + platform + ' native ' + mode + ' fixture');
    } finally { await session.close(); }
  }
}

const run = process.argv.includes('--profiles') ? optionalProfiles() : exercise(wrapperFor('jobs'));
run
  .catch(error => { console.error(error.stack || error); process.exitCode = 1; })
  .finally(() => fs.rmSync(temporary, {recursive: true, force: true, maxRetries: 3, retryDelay: 150}));
