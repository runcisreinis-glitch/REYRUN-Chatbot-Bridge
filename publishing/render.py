"""Build the public static site and its three matching README documents."""
import json, html, zipfile
from pathlib import Path
from wording import COPY, LANGS, tr
import devices
from share import NAMES, START, SUMMARY, metadata, render_start, theme_button, language_controls
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
        entries[0]['proof']+=' '+t('Windows datorā, kurā jau bija Node, uzstādīšana aizņēma 6,68 sekundes. Pārbaudē ierakstījām un nolasījām to pašu tekstu latviski. Failiem ārpus darba mapes piekļūt nevarēja.','On a Windows PC with Node already installed, setup took 6.68 seconds. The test wrote and read back the same Unicode note. It could only access files inside the workspace.','На физическом ПК с Windows и установленным Node чистая установка заняла 6,68 секунды. Запись и чтение текста с диакритикой совпали, запрос вне рабочей папки был отклонён.')
        entries[0]['links'].append(('Windows · JSON',GITHUB+'/blob/main/research/windows-filesystem.json'))
    entries.append(card('REYRUN Task Bridge · 1.0.0',['Windows','macOS'],t('Saglabā paveikto, lai cits čats var turpināt no tās pašas vietas. Katram uzdevumam ir savi pieraksti.','Save where you left off so another chat can pick up the work. Each job has its own revision history.','Сохраните, на чём остановились, чтобы другой чат мог продолжить работу. У каждого задания своя история версий.'),r[l]['windowsLauncher'],t('Projekta paša 12. novembra pārbaude.','Project test on 12 November (Riga).','Собственное испытание проекта 12 ноября по Риге.'),t('Šis profils glabā darba pierakstus. Failu pārkopēšanai izvēlies Filesystem.','This profile stores job notes. Choose Filesystem for copying files.','Профиль сохраняет записи заданий. Для копирования файлов выберите Filesystem.'),[('Windows · JSON',GITHUB+'/blob/main/research/reinis.json'),('4 × stdio',GITHUB+'/blob/main/research/parallel.json')],'jobs'))
    entries[-1]['proof']+=' '+t('Četri vienlaicīgi lokāli klienti saglabāja četrus atsevišķus darbus. No četriem mēģinājumiem vienlaikus mainīt vienu ierakstu izdevās viens. Pēc pārstartēšanas varējām nolasīt visus piecus uzdevumus.','Four simultaneous local clients saved four separate jobs. When all four tried to change one record, one change went through. A fresh process recovered all five jobs.','Четыре локальных клиента одновременно сохранили четыре разные задачи. Когда все четверо попытались изменить одну запись, сохранилось одно изменение. После перезапуска были доступны все пять задач.')
    entries+= [fromdesk(desk[1],'playwright'),fromdesk(desk[2],'devtools')]
    entries.append(card('Desktop Commander · Remote / Local',['Windows','macOS'],t('Fonā strādā ar failiem un termināļa sesijām. Šejienes lokālais palaidējs dod čatam trīs rīkus vienas darba mapes apskatei.','Use files and terminal sessions in the background. Our local launcher offers three inspection tools in one workspace.','Работает с файлами и сеансами терминала в фоне. Наш локальный файл запуска открывает три инструмента для просмотра одной рабочей папки.'),dc['works']+' '+dc['gui'],dc['feedback'],t('Palaidējs lieto lokālo 0.3.2 pakotni. Attālais 0.3.0 ir atsevišķs produkts ar konta piesaisti. Grafiskās pogas var pārbaudīt pārlūka profilā.','The launcher uses local package 0.3.2. Remote 0.3.0 is a separate, paired service. Use a browser profile to inspect graphical controls.','Файл запуска использует локальный пакет 0.3.2. Remote 0.3.0 — отдельный сервис с привязкой. Элементы интерфейса проверяйте в профиле браузера.'),[(k,r['sources'][k]) for k in ['local','remote','help','reportFocus','reportTimeout']],'commander',r['evidence']['githubActivity']['localStars']))
    entries.append(card('Reinis Bridge · 1.0.0',['Windows'],rb['gui'],rb['works'],rb['parallel'],rb['start'],[('REYRUN · Windows',GITHUB+'/blob/main/research/reinis.json')]))
    entries.append(fromdesk(desk[3],'git-handoff'))
    entries+=mobile_cards(l,card)
    native='https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278'
    for i in [0,1,2,3]:
        entries[i]['links'].append(('Windows + macOS · CI',native))
    for i in [2,3]:
        entries[i]['proof']=t('Mūsu Windows un macOS pārbaudēs palaidējs atvēra atsevišķu Chrome procesu un nosūtīja čata klientam ekrānattēlu. Pārbaudē atvērām tukšu lapu un pārliecinājāmies, ka saņemto PNG attēlu var nolasīt.','On both Windows and macOS our launcher opened a separate Chrome process and returned a screenshot to the chat client. We used a blank page and checked that the PNG opened correctly.','На Windows и macOS наш файл запуска открыл отдельный процесс Chrome и передал снимок экрана клиенту чата. Мы открыли пустую страницу и убедились, что полученное изображение PNG читается.')
    counts=[
        ('Vienā mapē failus vienlaikus ļauj mainīt tikai vienam čatam. Atsevišķām mapēm var izmantot atsevišķus savienojumus.','Assign one writer per folder. Separate folders can use separate connections.','Назначьте одного автора для каждой папки. Разным папкам можно дать отдельные подключения.'),
        ('Četri klienti varēja darboties reizē. Pēc pārstartēšanas atradām visus piecus uzdevumus.','Four concurrent clients and five recovered jobs tested.','Проверены четыре параллельных клиента и восстановление пяти задач.'),
        ('Katrai vienlaicīgai sesijai savs pārlūka process un profils. Ar katru pārbaudīto operētājsistēmu izmēģinājām vienu sesiju.','Use a separate process and profile per concurrent browser session. Our check opened one per operating system.','Каждому параллельному сеансу нужны свой процесс и профиль. В нашем тесте открывался один на каждую ОС.'),
        ('Katrā sesijā savs Chrome process. Kopīgs pārlūka profils sajauktu cilnes.','Each session has its own Chrome process. A shared profile can mix up tabs.','В каждом сеансе свой процесс Chrome. В общем профиле вкладки могут смешиваться.'),
        ('Divu rīku failu apmaiņa pārbaudīta. Vienas ierīces maksimālais vienlaicīgo čatu skaits nav izmērīts.','File handoff between two tools was tested. The maximum live-chat count per device was not measured.','Проверена передача файла между двумя инструментами. Предел числа одновременных чатов на устройстве не измерялся.'),
        ('Viena interaktīva darbvirsma. Divi mūsu fona darbi pārklājās 5,011 sekundes.','One interactive desktop. Two observed background jobs overlapped by 5.011 seconds.','Один интерактивный рабочий стол. Два фоновых задания выполнялись одновременно 5,011 секунды.'),
        ('Pārbaudītas divas darba kopijas, katrai savs zars.','Two working copies tested, each on its own branch.','Проверены две рабочие копии, каждая в своей ветке.')]
    for i,row in enumerate(entries):row['parallel']=t(*counts[i]) if i<len(counts) else t('Katram darbam savs fails vai kvīts. Tālruņa kopīgošanas izvēlni izmanto viena darbība reizē.','Give each job its own file or receipt. One action uses the phone share sheet at a time.','У каждого задания свой файл или квитанция. Меню отправки телефона обслуживает одно действие за раз.')
    for slug, systems, title, source in [
        ('windows', ['Windows','macOS','Linux'], 'Desktop Commander Remote · ChatGPT', devices.DC),
        ('android', ['Android'], 'Google Gemini · Device assistance', devices.GOOGLE_HELP),
        ('iphone', ['iOS'], 'Claude · Apple Reminders', devices.CLAUDE_HELP)]:
        desc, proof, limit = {
            'windows': (t('Strādā ar piesaistītā datora failiem no tīmekļa čata.','Work on a paired computer’s files from a web chat.','Работайте с файлами подключённого компьютера из веб-чата.'), t('Izstrādātājs dokumentē Windows, macOS un Linux.','The developer documents Windows, macOS and Linux.','Разработчик описывает Windows, macOS и Linux.'), t('Savienojumam jādarbojas mērķa datorā.','The connection needs to run on the target computer.','Подключение должно работать на целевом компьютере.')),
            'android': (t('Palūdz Gemini iestatīt taimeri telefona lietotnē Pulkstenis.','Ask Gemini to set a timer in the phone’s Clock app.','Попросите Gemini поставить таймер в приложении Часы.'), t('Google apraksta darbību Gemini Android lietotnē.','Google documents the action in the Android Gemini app.','Google описывает действие в приложении Gemini для Android.'), t('Jāizmanto Gemini Android lietotne.','Requires the Gemini Android app.','Требуется приложение Gemini для Android.')),
            'iphone': (t('Izveido atgādinājumu jau esošā iPhone vai iPad sarakstā.','Add a reminder to an existing list on your iPhone or iPad.','Добавьте напоминание в существующий список на iPhone или iPad.'), t('Anthropic apraksta atgādinājumu izveidi ar lietotāja atļauju.','Anthropic documents creating reminders with permission.','Anthropic описывает создание напоминаний с разрешения пользователя.'), t('Vajadzīga Claude mobilā lietotne un atļauja atgādinājumiem.','Requires the Claude mobile app and access to Reminders.','Нужны мобильное приложение Claude и доступ к напоминаниям.'))}[slug]
        row=card(title, systems, desc, proof, t('Izstrādātāja dokumentācija.','Developer documentation.','Документация разработчика.'), limit, [(title,source)], 'device-'+slug)
        row['parallel']=t('Vienlaicīgu savienojumu skaits šim variantam nav mērīts.','Concurrent sessions have not been measured for this route.','Число одновременных сеансов для этого варианта не измерялось.')
        entries.append(row)
    return entries
