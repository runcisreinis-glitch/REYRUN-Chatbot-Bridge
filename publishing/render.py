"""Build the public static site and its three matching README documents."""
import json, html, shutil, zipfile
from pathlib import Path
from wording import COPY, LANGS, tr
ROOT=Path(__file__).resolve().parents[1]
WEB=ROOT/'web'
REFS=ROOT/'skill/reyrun-chatbot-bridge/references'
SITE='https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site'
GITHUB='https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge'
GAME='https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site'
SEARCH='https://reyrun-rekursive-deep-search.runcisreinis.chatgpt.site'
PAGES={'lv':'/','en':'/en/','ru':'/ru/'}
def read(name): return json.loads((ROOT/'research'/name).read_text())
def h(a): return html.escape(str(a),quote=True)
def url(l):return SITE+PAGES[l]
def dl(mode,platform):
    extension='Windows.cmd' if platform=='Windows' else 'macOS.command.zip'
    return '/launchers/REYRUN-'+mode+'-'+extension
def btn(target,label,primary=False,download=False):
    return '<a class="btn'+(' primary' if primary else '')+'" href="'+h(target)+'"'+(' download' if download else '')+'>'+h(label)+'</a>'
def sources(items):
    return [(v['label'],v['url']) for v in items if v.get('url','').startswith('https://')]
def catalog(l):
    t=lambda *v:tr(l,*v)
    desk=read('desktop.json')['projects']
    r=read('reinis.json')
    dc=r[l]['desktopCommander']; rb=r[l]['reinis']
    def card(name,os,desc,proof,field,lim,links,launch=None,stars=None):
        return dict(name=name,os=os,desc=desc,proof=proof,field=field,lim=lim,links=links,launch=launch,stars=stars)
    def fromdesk(d,profile):
        return card(d['name']+' · '+d['version'],d['platforms'],d['use'][l],d['verified'][l],d['community'][l],d['limit'][l],sources(d['sources'])+([('GitHub · '+d['stars']['repository'],d['stars']['url'])] if d.get('stars',{}).get('url') else []),profile,d.get('stars',{}).get('count'))
    entries=[fromdesk(desk[0],'filesystem')]
    if (ROOT/'research/windows-filesystem.json').exists():
        entries[0]['proof']+=' '+t('Uz fiziska Windows datora svaiga uzstādīšana ar esošu Node aizņēma 6,68 sekundes. Latviešu teksta fails tika ierakstīts un precīzi nolasīts. Piekļuve ārpus darba mapes tika atteikta.','On a physical Windows PC with Node already present a fresh install took 6.68 seconds. A Unicode note survived a write/read round trip and access outside the workspace was refused.','На физическом ПК с Windows и установленным Node чистая установка заняла 6,68 секунды. Запись и чтение текста с диакритикой совпали, запрос вне рабочей папки был отклонён.')
        entries[0]['links'].append(('Windows · JSON',GITHUB+'/blob/main/research/windows-filesystem.json'))
    entries.append(card('REYRUN Task Bridge · 1.0.0',['Windows','macOS'],t('Nodod nākamajam čatam precīzi to vietu, kur darbs apstājās. Katram darbam ir sava pierakstu vēsture.','Pass an exact stopping point to your next chat. Each job has its own revision history.','Передайте следующему чату точную точку остановки. У каждого задания своя история версий.'),r[l]['windowsLauncher'],t('Projekta paša 12. novembra pārbaude.','Project test on 12 November (Riga).','Собственное испытание проекта 12 ноября по Риге.'),t('Šis profils glabā darba pierakstus. Failu pārkopēšanai izvēlies Filesystem.','This profile stores job notes. Choose Filesystem for copying files.','Профиль сохраняет записи заданий. Для копирования файлов выберите Filesystem.'),[('Windows · JSON',GITHUB+'/blob/main/research/reinis.json'),('4 × stdio',GITHUB+'/blob/main/research/parallel.json')],'jobs'))
    entries[-1]['proof']+=' '+t('Četri vienlaicīgi lokāli klienti saglabāja četrus atsevišķus darbus. Kopīgajā ierakstā uzvarēja viens no četriem. Pēc restartēšanas varēja nolasīt visus piecus darbus.','Four simultaneous local clients saved four separate jobs. One of four writers won the shared record. A fresh process recovered all five jobs.','Четыре локальных клиента одновременно сохранили четыре разные задачи. При общей записи сработала одна из четырёх попыток. После перезапуска были доступны все пять задач.')
    entries+= [fromdesk(desk[1],'playwright'),fromdesk(desk[2],'devtools')]
    entries.append(card('Desktop Commander · Remote / Local',['Windows','macOS'],t('Fonā strādā ar failiem un termināļa sesijām. Šejienes lokālais palaidējs dod čatam trīs rīkus vienas darba mapes apskatei.','Use files and terminal sessions in the background. Our local launcher offers three inspection tools in one workspace.','Работает с файлами и сеансами терминала в фоне. Наш локальный файл запуска открывает три инструмента для просмотра одной рабочей папки.'),dc['works']+' '+dc['gui'],dc['feedback'],t('Palaidējs lieto lokālo 0.3.2 pakotni. Attālais 0.3.0 ir atsevišķs produkts ar konta piesaisti. Grafiskās pogas var pārbaudīt pārlūka profilā.','The launcher uses local package 0.3.2. Remote 0.3.0 is a separate, paired service. Use a browser profile to inspect graphical controls.','Файл запуска использует локальный пакет 0.3.2. Remote 0.3.0 — отдельный сервис с привязкой. Элементы интерфейса проверяйте в профиле браузера.'),[(k,r['sources'][k]) for k in ['local','remote','help','reportFocus','reportTimeout']],'commander',r['evidence']['githubActivity']['localStars']))
    entries.append(card('Reinis Bridge · 1.0.0',['Windows'],rb['gui'],rb['works'],rb['parallel'],rb['start'],[('REYRUN · Windows',GITHUB+'/blob/main/research/reinis.json')]))
    entries.append(fromdesk(desk[3],'git-handoff'))
    entries+=mobile_cards(l,card)
    return entries
