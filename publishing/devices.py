"""Device-specific starting points for the public site and its written guides."""
from html import escape
from wording import tr

DEVICES = ("windows", "mac", "android", "iphone", "linux")
NAMES = {"windows": "Windows", "mac": "Mac · macOS", "android": "Android", "iphone": "iPhone · iPad", "linux": "Linux"}
DC = "https://desktopcommander.app/help/devices/connect-computer"
DC_ANDROID = "https://desktopcommander.app/help/devices/connect-android-phone"
DC_WIN = "https://mcp.desktopcommander.app/remote-windows.cmd"
GEMINI = "https://play.google.com/store/apps/details?id=com.google.android.apps.bard"
GOOGLE_HELP = "https://support.google.com/gemini/answer/15235441"
CLAUDE = "https://apps.apple.com/app/id6473753684"
CLAUDE_HELP = "https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps"

def paths(lang):
    prefix = "/" if lang == "lv" else f"/{lang}/"
    return prefix + "phone/", prefix + "start/"

def guides(lang):
    def t(*words):
        return tr(lang, *words)
    phone, checker = paths(lang)
    handoff = (
        t("Ar citu tīmekļa čatu", "With another web chatbot", "С другим веб-чатом"),
        t("Čatbots sagatavo piezīmes tekstu vai e-pasta melnrakstu. Tu apskati saturu telefonā un izvēlies, vai saglabāt failu vai atvērt melnrakstu pasta lietotnē. Vēstuli nosūti pats.",
          "Have the chatbot prepare a note or an email draft. Review it on your phone, then choose whether to save the file or open the draft in your mail app. You choose when to send.",
          "Попросите чат-бота подготовить заметку или черновик письма. Проверьте текст на телефоне и выберите, сохранить файл или открыть черновик в почтовом приложении. Отправку подтверждаете вы."),
        [(t("Sagatavot piezīmi vai vēstuli", "Prepare a note or email", "Подготовить заметку или письмо"), phone),
         (t("Pārbaudīt faila kontrolsummu", "Check a file checksum", "Проверить контрольную сумму файла"), checker)])
    desktop = {}
    for device in ("windows", "mac", "linux"):
        os = NAMES[device]
        steps = {
            "windows": t("Atver oficiālo Windows palaidēju.", "Open the official Windows launcher.", "Откройте официальный файл запуска для Windows."),
            "mac": t("Atver oficiālo pamācību un izmanto sadaļā Mac norādīto komandu lietotnē Terminal.", "Open the official guide and run its Mac setup command in Terminal.", "Откройте официальную инструкцию и выполните команду из раздела Mac в Терминале."),
            "linux": t("Atver oficiālo pamācību un izpildi tajā norādīto Linux uzstādīšanas komandu.", "Open the official guide and run its Linux setup command in your terminal.", "Откройте официальную инструкцию и выполните в терминале команду установки для Linux.")
        }[device]
        remote = (
            "ChatGPT · Desktop Commander Remote",
            steps + " " + t("Pievieno ChatGPT lietotni Remote Desktop Commander, pieraksties, salīdzini ierīces kodu ar terminālī redzamo un apstiprini sakritību. Atstāj termināli atvērtu. Palūdz čatā parādīt pieslēgtās ierīces un nolasīt vienu sava testa faila rindu. Savienojumu aptur ar Ctrl+C.",
                               "Connect the Remote Desktop Commander app in ChatGPT and sign in. Match the device code to the one in your terminal, confirm it and leave the terminal open. Ask the chat to list your connected devices and read one line of your test file. Press Ctrl+C to stop the connection.",
                               "Подключите приложение Remote Desktop Commander в ChatGPT и войдите в аккаунт. Сверьте код с кодом в терминале, подтвердите совпадение и оставьте терминал открытым. Попросите чат показать подключённые устройства и прочитать одну строку из вашего тестового файла. Ctrl+C останавливает подключение."),
            ([(t("Lejupielādēt Windows palaidēju", "Download Windows launcher", "Скачать файл запуска для Windows"), DC_WIN)] if device == "windows" else []) +
            [(t("Oficiālā uzstādīšana", "Official setup guide", "Официальная инструкция"), DC),
             (t("Pievienot ChatGPT", "Connect in ChatGPT", "Подключить в ChatGPT"), "https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425")])
        rows = [remote]
        if device != "linux":
            platform = "Windows" if device == "windows" else "macOS"
            ext = "Windows.cmd" if device == "windows" else "macOS.command.zip"
            local = t("Lejupielādē REYRUN palaidēju un atver to datorā, kurā jau ir Claude Desktop.", "Download the REYRUN launcher and open it on the computer where Claude Desktop is installed.", "Скачайте файл запуска REYRUN и откройте его на компьютере с установленным Claude Desktop.")
            if device == "mac":
                local += " " + t("Atver ZIP arhīvu un tajā esošo .command failu.", "Unzip the download and open the .command file inside.", "Распакуйте ZIP и откройте находящийся внутри файл .command.")
            local += " " + t("Pilnībā aizver un vēlreiz atver Claude Desktop. Palūdz izveidot un nolasīt piezīmi tā darba mapē.", "Quit and reopen Claude Desktop. Ask it to create a note in its workspace and read it back.", "Полностью закройте и снова откройте Claude Desktop. Попросите его создать и прочитать заметку в рабочей папке.")
            rows.append(("Claude Desktop · REYRUN", local,
                         [(f"REYRUN · {platform}", f"/launchers/REYRUN-filesystem-{ext}")]))
        desktop[device] = rows
    desktop["android"] = [
        ("Google Gemini · Android",
         t("Atver Gemini lietotni telefonā un palūdz iestatīt taimeri uz piecām minūtēm. Atver lietotni Pulkstenis un pārbaudi atlikušo laiku. Ja darbība nav pieejama, Gemini savienoto lietotņu sarakstā pārbaudi Device assistance (agrāk Utilities).",
           "Open the Gemini app on your phone and ask it to set a five-minute timer. Open the Clock app to see it count down. If Gemini cannot set it, check that Device assistance (formerly Utilities) is enabled in Connected Apps.",
           "Откройте Gemini на телефоне и попросите поставить таймер на пять минут. Откройте приложение Часы и проверьте обратный отсчёт. Если действие недоступно, проверьте в списке подключённых приложений Gemini функцию Device assistance (прежнее название — Utilities)."),
         [("Google Play · Gemini", GEMINI), (t("Google pamācība", "Google’s guide", "Справка Google"), GOOGLE_HELP)]),
        ("ChatGPT · Desktop Commander Remote",
         t("Ja mērķis ir Android faili, izstrādātājs piedāvā eksperimentālu savienojumu ar Termux. Pēc savienošanas palūdz parādīt telefonā brīvo vietu. Čatam ir Termux piešķirtās tiesības. Android var apturēt savienojumu fonā.",
           "For files on the Android device, the developer documents an experimental Termux connection. After pairing, ask the chat how much space is free on the phone. Access follows Termux permissions. Android may stop the connection in the background.",
           "Для работы с файлами Android разработчик описывает экспериментальное подключение через Termux. После подключения спросите в чате, сколько на телефоне свободного места. Доступ ограничен правами Termux. Android может остановить соединение в фоне."),
         [(t("Izstrādātāja Android pamācība", "Developer’s Android guide", "Инструкция разработчика для Android"), DC_ANDROID)]),
        handoff]
    desktop["iphone"] = [
        ("Claude · Apple Reminders",
         t("Atver Claude lietotni savā iPhone vai iPad un palūdz pievienot atgādinājumu “REYRUN pārbaude” jau esošā sarakstā. Kad parādās atļaujas pieprasījums, atļauj piekļuvi atgādinājumiem. Atver Apple lietotni Atgādinājumi un pārbaudi ierakstu. Atļauju vari atsaukt ierīces iestatījumos pie Claude.",
           "Open Claude on your iPhone or iPad and ask it to add a reminder called “REYRUN test” to an existing list. Allow access to Reminders when prompted. Open Apple Reminders to check the item. You can revoke access under Claude in your device settings.",
           "Откройте Claude на iPhone или iPad и попросите добавить напоминание «Проверка REYRUN» в существующий список. Разрешите доступ к напоминаниям, когда появится запрос. Откройте приложение Напоминания и проверьте запись. Доступ можно отозвать в настройках устройства для Claude."),
         [("App Store · Claude", CLAUDE), (t("Anthropic pamācība", "Anthropic’s guide", "Справка Anthropic"), CLAUDE_HELP)]),
        handoff]
    return desktop

