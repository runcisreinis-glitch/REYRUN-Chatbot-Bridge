"""Generate static metadata for the public homepage and file checker."""
from html import escape
from pathlib import Path
import json

LOCALES = {"lv": "lv_LV", "en": "en_US", "ru": "ru_RU"}
HOME = {"lv": "/", "en": "/en/", "ru": "/ru/"}
START = {"lv": "/start/", "en": "/en/start/", "ru": "/ru/start/"}
NAMES = {"lv": "REYRUN Tilts", "en": "REYRUN Bridge", "ru": "Мост REYRUN"}
SUMMARY = {
    "lv": "Atrodi savam datoram vai telefonam piemērotu tiltu. Izvēlies Windows, Mac, Linux, Android vai iPhone un izmēģini vienu konkrētu darbību.",
    "en": "Connect a chatbot to your computer or phone. Choose Windows, Mac, Linux, Android or iPhone and try a device-specific task.",
    "ru": "Подключите чат-бота к своему компьютеру или телефону. Выберите Windows, Mac, Linux, Android или iPhone и попробуйте конкретное действие.",
}
ART = {
    "lv":"REYRUN. Metāla tilts savieno mikroshēmu ar datoru un telefonu uz safīrzilas pamatnes.",
    "en":"REYRUN. A metal bridge links a chip, a computer and a phone on sapphire-blue bases.",
    "ru":"REYRUN. Металлический мост соединяет микросхему с компьютером и телефоном на сапфировых подставках.",
}

FLAGS = {"en": "gb", "lv": "lv", "ru": "ru"}
LANG_NAMES = {"en": "English", "lv": "Latviski", "ru": "Русский"}

def language_controls(lang, routes, extra=""):
    links = []
    for key in ("en", "lv", "ru"):
        current = ' aria-current="page"' if key == lang else ''
        links.append(f'<a{extra} lang="{key}" hreflang="{key}" href="{routes[key]}" aria-label="{LANG_NAMES[key]}"{current}>'
                     f'<img class="flag" src="/assets/flags/{FLAGS[key]}.svg" alt="">{key.upper()}</a>')
    return "".join(links)

def theme_button(lang):
    label, light, dark = {
        "lv": ("Tumšais režīms", "Ieslēgt gaišo režīmu", "Ieslēgt tumšo režīmu"),
        "en": ("Dark mode", "Switch to light mode", "Switch to dark mode"),
        "ru": ("Тёмная тема", "Включить светлую тему", "Включить тёмную тему"),
    }[lang]
    return (
        f'<button hidden type="button" class="theme-switch" data-theme-switch '
        f'aria-label="{label}" aria-pressed="false" data-light="{light}" data-dark="{dark}">'
        '<span class="sun" aria-hidden="true">☼</span><span class="moon" aria-hidden="true">☾</span></button>'
    )

def metadata(site, lang, route, title, description):
    kind = "phone" if route.endswith("/phone/") else ("check" if route == START[lang] else "bridge")
    version = 3 if kind == "bridge" else 2
    image = f"{site}/assets/{kind}-{lang}-v{version}.jpg"
    props = [
        ("og:type", "website"), ("og:site_name", NAMES[lang]),
        ("og:url", site + route), ("og:title", title), ("og:description", description),
        ("og:locale", LOCALES[lang]),
        *(("og:locale:alternate", locale) for key, locale in LOCALES.items() if key != lang),
        ("og:image", image), ("og:image:width", "1200"), ("og:image:height", "630"),
        ("og:image:type", "image/jpeg"), ("og:image:alt", ART[lang]),
    ]
    cards = [("twitter:card", "summary_large_image"), ("twitter:title", title),
             ("twitter:description", description), ("twitter:image", image), ("twitter:image:alt", ART[lang])]
    return "\n".join(
        f'<meta {attribute}="{key}" content="{escape(value, quote=True)}">'
        for attribute, fields in (("property", props), ("name", cards)) for key, value in fields
    )

def render_start(web, site, lang):
    source = Path(__file__).parent
    words = json.loads((source / "start-copy.json").read_text(encoding="utf-8"))[lang]
    tpl = (source / "start-template.html").read_text(encoding="utf-8")
    url = site + START[lang]
    title = words["title"] + " · " + NAMES[lang]
    alternatives = "".join(f'<link rel="alternate" hreflang="{key}" href="{site + path}">' for key, path in START.items())
    links = language_controls(lang, START)
    head = (
        f'<link rel="canonical" href="{url}">{alternatives}'
        + f'<meta name="description" content="{escape(words["intro"], quote=True)}">'
        + metadata(site, lang, START[lang], title, words["intro"])
    )
    context = {**{key: escape(value) for key, value in words.items()}, "lang": lang,
               "head": head, "pagetitle": escape(title), "nav": links, "home": HOME[lang], "theme_button": theme_button(lang),
               "theme_js": (web / "assets/theme.js").read_text(encoding="utf-8"),
               "i18n": json.dumps(words, ensure_ascii=False).replace("<", r"\u003c")}
    for key, value in context.items():
        tpl = tpl.replace("{{" + key + "}}", value)
    if "{{" in tpl:
        raise ValueError("Unresolved start page field")
    output = web / START[lang].strip("/") / "index.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(tpl, encoding="utf-8")