def mobile_cards(l,card):
    # The mobile evidence table stores independent device-specific field notes.
    entries=[]
    for row in read('mobile-normalized.json'):
        entries.append(card(row['name'],row['platforms'],row['use'][l],row['verified'][l],row['community'][l],row['limit'][l],sources(row['sources']),row.get('launch','mobile'),row.get('stars')))
    return entries
def section_actions(d,l,web=True):
    tag=d['launch']
    if not tag:return []
    if tag=='mobile':return [('/start/?lang='+l,tr(l,'Atvērt gatavo paraugu','Open the ready-made sample','Открыть готовый пример'))]
    if tag=='termux':return [('/start/mobile-termux.sh',tr(l,'Gatavais Termux skripts','Ready-made Termux script','Готовый скрипт для Termux'))]
    return [(dl(tag,os),os) for os in ('Windows','macOS') if os in d['os']]
def details(d,l,i):
    c=lambda k:tr(l,*COPY[k])
    links=''.join('<li><a href="'+h(u)+'">'+h(n)+'</a></li>' for n,u in d['links'])
    stars='' if d['stars'] is None else ' · GitHub ★ '+f"{d['stars']:,}".replace(',',' ')
    meta=' · '.join(d['os'])+stars
    actions=''.join(btn(u,n,download=u.startswith('/launchers/')) for u,n in section_actions(d,l))
    return f'''<details class="method" data-platforms="{h(" ".join(d['os']))}"><summary><span class="index">{i:02d}</span><span><strong>{h(d['name'])}</strong><span class="meta">{h(meta)}</span><span class="brief">{h(d['desc'])}</span></span><span aria-hidden="true" class="plus">+</span></summary><div class="inside"><div class="btns">{actions}</div><p><b>{c('tested')}</b> · {h(d['proof'])}</p><p><b>{c('field')}</b> · {h(d['field'])}</p><p class="small">{h(d['lim'])}</p><ul>{links}</ul></div></details>'''