def mobile_cards(l,card):
    # The mobile evidence table stores independent device-specific field notes.
    entries=[]
    for row in read('mobile-normalized.json'):
        if row.get('launch')=='mobile' and row['name']!='REYRUN · Web Crypto':
            row['sources'].append({'label':'REYRUN · mobile-request.json','url':SITE+'/start/mobile-request.json'})
        entries.append(card(row['name'],row['platforms'],row['use'][l],row['verified'][l],row['community'][l],row['limit'][l],sources(row['sources']),row.get('launch','mobile'),row.get('stars')))
    return entries
def section_actions(d,l,web=True):
    tag=d['launch']
    if not tag:return []
    if tag.startswith('device-'):
        anchor = '#devices' if tag == 'device-windows' else '#'+tag
        return [(PAGES[l]+anchor,tr(l,'Atvērt pamācību','Open setup guide','Открыть инструкцию'))]
    if tag=='mobile':return [(START[l],tr(l,'Atvērt gatavo paraugu','Open the ready-made sample','Открыть готовый пример'))]
    if tag=='termux':return [('/start/mobile-termux.sh',tr(l,'Gatavais Termux skripts','Ready-made Termux script','Готовый скрипт для Termux'))]
    return [(dl(tag,os),os) for os in ('Windows','macOS') if os in d['os']]
