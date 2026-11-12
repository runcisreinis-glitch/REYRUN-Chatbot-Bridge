"""Build the six guide and file-check cards and three phone cards at 1200 × 630."""
import argparse
import base64
from html import escape
from pathlib import Path
from playwright.sync_api import sync_playwright

WEB = Path(__file__).resolve().parents[1] / "web"
COPY = {
    "lv": {"bridge": ("Tilts no čata", "uz tavu datoru", "Windows · Mac · Linux · Android · iPhone"),
           "check": ("Pārbaudi failu", "telefonā.", "Pārbaudi izvēlēto failu un saņem apliecinājumu."),
           "phone": ("No čata", "uz telefonu.", "Saglabā piezīmi vai atver e-pasta melnrakstu.")},
    "en": {"bridge": ("Your AI chat", "on your computer", "Windows · Mac · Linux · Android · iPhone"),
           "check": ("Check a file", "on your phone.", "Choose a file and get a checksum receipt."),
           "phone": ("From your chat", "to your phone.", "Save a note or open an email draft.")},
    "ru": {"bridge": ("Из чата", "на компьютер", "Windows · Mac · Linux · Android · iPhone"),
           "check": ("Проверьте файл", "на телефоне.", "Выберите файл и получите результат проверки."),
           "phone": ("Из чата", "на телефон.", "Сохраните заметку или откройте черновик письма.")},
}
STYLE = """
*{box-sizing:border-box}body{margin:0;font-family:system-ui,sans-serif;color:#eff5ff}
main{position:relative;isolation:isolate;width:1200px;height:630px;overflow:hidden;background:
radial-gradient(ellipse at 95% 15%,#395983 0,transparent 46%),
radial-gradient(ellipse at 54% 105%,#214c89 0,transparent 52%),linear-gradient(130deg,#090f20,#162541 75%,#10213e)}
main:before{content:"";position:absolute;inset:20px;border:1px solid #57729b;border-radius:25px;box-shadow:inset 0 1px #e3f1ff68,0 1px #010813}
main:after{content:"";position:absolute;right:8%;top:20px;width:48%;height:3px;background:linear-gradient(90deg,transparent,#b4dcff,#f6fbff 57%,transparent);border-radius:100%;box-shadow:0 1px 8px #8abaff63}
.brand{display:flex;align-items:center;gap:14px;position:absolute;left:64px;top:56px;font-weight:760;font-size:32px;letter-spacing:.05em}
.brand img{width:58px;height:58px;object-fit:contain;background:linear-gradient(130deg,#293c58,#0c172c);padding:4px;border:1px solid #8ea9d0;border-radius:12px;box-shadow:inset 0 1px #cbdfff97,0 3px 6px #0006}
h1{position:absolute;z-index:1;left:62px;top:155px;margin:0;font-weight:740;line-height:1.04;letter-spacing:-.055em;font-size:65px}
h1 span{display:block;color:#bfd9fa}.art{position:absolute;top:166px;right:40px;width:590px;height:auto;filter:drop-shadow(0 22px 13px #030b1e88)}
footer{position:absolute;left:65px;right:65px;bottom:48px;border-top:1px solid #6081a477;padding-top:19px;font-size:25px;font-weight:520;color:#c7daf4}
"""
def asset_uri(name, kind):
    return f"data:{kind};base64," + base64.b64encode((WEB / "assets" / name).read_bytes()).decode()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--browser", choices=["chromium", "webkit"], default="chromium")
    parser.add_argument("--executable-path")
    parser.add_argument("--kind", choices=["bridge", "check", "phone"])
    args = parser.parse_args()
    logo = asset_uri("reyrun.png", "image/png")
    art = asset_uri("bridge-model.webp", "image/webp")
    with sync_playwright() as pw:
        browser = getattr(pw, args.browser).launch(executable_path=args.executable_path)
        page = browser.new_page(viewport={"width":1200, "height":630}, reduced_motion="reduce")
        for lang, cards in COPY.items():
            for kind, (first, second, caption) in cards.items():
                if args.kind and args.kind != kind:
                    continue
                page.set_content(f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><style>{STYLE}</style>'
                    f'<main><div class="brand"><img src="{logo}">REYRUN</div><h1>{escape(first)}<span>{escape(second)}</span></h1>'
                    f'<img class="art" src="{art}"><footer>{escape(caption)}</footer></main></html>')
                page.evaluate("Promise.all(Array.from(document.images, i=>i.decode()))")
                if page.locator("h1").bounding_box()["width"] > 580:
                    page.locator("h1").evaluate("e=>e.style.fontSize='58px'")
                version = 3 if kind == "bridge" else 2
                page.screenshot(path=str(WEB / "assets" / f"{kind}-{lang}-v{version}.jpg"),
                                type="jpeg", quality=94)
        browser.close()

if __name__ == "__main__":
    main()
