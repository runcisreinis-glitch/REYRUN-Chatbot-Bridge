(() => {
  'use strict';
  const get = id => document.getElementById(id);
  const title = get('note-title');
  const body = get('note-body');
  const status = get('status');
  const download = get('download-note');
  const mail = get('draft-mail');
  const params = new URLSearchParams(location.hash.slice(1));
  const values = { title: params.get('title'), body: params.get('body') };
  const received = values.title !== null || values.body !== null;
  const valid = location.hash.length <= 28000 && (values.title || '').length <= title.maxLength &&
    (values.body || '').length <= body.maxLength && !/[\r\n\u0000-\u001F\u007F]/.test(values.title || '') &&
    !/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/.test(values.body || '');
  if (received && valid) {
    title.value = values.title || '';
    body.value = values.body || '';
    status.textContent = status.dataset.received;
  } else if (!valid) {
    status.textContent = status.dataset.invalid;
  }
  function updateActions() {
    const hasText = body.value.trim().length > 0;
    download.disabled = !hasText;
    mail.disabled = !hasText;
  }
  function carryDraft(link) {
    if (!body.value && !title.value) return;
    const next = new URL(link.href);
    next.hash = new URLSearchParams({title: title.value, body: body.value}).toString();
    link.href = next.href;
  }
  for (const link of document.querySelectorAll('a[data-language]')) {
    link.addEventListener('click', () => carryDraft(link));
  }
  for (const field of [title, body]) field.addEventListener('input', updateActions);
  download.addEventListener('click', () => {
    const filename = (title.value.normalize('NFC').replace(/[^\p{L}\p{N} _.()-]/gu,' ').trim().slice(0,70) || 'REYRUN') + '.txt';
    const url = URL.createObjectURL(new Blob([body.value], {type:'text/plain;charset=utf-8'}));
    const a = Object.assign(document.createElement('a'), {href:url, download:filename});
    document.body.append(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 30000);
    status.textContent = status.dataset.saved;
  });
  mail.addEventListener('click', () => {
    if (!body.value.trim()) return;
    const uri = 'mailto:?subject=' + encodeURIComponent(title.value.replace(/[\r\n]/g, ' ')) +
      '&body=' + encodeURIComponent(body.value.replace(/\r?\n/g, '\r\n'));
    if (uri.length > 2000) {
      status.textContent = status.dataset.long;
      return;
    }
    const link = Object.assign(document.createElement('a'), {href:uri});
    document.body.append(link);
    link.click();
    link.remove();
    status.textContent = status.dataset.open;
  });
  const copy = get('copy-request');
  copy.addEventListener('click', async () => {
    const request = get('request-text');
    const target = get('copy-status');
    try {
      await navigator.clipboard.writeText(request.innerText);
      target.textContent = copy.dataset.copied;
    } catch {
      const range = document.createRange();
      range.selectNodeContents(request);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      target.textContent = copy.dataset.select;
    }
  });
  get('sample').addEventListener('click', () => {
    if ((title.value || body.value) && !window.confirm(get('sample').dataset.replace)) return;
    title.value = title.dataset.sample;
    body.value = body.dataset.sample;
    status.textContent = status.dataset.received;
    updateActions();
  });
  updateActions();
})();
