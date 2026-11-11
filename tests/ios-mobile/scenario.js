// WKWebView runs this in its own page world, against the unmodified public starter.
const element = id => document.getElementById(id);
const check = (ok, message) => { if (!ok) throw Error(message); };
async function until(test, message) {
  for (let i = 0; i < 150; i++) {
    if (test()) return;
    await new Promise(resolve => setTimeout(resolve, 40));
  }
  throw Error(message + ': ' + element('status').textContent);
}
check(/iPhone/.test(navigator.userAgent), 'Expected the simulator iPhone WebKit user agent');
check(isSecureContext && !!crypto.subtle, 'Expected Web Crypto on loopback');
element('demo').click();
await until(() => !element('output').hidden, 'Demo did not show a receipt');
const receipt = JSON.parse(element('result').value);
check(receipt.schema === 'reyrun.mobile.receipt/1' && receipt.id === 'phone-test-01', 'Receipt identity mismatch');
check(receipt.action === 'inspect-text' && receipt.bytes === 13 && receipt.lines === 2, 'Incorrect receipt contents');
check(receipt.sha256 === '927089762e6199a4a37a3cf75788c5ca045d15698109a55c6d607992a0148ca9', 'Incorrect SHA-256');
const invalid = {schema:'reyrun.mobile.request/1',id:'ignored',action:'unsupported',text:'example'};
const files = new DataTransfer();
files.items.add(new File([JSON.stringify(invalid)], 'invalid.json', {type:'application/json'}));
element('picker').files = files.files;
element('picker').dispatchEvent(new Event('change', {bubbles:true}));
await until(() => element('status').textContent.includes('inspect-text'), 'Unsupported action was not rejected');
check(element('output').hidden, 'The old receipt should disappear after an invalid request');
return {receipt, rejected:true, userAgent:navigator.userAgent};