def details(d,l,i):
    c=lambda k:tr(l,*COPY[k])
    links=''.join('<li><a href="'+h(u)+'">'+h(n)+'</a></li>' for n,u in d['links'])
    stars='' if d['stars'] is None else ' · GitHub ★ '+f"{d['stars']:,}".replace(',',' ')
    kinds={ 'jobs':('Darba pieraksti','Task notes','Записи задач'), 'filesystem':('Darba mape','Workspace files','Файлы папки'), 'playwright':('Atsevišķs pārlūks','Isolated browser','Отдельный браузер'), 'devtools':('Atsevišķs pārlūks','Isolated browser','Отдельный браузер'), 'commander':('Failu apskate','File inspection','Просмотр файлов'), 'git-handoff':('Darba nodošana','File handoff','Передача работы'), 'termux':('Lokāls skripts','Local script','Локальный скрипт'), 'mobile':('Failu apmaiņa','File handoff','Передача файлов'), None:('Privāta darbvirsma','Private desktop','Личный рабочий стол')}
    meta=tr(l,*kinds.get(d['launch'],('Lietotnes savienojums','Connected app','Подключённое приложение')))+' · '+' · '.join(d['os'])+stars
    actions=''.join(btn(u,n,download=u.startswith('/launchers/')) for u,n in section_actions(d,l))
    return f'''<details class="method" data-platforms="{h(" ".join(d['os']))}"><summary><span class="index">{i:02d}</span><span><strong>{h(d['name'])}</strong><span class="meta">{h(meta)}</span><span class="brief">{h(d['desc'])}</span></span><span aria-hidden="true" class="plus">+</span></summary><div class="inside"><div class="btns">{actions}</div><p><b>{c('tested')}</b> · {h(d['proof'])}</p><p><b>{c('field')}</b> · {h(d['field'])}</p><p><b>{c('parallel_label')}</b> · {h(d['parallel'])}</p><p class="small">{h(d['lim'])}</p><ul>{links}</ul></div></details>'''
