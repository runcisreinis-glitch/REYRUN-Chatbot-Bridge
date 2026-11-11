'use strict';

const fs = require('node:fs');
const path = require('node:path');
const title = 'Red Dead Redemption 2';
const appId = '1174180';

function smallText(file) {
  try {
    const stat = fs.statSync(file);
    return stat.isFile() && stat.size <= 2 * 1024 * 1024 ? fs.readFileSync(file, 'utf8').replace(/^\uFEFF/, '') : '';
  } catch { return ''; }
}

// Steam stores its library and app records as quoted KeyValues with nested blocks.
function vdf(text) {
  const tokens = [...text.matchAll(/"(?:\\.|[^"\\])*"|\/\/[^\r\n]*|[{}]/g)]
    .map(match => match[0]).filter(token => !token.startsWith('//'));
  let cursor = 0;
  function string(token) {
    if (!token || !token.startsWith('"')) throw Error('Malformed KeyValues string');
    return token.slice(1, -1).replace(/\\(["\\])/g, '$1');
  }
  function block(depth) {
    if (depth > 24) throw Error('KeyValues record too deeply nested');
    const result = Object.create(null);
    while (cursor < tokens.length) {
      const key = tokens[cursor++];
      if (key === '}' && depth) return result;
      const name = string(key);
      const value = tokens[cursor++];
      result[name.toLowerCase()] = value === '{' ? block(depth + 1) : string(value);
    }
    if (depth) throw Error('Unclosed KeyValues record');
    return result;
  }
  try { return block(0); } catch { return {}; }
}

function localPath(value) {
  return typeof value === 'string' && path.isAbsolute(value) && !/^[\\/]{2}/.test(value);
}

function discover(records) {
  const found = new Map();
  function verify(folder) {
    if (!localPath(folder)) return;
    try {
      if (!fs.statSync(path.join(folder, 'RDR2.exe')).isFile()) return;
      const canonical = fs.realpathSync.native(folder);
      found.set(process.platform === 'win32' ? canonical.toLowerCase() : canonical, canonical);
    } catch { /* Stale installation record or disconnected library. */ }
  }
  const steamLibraries = new Set();
  for (const root of records.steam || []) {
    if (!localPath(root)) continue;
    steamLibraries.add(root);
    const folders = vdf(smallText(path.join(root, 'steamapps', 'libraryfolders.vdf'))).libraryfolders;
    for (const [key, item] of Object.entries(folders || {})) {
      if (!/^\d+$/.test(key)) continue;
      const location = typeof item === 'string' ? item : item?.path;
      if (localPath(location)) steamLibraries.add(location);
    }
  }
  for (const library of steamLibraries) {
    const apps = path.join(library, 'steamapps');
    const record = vdf(smallText(path.join(apps, 'appmanifest_' + appId + '.acf'))).appstate;
    const directory = record?.installdir;
    if (record?.appid !== appId || typeof directory !== 'string' || !directory ||
        /[\\/:]/.test(directory) || directory === '.' || directory === '..') continue;
    verify(path.join(apps, 'common', directory));
  }
  for (const folder of records.rockstar || []) verify(folder);
  for (const source of records.epicManifests || []) {
    if (!localPath(source)) continue;
    let entries;
    try { entries = fs.readdirSync(source, {withFileTypes: true}); } catch { continue; }
    for (const entry of entries) {
      if (!entry.isFile() || !entry.name.toLowerCase().endsWith('.item')) continue;
      try {
        const manifest = JSON.parse(smallText(path.join(source, entry.name)));
        if (manifest.DisplayName?.trim().toLowerCase() === title.toLowerCase()) verify(manifest.InstallLocation);
      } catch { /* Other titles and incomplete .item files are in the same folder. */ }
    }
  }
  return [...found.values()];
}

if (require.main === module) {
  try {
    const matches = discover(JSON.parse(smallText(process.argv[2])));
    // ASCII transport preserves non-ASCII Windows paths across older PowerShell code pages.
    if (matches.length === 1) process.stdout.write(Buffer.from(matches[0], 'utf8').toString('base64'));
  } catch { /* Let the normal folder picker handle unknown or missing records. */ }
}
module.exports = {discover};
