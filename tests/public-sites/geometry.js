(() => {
    const meta = name => document.querySelector('meta[property="og:' + name + '"]')?.content || '';
    const imageURL = meta('image');
    if (imageURL && !window.reyrunShareImage) {
        const image = new Image();
        window.reyrunShareImage = image;
        image.src = imageURL;
    }
    const headerControls = [...document.querySelectorAll('header a, header button, header select')].map(el => ({
        name: (el.textContent.trim() || el.getAttribute('aria-label') || el.tagName).slice(0,48),
        rect: el.getBoundingClientRect()
    })).filter(item => item.rect.width > 0 && item.rect.height > 0);
    const overlaps = [];
    for (let i=0; i<headerControls.length; ++i) {
        const a=headerControls[i];
        for (const b of headerControls.slice(i+1)) {
            const w = Math.min(a.rect.right,b.rect.right) - Math.max(a.rect.left,b.rect.left);
            const h = Math.min(a.rect.bottom,b.rect.bottom) - Math.max(a.rect.top,b.rect.top);
            if (w > 2 && h > 2) overlaps.push([a.name,b.name]);
        }
    }
    const hasInstaller = [...document.links].some(a=>a.pathname.endsWith('/REYRUN-RDR2-Install-XML.cmd'));
    const image = window.reyrunShareImage;
    return {
        url: location.href, lang: document.documentElement.lang, title: document.title,
        heading: document.querySelector('h1')?.innerText || '',
        overlaps, hasInstaller, canonical: meta('url'), card: imageURL, cardTitle: meta('title'),
        image: [image?.naturalWidth || 0, image?.naturalHeight || 0],
        client: document.documentElement.clientWidth, scroll: document.documentElement.scrollWidth
    };
})()
