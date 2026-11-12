"""Render the site's own bridge artwork into its social previews (Playwright)."""
from pathlib import Path
from html import escape
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from functools import partial
import argparse
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "web"
COPY = {
    "lv": ("REYRUN Tilts", ("Čatbots tavā", "datorā"), ("Pārbaudi failu", "telefonā"), "Windows un Mac", "Faila pārbaude pārlūkā"),
    "en": ("REYRUN Bridge", ("Your chatbot,", "on your computer"), ("Check a file", "on your phone"), "Windows and Mac", "Check a file in your browser"),
    "ru": ("Мост REYRUN", ("Чат-бот на вашем", "компьютере"), ("Проверьте файл", "на телефоне"), "Windows и Mac", "Проверка файла в браузере"),
}
STYLE = """
*{box-sizing:border-box}body{margin:0;background:#09161d;color:#eff5f3;font-family:Arial,sans-serif}
main{position:relative;width:1200px;height:630px;padding:54px 65px;overflow:hidden;
background:radial-gradient(ellipse at 78% 45%,#20414c 0%,#102731 38%,#08151c 82%)}
.brand{font-size:30px;font-weight:700;letter-spacing:1px;color:#ffbd88}
h1{position:absolute;left:65px;top:164px;margin:0;z-index:1;font-size:67px;line-height:1.07;
letter-spacing:-2.2px;max-width:610px}h1 span{display:block;color:#91f3dc}
p{position:absolute;bottom:30px;left:65px;font-size:28px;color:#cbd9db}
canvas{position:absolute;right:15px;top:104px;width:543px;height:366px}
img{position:absolute;right:54px;bottom:35px;width:83px;height:83px}
"""
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass

def main():
    options = argparse.ArgumentParser()
    options.add_argument("--browser", choices=["chromium","webkit"], default="chromium")
    options.add_argument("--executable-path")
    args = options.parse_args()
    with ThreadingHTTPServer(("127.0.0.1",0), partial(Quiet, directory=str(WEB))) as server, sync_playwright() as pw:
        Thread(target=server.serve_forever, daemon=True).start()
        origin = f"http://127.0.0.1:{server.server_port}"
        browser = getattr(pw, args.browser).launch(executable_path=args.executable_path)
        page = browser.new_page(viewport={"width":1200,"height":630}, reduced_motion="reduce")
        page.goto(origin + "/")
        for lang, (name, home, start, devices, check) in COPY.items():
            for kind, (lines, caption) in {"bridge":(home,devices), "check":(start,check)}.items():
                page.set_content(f'''<!doctype html><html lang="{lang}"><meta charset="utf-8"><style>{STYLE}</style>
                    <main><div class="brand">{escape(name)}</div><h1>{escape(lines[0])}<span>{escape(lines[1])}</span></h1>
                    <canvas id="bridge-art"></canvas><p>{escape(caption)}</p><img src="{origin}/assets/reyrun.png"></main>
                    <script src="{origin}/assets/bridge-visual.js"></script></html>''')
                page.wait_for_function("document.querySelector('img').naturalWidth && document.querySelector('canvas').width > 500")
                page.evaluate("new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))")
                page.screenshot(path=str(WEB / "assets" / f"{kind}-{lang}-v1.jpg"), type="jpeg", quality=91)
        browser.close()
        server.shutdown()
if __name__ == "__main__":
    main()
