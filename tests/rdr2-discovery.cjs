'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {spawnSync} = require('node:child_process');
const script = path.resolve(__dirname, '../scripts/rdr2/detect.cjs');
const {discover} = require(script);

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'reyrun-detection-'));
function write(file, content) {
  fs.mkdirSync(path.dirname(file), {recursive: true});
  fs.writeFileSync(file, content);
}
function recordPath(directory) { return directory.replace(/\\/g, '\\\\'); }
const steam = path.join(tmp, 'Steam');
const library = path.join(tmp, 'Other volume', 'Spēļu bibliotēka');
const game = path.join(library, 'steamapps', 'common', 'Actual folder name');
const catalogue = path.join(steam, 'steamapps', 'libraryfolders.vdf');
const app = path.join(library, 'steamapps', 'appmanifest_1174180.acf');
const items = path.join(tmp, 'Epic', 'Manifests');
const secondGame = path.join(tmp, 'Alternative install');
const source = {steam:[steam],rockstar:[],epicManifests:[]};
const manifest = id => '"AppState" { "appid" "' + id + '" "installdir" "Actual folder name" }';
function cli(records) {
  const index = path.join(tmp, 'sample.json');
  write(index, JSON.stringify(records));
  const run = spawnSync(process.execPath, [script,index], {encoding:'utf8'});
  assert.equal(run.status,0);
  return Buffer.from(run.stdout,'base64').toString('utf8');
}
try {
  write(catalogue, '"libraryfolders" { "0" { "path" "' + recordPath(steam) +
    '" } "1" { "path" "' + recordPath(library) + '" "apps" { "1174180" "700" } } }');
  write(app,manifest('1174180'));
  write(path.join(game,'RDR2.exe'),'fixture');
  assert.deepEqual(discover(source),[fs.realpathSync.native(game)]);
  assert.equal(cli(source),fs.realpathSync.native(game));
  write(catalogue,'"LibraryFolders" { "TimeNextStatsReport" "77" "1" "' + recordPath(library) + '" }');
  assert.deepEqual(discover(source),[fs.realpathSync.native(game)]);
  write(app,manifest('123'));assert.deepEqual(discover(source),[]);
  write(app,manifest('1174180'));
  write(path.join(items,'match.item'),JSON.stringify({DisplayName:'Red Dead Redemption 2',InstallLocation:game}));
  write(path.join(items,'other.item'),JSON.stringify({DisplayName:'Other game',InstallLocation:secondGame}));
  write(path.join(items,'invalid.item'),'incomplete fixture');
  const both={...source,rockstar:[game,path.join(tmp,'removed')],epicManifests:[items]};
  assert.deepEqual(discover(both),[fs.realpathSync.native(game)]);
  assert.deepEqual(discover({epicManifests:[items]}),[fs.realpathSync.native(game)]);
  assert.deepEqual(discover({rockstar:[game]}),[fs.realpathSync.native(game)]);
  write(path.join(secondGame,'RDR2.exe'),'second fixture');
  assert.equal(cli({...both,rockstar:[secondGame]}),'');
  assert.equal(cli({rockstar:[path.join(tmp,'removed')]}),'');
  fs.unlinkSync(path.join(game,'RDR2.exe'));assert.deepEqual(discover(both),[]);
  process.stdout.write('RDR2 discovery passed: modern and legacy Steam libraries, custom install name, Unicode, app identity, Rockstar, Epic, duplicate, stale and ambiguous records.\n');
} finally { fs.rmSync(tmp,{recursive:true,force:true}); }