def picker(lang):
    label = tr(lang, "Kurā ierīcē čatbotam jāstrādā?", "Which device should your chatbot work on?", "На каком устройстве должен работать чат-бот?")
    links = "".join(f'<a href="#device-{d}">{NAMES[d]}</a>' for d in DEVICES)
    return f'<p id="device-label" class="device-label">{label}</p><nav class="device-links" aria-labelledby="device-label">{links}</nav>'

def section(lang):
    heading = tr(lang, "Pieslēgšana tavai ierīcei", "Connect your device", "Подключение вашего устройства")
    out = []
    routes = guides(lang)
    for device in DEVICES:
        rows = []
        for title, description, links in routes[device]:
            buttons = "".join(f'<a href="{escape(url, quote=True)}">{escape(label)} →</a>' for label,url in links)
            rows.append(f'<div class="route-step"><h3>{escape(title)}</h3><p>{escape(description)}</p><div class="route-actions">{buttons}</div></div>')
        if device in ("windows", "mac", "linux"):
            summary = tr(lang,"Darbs ar datora failiem","Work with files on your computer","Работа с файлами компьютера")
        elif device == "android":
            summary = tr(lang,"Taimeris, faili un piezīmes","Timers, files and notes","Таймер, файлы и заметки")
        else:
            summary = tr(lang,"Atgādinājumi un piezīmes","Reminders and notes","Напоминания и заметки")
        out.append(f'<details class="device-guide" id="device-{device}"><summary><b>{NAMES[device]}</b><span>{summary}</span></summary><div class="device-steps">{"".join(rows)}</div></details>')
    return f'<section id="devices" class="content devices"><h2>{heading}</h2>{"".join(out)}</section>'
