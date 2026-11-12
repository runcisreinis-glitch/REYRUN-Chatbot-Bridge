(() => {
    const meta = name => document.querySelector('meta[property="og:' + name + '"]')?.content || '';
    const imageURL = meta('image');
    if (imageURL && !window.reyrunShareImage) {
        const image = new Image();
        window.reyrunShareImage = image;
        image.src = imageURL;
    }
    const image = window.reyrunShareImage;
    return {
        url: location.href, lang: document.documentElement.lang, title: document.title,
        heading: document.querySelector('h1')?.innerText || '',
        canonical: meta('url'), card: imageURL, cardTitle: meta('title'),
        image: [image?.naturalWidth || 0, image?.naturalHeight || 0],
        client: document.documentElement.clientWidth, scroll: document.documentElement.scrollWidth
    };
})()