def make(l):
    c=lambda k:tr(l,*COPY[k])
    t=lambda *v:tr(l,*v)
    rows=catalog(l)
    guidegame=GAME+{'lv':'/uzstadisana/','en':'/en/install/','ru':'/ru/install/'}[l]
    support=SEARCH+{'lv':'/atbalsts.html','en':'/support.html','ru':'/support.ru.html'}[l]
    search_home=SEARCH+{'lv':'/index.lv.html','en':'/','ru':'/index.ru.html'}[l]
    xml_install='/launchers/REYRUN-RDR2-Install-XML.cmd'
    xml_restore='/launchers/REYRUN-RDR2-Restore-XML.cmd'
    xml_links=f"[{c('xml_install')}]({SITE+xml_install}) · [{c('xml_restore')}]({SITE+xml_restore})"
    skillpath='/download/REYRUN-Bridge-Skill.zip'
    headline=f"{c('h1')} {c('accent')}"
    refbasename='START-'+l+'.md'
    metaurl=url(l)
    prompt=c('prompt')+' '+metaurl+' '+'https://raw.githubusercontent.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/main/skill/reyrun-chatbot-bridge/SKILL.md'
    dcfile='https://mcp.desktopcommander.app/remote-windows.cmd'
    dcapp='https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425'
    dchelp='https://desktopcommander.app/help/devices/connect-computer'
    dcprice='https://desktopcommander.app/help/account-billing/plans-and-tool-call-limits'
    langs=language_controls(l, PAGES)
    opts=''.join('<button type="button" data-filter="'+k+'" aria-pressed="'+('true' if k=='all' else 'false')+'">'+h(name)+'</button>' for k,name in [('all',c('all')),('Windows','Windows'),('macOS','Mac · macOS'),('Linux','Linux'),('Android','Android'),('iOS','iPhone · iPad')])
    qs=''.join(f'<details class="guide"><summary>{c("guide"+str(i))}</summary><p>{c("answer"+str(i))}</p></details>' for i in (1,2,3))
    qs+=f'<details class="guide"><summary>{c("file_task")}</summary><p>{c("file_answer")}</p></details>'
    alts=''.join(f'<link rel="alternate" hreflang="{x}" href="{url(x)}">' for x in LANGS)
    cards=''.join(details(d,l,i) for i,d in enumerate(rows,1))
    data=f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{h(c('title'))} — {h(headline)}</title><meta name="description" content="{h(c('solution'))}"><meta name="theme-color" content="#091329"><link rel="canonical" href="{metaurl}"><link rel="alternate" type="text/markdown" href="https://raw.githubusercontent.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/main/skill/reyrun-chatbot-bridge/SKILL.md">{alts}{metadata(SITE, l, PAGES[l], NAMES[l] + " · " + headline, c('solution'))}<link rel="icon" href="/assets/reyrun.png"><script src="/assets/theme.js"></script><link rel="stylesheet" href="/assets/site.css"><link rel="stylesheet" href="/assets/bridge-glass.css"><script defer src="/assets/site.js"></script></head><body><a class="skip" href="#main">{t('Uz saturu','Skip to content','К содержанию')}</a><header class="masthead"><div class="wrap"><a class="brand" href="{PAGES[l]}"><img alt="" src="/assets/reyrun.png"> <span class="brand-type"><strong>REYRUN</strong><small>{t('Tilts','Bridge','Мост')}</small></span></a><nav class="navmain"><a href="#devices">{t('Ierīces','Devices','Устройства')}</a><a href="#rdr2">RDR2</a><a href="#bridges">{t('Tilti','Bridges','Мосты')}</a><a href="{GITHUB}">GitHub ↗</a></nav><div class="preferences"><nav class="langs language-controls" aria-label="{t('Valoda','Language','Язык')}">{langs}</nav>{theme_button(l)}</div></div></header>