def make(l):
    c=lambda k:tr(l,*COPY[k])
    t=lambda *v:tr(l,*v)
    rows=catalog(l)
    guidegame=GAME+('/uzstadisana/' if l=='lv' else '/en/install/')
    support=SEARCH+('/atbalsts.html' if l=='lv' else '/support.html')
    skillpath='/download/REYRUN-Bridge-Skill.zip'
    headline=f"{c('h1')} {c('accent')}"
    refbasename='START-'+l+'.md'
    metaurl=url(l)
    prompt=c('prompt')+' '+metaurl
    langs=''.join(f'<a lang="{x}" hreflang="{x}" href="{PAGES[x]}"'+(' aria-current="page"' if x==l else '')+f'>{x.upper()}</a>' for x in LANGS)
    opts=''.join('<button type="button" data-filter="'+k+'" aria-pressed="'+('true' if k=='all' else 'false')+'">'+h(name)+'</button>' for k,name in [('all',c('all')),('Windows','Windows'),('macOS','macOS'),('Android','Android'),('iOS','iPhone')])
    qs=''.join(f'<details class="guide"><summary>{c("guide"+str(i))}</summary><p>{c("answer"+str(i))}</p></details>' for i in (1,2,3))
    qs+=f'<details class="guide"><summary>{c("file_task")}</summary><p>{c("file_answer")}</p></details>'
    alts=''.join(f'<link rel="alternate" hreflang="{x}" href="{url(x)}">' for x in LANGS)
    cards=''.join(details(d,l,i) for i,d in enumerate(rows,1))
    data=f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{h(c('title'))} — {h(headline)}</title><meta name="description" content="{h(c('pitch'))}"><meta name="theme-color" content="#0b191f"><link rel="canonical" href="{metaurl}">{alts}<link rel="icon" href="/assets/reyrun.png"><link rel="stylesheet" href="/assets/site.css"><script defer src="/assets/bridge-visual.js"></script><script defer src="/assets/site.js"></script></head><body><a class="skip" href="#main">{t('Uz saturu','Skip to content','К содержанию')}</a><header><div class="wrap"><a class="brand" href="{PAGES[l]}"><img alt="" src="/assets/reyrun.png"> {h(c('title').upper())}</a><nav class="navmain"><a href="#rdr2">RDR2</a><a href="#bridges">{t('Tilti','Bridges','Мосты')}</a><a href="{GITHUB}">GitHub ↗</a></nav><nav class="langs" aria-label="{t('Valoda','Language','Язык')}">{langs}</nav></div></header>