<main id="main"><section class="hero"><div class="wrap heroGrid"><div class="hero-heading"><h1>{h(c('h1'))} <span>{h(c('accent'))}</span></h1><p class="hero-intro">{h(c('opening'))}</p></div><div class="hero-copy"><p class="hero-reassurance">{h(c('solution'))}</p><p class="hero-step">{h(c('how'))}</p><div class="start-chat"><button type="button" class="btn primary" data-copy data-ok="{h(c('copied'))}" data-selected="{h(c('selected'))}" aria-live="polite">{h(c('copy'))}</button><p class="calltext" id="page-address" hidden>{h(metaurl)}</p><noscript><p class="calltext">{h(metaurl)}</p></noscript></div><p class="hero-lead">{h(c('pitch'))}</p><p class="chat-definition">{h(c('definition'))}</p><details class="chat-difference"><summary>{h(c('difference'))}</summary><p>{h(c('explain'))}</p></details></div><figure class="bridge-frame"><img class="bridge-model" src="/assets/bridge-model.webp" width="1120" height="590" fetchpriority="high" alt="{h(t('Metāla tilts starp mikroshēmu, datoru un telefonu','A metal bridge connecting a chip, a computer and a phone','Металлический мост между микросхемой, компьютером и телефоном'))}"><figcaption><span>{c('base')}</span><span>REYRUN</span><span>{c('device')}</span></figcaption></figure></div></section>
<div class="wrap"><section class="author-support"><aside class="person"><div class="byline"><img src="/assets/reinis.webp" alt="Reinis"><div><strong>Reinis</strong><br><small>{c('author')}</small></div></div><p>{c('appeal')}</p>{btn(support,c('support')+' ↗')}</aside></section><details class="guide technical" id="technical"><summary>{h(c('tech'))}</summary><h2>{h(c('skill'))}</h2><p>{h(c('ai_next'))}</p><p><a href="{skillpath}" download>ZIP</a> · <a href="{GITHUB}">GitHub</a></p><p>{h(c('actions'))}</p><h3>{h(c('prompt_title'))}</h3><blockquote class="calltext" id="prompt">{h(prompt)}</blockquote><div class="device-choice">{devices.picker(l)}</div>{devices.section(l)}<section class="content"><article class="pane"><h2>{c('local_setup')}</h2><p>{c('first')} {c('device_note')}</p><div class="btns">{btn(dl('filesystem','Windows'),c('win'),download=True)}{btn(dl('filesystem','macOS'),c('mac'),download=True)}<a href="{skillpath}" download>{c('method')} (.zip)</a></div></article></section>
<section id="chatgpt" class="content pane"><h2>{c('chatgpt_title')}</h2><div class="btns">{btn(dcfile,c('chatgpt_file'),True)}{btn(dchelp,t('Mac un Linux uzstādīšana','Mac and Linux setup','Установка на Mac и Linux'))}{btn(dcapp,c('chatgpt_open'))}</div><p>{c('chatgpt_intro')}</p><small><a href="{dchelp}">Desktop Commander</a> · <a href="{dcprice}">{t('Bezmaksas plāns','Free plan','Бесплатный план')}</a></small></section>
<section id="rdr2" class="content pane"><h2>{c('rdr')}</h2><p>{c('xml_help')}</p><div class="btns">{btn(xml_install,c('xml_install'),True,True)}{btn(xml_restore,c('xml_restore'),download=True)}</div><p>{c('rdr_text')}</p><div class="btns">{btn(dl('rdr2','Windows'),c('rdr_win'),download=True)}{btn(guidegame,c('rdr_guide')+' ↗')}</div></section>
<section id="bridges" class="content"><h2>{c('catalog')}</h2><p class="lead">{c('rank')}</p><div class="filters" aria-label="{c('all')}">{opts}</div><div class="methods">{cards}</div></section><section class="content"><h2>{c('guide')}</h2>{qs}<p><a href="{GITHUB}/blob/main/skill/reyrun-chatbot-bridge/references/{refbasename}">{c('method')} ↗</a> · <a href="{GITHUB}/tree/main/research">{c('evidence')} ↗</a></p></section></details></div></main>
<footer><div class="wrap"><strong>{c('title')}</strong><a href="{GITHUB}">GitHub</a><a href="{guidegame}">RDR2</a><a href="{search_home}">{c('search')}</a><a href="{support}">{c('support')}</a></div></footer></body></html>'''
    external_icon = '<svg class="out-link" aria-hidden="true" width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 9.5 9.5 2.5M3.8 2.5h5.7v5.7"/></svg>'
    data=data.replace(' ↗</a>', ' '+external_icon+'</a>')
    out=WEB/PAGES[l].strip('/');out.mkdir(parents=True,exist_ok=True);(out/'index.html').write_text(data)
    header='[Latviski](%s) · [English](%s) · [Русский](%s)'%tuple(url(x) for x in LANGS)
    starters=f"[{c('win')}]({SITE+dl('filesystem','Windows')}) · [{c('mac')}]({SITE+dl('filesystem','macOS')}) · [{c('phone')}]({SITE}{START[l]})"
    readme=f"# {c('title')} — {headline}\n\n{c('pitch')}\n\n{c('how')}\n\n> {prompt}\n\n{c('actions')}\n\n{starters}\n\n{c('first')} {c('device_note')}\n\n"+' · '.join(f"[{s}]({p})" for s,p in [('Latviski','README.lv.md'),('English','README.md'),('Русский','README.ru.md')])+f" · [{c('title')}]({metaurl})\n\n[{c('method')}]({SITE}{skillpath}) · [SKILL.md](skill/reyrun-chatbot-bridge/SKILL.md)\n\n## {c('rdr')}\n\n{c('xml_help')}\n\n{xml_links}\n\n{c('rdr_text')}\n\n[{c('rdr_win')}]({SITE+dl('rdr2','Windows')}) · [{c('rdr_guide')}]({guidegame})\n\n## {c('catalog')}\n\n{c('rank')}\n\n"
    dcguide=f"## {c('chatgpt_title')}\n\n[{c('chatgpt_file')}]({dcfile}) · [{c('chatgpt_open')}]({dcapp})\n\n{c('chatgpt_intro')} [Desktop Commander]({dchelp}) · [{t('Bezmaksas plāns','Free plan','Бесплатный план')}]({dcprice})\n\n"
    device_links=' · '.join(f'[{devices.NAMES[key]}]({metaurl}#device-{key})' for key in devices.DEVICES)
    handoff=devices.paths(l)[0]
    mobile_links=f'[{t("Piezīme vai e-pasts telefonā","Prepare a note or email on your phone","Заметка или письмо на телефоне")}]({SITE}{handoff})'
    readme=readme.replace('## '+c('catalog'),device_links+'\n\n'+mobile_links+'\n\n'+dcguide+'## '+c('catalog'))
    long='# '+c('method')+' · '+c('title')+'\n\n'+header+'\n\n'+starters+'\n\n'+c('first')+' '+c('device_note')+'\n\n'
    long+=device_links+'\n\n'+mobile_links+'\n\n'+dcguide
    specific=t('Pārbaudes pēc palaidēja atvēršanas','Checks after opening the launcher','Проверка после запуска')
    actions=t('Files lietotnē izsauc list_allowed_directories. Izveido testa failu tikai parādītajā darba mapē un nolasi tā saturu. Ja rezultāts nesakrīt, neveic instalāciju. Task Bridge profilā izsauc bridge_status, pēc tam read_checkpoint. Pirms pirmās save_checkpoint izmanto revision 0. Pēc savienojuma pārrāvuma izsauc read_checkpoint ar to pašu darba nosaukumu.','For Filesystem, call list_allowed_directories. Write one test file in the returned workspace and read it back. If the contents differ, stop the installation. For Task Bridge call bridge_status, then read_checkpoint. Use revision 0 for the first save_checkpoint. After a disconnect, call read_checkpoint with the same job ID.','Для Filesystem вызовите list_allowed_directories. Создайте тестовый файл в показанной папке и прочитайте его. Если содержимое отличается, остановите установку. Для Task Bridge вызовите bridge_status и read_checkpoint. Для первого save_checkpoint используйте revision 0. После обрыва связи вызовите read_checkpoint с прежним именем задания.')
    long+=f"## {specific}\n\n{actions}\n\n"
    for i,d in enumerate(rows,1):
        plat=', '.join(d['os']);guideactions=section_actions(d,l)
        linktext=' · '.join(f'[{label}]({SITE+u})' for u,label in guideactions)
        readme+=f"{i}. **{d['name']}** ({plat}) — {d['desc']} "+(linktext+' ' if linktext else '')+f"[{c('tested')}]({metaurl}#bridges)\n"
        links=' · '.join(f'[{n}]({u})' for n,u in d['links'])
        long+=f"## {i}. {d['name']}\n\n{plat}. {d['desc']}\n\n{linktext}\n\n**{c('tested')}.** {d['proof']}\n\n**{c('field')}.** {d['field']}\n\n{d['lim']}\n\n**{c('parallel_label')}.** {d['parallel']}\n\n{links}\n\n"
    long+='## '+c('rdr')+'\n\n'+c('xml_help')+'\n\n'+xml_links+'\n\n'+c('rdr_text')+f" [{c('rdr_guide')}]({guidegame})\n\n"
    for i in (1,2,3):long+='## '+c('guide'+str(i))+'\n\n'+c('answer'+str(i))+'\n\n'
    long+='## '+c('file_task')+'\n\n'+c('file_answer')+'\n'
    long+='\n## '+c('client')+'\n\n'+c('client_text')+'\n\n## '+c('resume_test')+'\n\n'+c('resume_text')+'\n\n'
    example={'name':'save_checkpoint','arguments':{'job':'game-check','revision':0,'done':t('Testa fails precīzi nolasīts.','Test note read back exactly.','Тестовый файл прочитан без изменений.'),'next':t('Pārbaudi izvēlēto spēles mapi.','Verify the selected game folder.','Проверь выбранную папку игры.')}}
    long+='\n```json\n'+json.dumps(example,ensure_ascii=False,indent=2)+'\n```\n'
    heading, rest = long.split('\n\n', 1)
    note = json.loads((ROOT / 'publishing' / 'one-launcher.json').read_text(encoding='utf-8'))[l]
    long = heading + '\n\n' + note + '\n\n' + rest
    (REFS/refbasename).write_text(long)
    readme+=f"\n[{c('evidence')}](skill/reyrun-chatbot-bridge/references/{refbasename}) · [JSON](research/)\n\n"
    for i in (1,2):readme+=f"### {c('guide'+str(i))}\n\n{c('answer'+str(i))}\n\n"
    readme+=f"{c('appeal')} [{c('support')}]({support}) · [{c('search')}]({search_home})\n"
    full_guide = readme[readme.index(starters):]
    readme = (f"# {c('title')} · {headline}\n\n{c('opening')}\n\n{c('solution')}\n\n{c('pitch')}\n\n{c('how')}\n\n"
              f"[{c('open_page')}]({metaurl})\n\n{c('definition')}\n\n{header}\n\n"
              f"<details>\n<summary>{c('tech')}</summary>\n\n"
              f"{c('skill')} · [SKILL.md](skill/reyrun-chatbot-bridge/SKILL.md)\n\n"
              f"{c('ai_next')}\n\n> {prompt}\n\n{c('actions')}\n\n{full_guide}\n</details>\n")
    (ROOT/({'lv':'README.lv.md','en':'README.md','ru':'README.ru.md'}[l])).write_text(readme)
if __name__=='__main__':
    for l in LANGS:
        make(l)
        render_start(WEB, SITE, l)
    dest=WEB/'download';dest.mkdir(exist_ok=True)
    with zipfile.ZipFile(dest/'REYRUN-Bridge-Skill.zip','w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted((ROOT/'skill').rglob('*')):
            if f.is_file():
                entry=zipfile.ZipInfo(str(f.relative_to(ROOT/'skill')), (2026,11,12,0,0,0))
                entry.external_attr=0o100644 << 16
                z.writestr(entry,f.read_bytes(),compress_type=zipfile.ZIP_DEFLATED)