<main id="main"><section class="hero"><div class="wrap heroGrid"><div><h1>{h(c('h1'))}<span>{h(c('accent'))}</span></h1><p>{h(c('pitch'))}</p><div class="btns" id="first-launch">{btn(dl('filesystem','Windows'),c('win'),True,True)}{btn(dl('filesystem','macOS'),c('mac'),download=True)}</div><p class="small"><a id="browser-start" href="/start/?lang={l}">{c('phone')} →</a></p></div><figure><canvas id="bridge-art" width="680" height="385" role="img" aria-label="{h(t('Gaismas tilts starp MI un datoru','An illuminated bridge from an AI to a computer','Световой мост от ИИ к компьютеру'))}"></canvas><figcaption><span>{c('base')}</span><span>REYRUN</span><span>{c('device')}</span></figcaption></figure></div></section>
<div class="wrap"><section class="content board"><article class="pane"><h2>{c('prompt_title')}</h2><blockquote class="calltext" id="prompt">{h(prompt)}</blockquote><div class="btns"><button class="btn" data-copy data-ok="{c('copied')}" data-selected="{c('selected')}">{c('copy')}</button><a href="{skillpath}" download>{c('method')} (.zip)</a></div><p class="small">{c('first')} {c('device_note')}</p></article><aside class="person"><div class="byline"><img src="/assets/reinis.webp" alt="Reinis"><div><strong>Reinis</strong><br><small>{c('author')}</small></div></div><p>{c('appeal')}</p>{btn(support,c('support')+' ↗')}</aside></section>
<section id="rdr2" class="content pane"><h2>{c('rdr')}</h2><p>{c('rdr_text')}</p><div class="btns">{btn(dl('rdr2','Windows'),c('rdr_win'),True,True)}{btn(guidegame,c('rdr_guide')+' ↗')}</div></section>
<section id="bridges" class="content"><h2>{c('catalog')}</h2><p class="lead">{c('rank')}</p><div class="filters" aria-label="{c('all')}">{opts}</div><div class="methods">{cards}</div></section><section class="content"><h2>{c('guide')}</h2>{qs}<p><a href="{GITHUB}/blob/main/skill/reyrun-chatbot-bridge/references/{refbasename}">{c('method')} ↗</a> · <a href="{GITHUB}/tree/main/research">{c('evidence')} ↗</a></p></section></div></main>
<footer><div class="wrap"><strong>{c('title')}</strong><a href="{GITHUB}">GitHub</a><a href="{guidegame}">RDR2</a><a href="{SEARCH}/">{c('search')}</a><a href="{support}">{c('support')}</a></div></footer></body></html>'''
    out=WEB/PAGES[l].strip('/');out.mkdir(parents=True,exist_ok=True);(out/'index.html').write_text(data)
    header='[Latviski](%s) · [English](%s) · [Русский](%s)'%tuple(url(x) for x in LANGS)
    starters=f"[{c('win')}]({SITE+dl('filesystem','Windows')}) · [{c('mac')}]({SITE+dl('filesystem','macOS')}) · [{c('phone')}]({SITE}/start/?lang={l})"
    readme=f"# {c('title')} — {headline}\n\n{starters}\n\n{c('first')} {c('device_note')}\n\n"+' · '.join(f"[{s}]({p})" for s,p in [('Latviski','README.lv.md'),('English','README.md'),('Русский','README.ru.md')])+f" · [{c('title')}]({metaurl})\n\n## {c('prompt_title')}\n\n> {prompt}\n\n[{c('method')}]({SITE}{skillpath}) · [SKILL.md](skill/reyrun-chatbot-bridge/SKILL.md)\n\n## {c('rdr')}\n\n{c('rdr_text')}\n\n[{c('rdr_win')}]({SITE+dl('rdr2','Windows')}) · [{c('rdr_guide')}]({guidegame})\n\n## {c('catalog')}\n\n{c('rank')}\n\n"
    long='# '+c('method')+' · '+c('title')+'\n\n'+header+'\n\n'+starters+'\n\n'+c('first')+' '+c('device_note')+'\n\n'
    specific=t('Pārbaudes pēc palaidēja atvēršanas','Checks after opening the launcher','Проверка после запуска')
    actions=t('Files lietotnē izsauc list_allowed_directories. Izveido testa failu tikai parādītajā darba mapē un nolasi tā saturu. Ja rezultāts nesakrīt, neveic instalāciju. Task Bridge profilā izsauc bridge_status, pēc tam read_checkpoint. Pirms pirmās save_checkpoint izmanto revision 0. Pēc savienojuma pārrāvuma izsauc read_checkpoint ar to pašu darba nosaukumu.','For Filesystem, call list_allowed_directories. Write one test file in the returned workspace and read it back. If the contents differ, stop the installation. For Task Bridge call bridge_status, then read_checkpoint. Use revision 0 for the first save_checkpoint. After a disconnect, call read_checkpoint with the same job ID.','Для Filesystem вызовите list_allowed_directories. Создайте тестовый файл в показанной папке и прочитайте его. Если содержимое отличается, остановите установку. Для Task Bridge вызовите bridge_status и read_checkpoint. Для первого save_checkpoint используйте revision 0. После обрыва связи вызовите read_checkpoint с прежним именем задания.')
    long+=f"## {specific}\n\n{actions}\n\n"
    for i,d in enumerate(rows,1):
        plat=', '.join(d['os']);guideactions=section_actions(d,l)
        linktext=' · '.join(f'[{label}]({SITE+u})' for u,label in guideactions)
        readme+=f"{i}. **{d['name']}** ({plat}) — {d['desc']} "+(linktext+' ' if linktext else '')+f"[{c('tested')}]({metaurl}#bridges)\n"
        links=' · '.join(f'[{n}]({u})' for n,u in d['links'])
        long+=f"## {i}. {d['name']}\n\n{plat}. {d['desc']}\n\n{linktext}\n\n**{c('tested')}.** {d['proof']}\n\n**{c('field')}.** {d['field']}\n\n{d['lim']}\n\n{links}\n\n"
    long+='## '+c('rdr')+'\n\n'+c('rdr_text')+f" [{c('rdr_guide')}]({guidegame})\n\n"
    for i in (1,2,3):long+='## '+c('guide'+str(i))+'\n\n'+c('answer'+str(i))+'\n\n'
    long+='## '+c('file_task')+'\n\n'+c('file_answer')+'\n'
    (REFS/refbasename).write_text(long)
    readme+=f"\n[{c('evidence')}](skill/reyrun-chatbot-bridge/references/{refbasename}) · [JSON](research/)\n\n"
    for i in (1,2):readme+=f"### {c('guide'+str(i))}\n\n{c('answer'+str(i))}\n\n"
    readme+=f"{c('appeal')} [{c('support')}]({support}) · [{c('search')}]({SEARCH}/)\n"
    (ROOT/({'lv':'README.lv.md','en':'README.md','ru':'README.ru.md'}[l])).write_text(readme)
if __name__=='__main__':
    for l in LANGS:make(l)
    dest=WEB/'download';dest.mkdir(exist_ok=True)
    with zipfile.ZipFile(dest/'REYRUN-Bridge-Skill.zip','w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted((ROOT/'skill').rglob('*')):
            if f.is_file():z.write(f,f.relative_to(ROOT/'skill'))
