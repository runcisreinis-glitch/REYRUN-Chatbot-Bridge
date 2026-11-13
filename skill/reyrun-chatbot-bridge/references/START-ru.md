# Инструкция для ИИ · REYRUN Мост

[Latviski](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/) · [English](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/) · [Deutsch](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/de/) · [日本語](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/) · [简体中文](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/) · [Русский](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/)

## Один файл для запуска

Если человек прислал адрес страницы, выясни, на каком устройстве нужно выполнить задачу. Сначала проверь уже разрешённое подключение. Если требуется установка, дай один готовый файл. Если опубликованный файл не подходит, подготовь один сценарий для этой системы. Человеку подскажи только ближайшее действие.

1. Проверь текущее состояние. Если задача уже выполнена, проверь результат и заверши работу. Работай в пределах предоставленного доступа.
2. Начни с основного способа. При временном сбое загрузки повтори попытку ограниченное число раз или возьми тот же выпуск из официального резервного источника. Перед запуском сверь контрольную сумму или подпись. Если в папку нельзя записывать, используй поддерживаемую установку в папку пользователя, когда это даёт нужный результат.
3. Если требуется сопряжение, выбор файла или системное разрешение, объясни, что именно нужно подтвердить, и дождись решения владельца. При отказе остановись. Передачу одного файла предложи только для задачи, которую она действительно решает.
4. Сохрани данные для восстановления. После прерывания проверь уже выполненные шаги и продолжи с первого незавершённого. Повторный запуск должен сохранить существующие настройки и резервные копии.
5. Проверь действие из чата, например прочитай заранее неизвестный файл в разрешённой папке и сверь содержимое. Сообщи результат или назови оставшееся препятствие. Учитывай загрузку, запуск, запросы системы и действия в приложении. Не обещай точное число нажатий.

## Проверка после запуска

Для Filesystem вызовите list_allowed_directories. Создайте тестовый файл в показанной папке и прочитайте его. Если содержимое отличается, остановите установку. Для Task Bridge вызовите bridge_status и read_checkpoint. Для первого save_checkpoint используйте revision 0. После обрыва связи вызовите read_checkpoint с прежним именем задания.

Если ИИ в вашем чате отказывается открыть ссылку, у него нет на это разрешения или сайт не открывается из-за технической проблемы, передайте инструкцию напрямую. Скачайте файл и прикрепите его к сообщению.

[Скачать инструкцию (.md)](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/download/REYRUN-Bridge-Instructions-ru.md)

## Инструкция для ИИ и технические сведения

## Умение (skill) для вашего чата

Если пользователь прислал только адрес этой страницы, помогите подключить чат к его компьютеру. Используйте уже доступное подключение, если оно подходит. Иначе уточните операционную систему, только если она неизвестна, и сразу дайте готовый файл или официальную ссылку на установку. Объясните, что открыть и что подтвердить. Если этот чат не поддерживает подключение, назовите совместимый чат.

[ZIP](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/download/REYRUN-Bridge-Skill-ru.zip) · [GitHub](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge)

В Windows скачайте и откройте один файл. При первом подключении к ChatGPT понадобится подтвердить устройство в браузере. Если связь уже работает, можно сразу попросить чат проверить папку.

## Готовое сообщение для чата

> Помоги подключить этот чат к моему компьютеру. Найди пять самых больших файлов в папке загрузок и покажи их размер. Ничего не удаляй. Используй умение (skill) REYRUN и скажи, когда мне нужно нажать. https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/ https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ai/ru.md

На каком устройстве должен работать чат-бот?

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-windows) · [Mac · macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-mac) · [Android](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-android) · [iPhone · iPad](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-iphone) · [Linux](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-linux)

## Подключение вашего устройства

## Windows · Работа с файлами компьютера

## ChatGPT · Desktop Commander Remote

Откройте официальный файл запуска для Windows. Подключите приложение Remote Desktop Commander в ChatGPT и войдите в аккаунт. Сверьте код устройства с кодом в терминале. Если они совпадают, подтвердите подключение и оставьте терминал открытым. Попросите чат показать подключённые устройства и прочитать одну строку из вашего тестового файла. Чтобы отключиться, нажмите Ctrl+C.

[Скачать файл запуска для Windows →](https://mcp.desktopcommander.app/remote-windows.cmd) · [Официальная инструкция →](https://desktopcommander.app/help/devices/connect-computer) · [Подключить в ChatGPT →](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

## Claude Desktop · REYRUN

Скачайте файл запуска REYRUN и откройте его на компьютере с установленным Claude Desktop. Полностью закройте и снова откройте Claude Desktop. Попросите его создать и прочитать заметку в рабочей папке.

[REYRUN · Windows →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd)

## Mac · macOS · Работа с файлами компьютера

## ChatGPT · Desktop Commander Remote

Откройте официальную инструкцию и выполните команду из раздела Mac в Терминале. Подключите приложение Remote Desktop Commander в ChatGPT и войдите в аккаунт. Сверьте код устройства с кодом в терминале. Если они совпадают, подтвердите подключение и оставьте терминал открытым. Попросите чат показать подключённые устройства и прочитать одну строку из вашего тестового файла. Чтобы отключиться, нажмите Ctrl+C.

[Официальная инструкция →](https://desktopcommander.app/help/devices/connect-computer) · [Подключить в ChatGPT →](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

## Claude Desktop · REYRUN

Скачайте файл запуска REYRUN и откройте его на компьютере с установленным Claude Desktop. Распакуйте ZIP и откройте находящийся внутри файл .command. Полностью закройте и снова откройте Claude Desktop. Попросите его создать и прочитать заметку в рабочей папке.

[REYRUN · macOS →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

## Android · Таймер, файлы и заметки

## Google Gemini · Android

Откройте Gemini на телефоне и попросите поставить таймер на пять минут. Откройте приложение «Часы» и проверьте обратный отсчёт. Если действие недоступно, проверьте в списке подключённых приложений Gemini функцию Device assistance (прежнее название — Utilities).

[Google Play · Gemini →](https://play.google.com/store/apps/details?id=com.google.android.apps.bard) · [Справка Google →](https://support.google.com/gemini/answer/15235441)

## ChatGPT · Desktop Commander Remote

Для работы с файлами Android разработчик описывает экспериментальное подключение через Termux. После подключения спросите в чате, сколько на телефоне свободного места. Доступ ограничен правами Termux. Android может прервать соединение, когда приложение работает в фоновом режиме.

[Инструкция разработчика для Android →](https://desktopcommander.app/help/devices/connect-android-phone)

## С другим веб-чатом

Попросите чат-бота подготовить заметку или черновик письма. Проверьте текст на телефоне и выберите, сохранить файл или открыть черновик в почтовом приложении. Отправку подтверждаете вы.

[Подготовить заметку или письмо →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/phone/) · [Проверить контрольную сумму файла →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

## iPhone · iPad · Напоминания и заметки

## Claude · Apple Reminders

Откройте Claude на iPhone или iPad и попросите добавить напоминание «Проверка REYRUN» в существующий список. Разрешите доступ к напоминаниям, когда появится запрос. Откройте приложение «Напоминания» и проверьте запись. Доступ можно отозвать в настройках устройства для Claude.

[App Store · Claude →](https://apps.apple.com/app/id6473753684) · [Справка Anthropic →](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)

## С другим веб-чатом

Попросите чат-бота подготовить заметку или черновик письма. Проверьте текст на телефоне и выберите, сохранить файл или открыть черновик в почтовом приложении. Отправку подтверждаете вы.

[Подготовить заметку или письмо →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/phone/) · [Проверить контрольную сумму файла →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

## Linux · Работа с файлами компьютера

## ChatGPT · Desktop Commander Remote

Откройте официальную инструкцию и выполните в терминале команду установки для Linux. Подключите приложение Remote Desktop Commander в ChatGPT и войдите в аккаунт. Сверьте код устройства с кодом в терминале. Если они совпадают, подтвердите подключение и оставьте терминал открытым. Попросите чат показать подключённые устройства и прочитать одну строку из вашего тестового файла. Чтобы отключиться, нажмите Ctrl+C.

[Официальная инструкция →](https://desktopcommander.app/help/devices/connect-computer) · [Подключить в ChatGPT →](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

## Если вы пользуетесь Claude Desktop

Если вы пользуетесь Claude Desktop, файл для Windows или Mac подключит к нему одну рабочую папку REYRUN. После этого полностью закройте и снова откройте Claude Desktop. На Mac откройте файл .command из архива. При первом запуске система может запросить подтверждение.

[Скачать для Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [Скачать для Mac](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) · [Инструкция для ИИ (.zip)](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/download/REYRUN-Bridge-Skill-ru.zip)

## Пользуетесь ChatGPT в браузере?

[Запуск для ChatGPT на Windows](https://mcp.desktopcommander.app/remote-windows.cmd) · [Установка на Mac и Linux](https://desktopcommander.app/help/devices/connect-computer) · [Открыть подключение в ChatGPT](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

Подключите компьютер с Windows, macOS или Linux по инструкции Desktop Commander. Когда в терминале появится «Device ready», ChatGPT сможет работать с файлами этого компьютера, даже если вы открыли чат на телефоне. Для действий на самом телефоне выберите выше Android или iPhone.

[Desktop Commander](https://desktopcommander.app/help/devices/connect-computer) · [Бесплатный план](https://desktopcommander.app/help/account-billing/plans-and-tool-call-limits)

## Установите латышский перевод RDR2

Для сюжетного режима в Windows. Если в игре уже стоят проверенные сборки Universal RDR2 String Translator и Ultimate ASI Loader x64 9.7.4, закройте игру, скачайте и откройте установщик XML. Он сверит контрольные суммы обоих файлов, сохранит прежний латышский XML и установит проверенный перевод. Если в папке есть другой основной перевод или не хватает плагина, установщик остановится и покажет ссылку на инструкцию.

[Установить латышский XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Install-XML.cmd) · [Восстановить прежний XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Restore-XML.cmd)

Скачайте и откройте файл запуска для Windows. Он ищет игру в библиотеках Steam, Rockstar и Epic и подготавливает проверенный файл латышского перевода в рабочей папке. Если найдётся несколько папок, выберите нужную. Передайте ИИ инструкцию. В ней описано, как установить плагин и загрузчик, сделать резервную копию и проверить перевод в сюжетном режиме.

[Скачать файл запуска для RDR2](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-rdr2-Windows.cmd) · [Открыть инструкцию по переводу](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/ru/install/)

## Другие способы подключения и результаты проверок

Выберите устройство и откройте описание инструмента. Там указано, для чего он подходит, что удалось проверить и где найти документацию.

## 01. Filesystem MCP · 2.3.0

Файлы в рабочей папке · Windows · macOS · GitHub ★ 91 934

ИИ может навести порядок в выбранной папке и сделать точные копии файлов.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

Проверка · В Linux мы проверили сервер версии 2.3.0. Он показал разрешённые папки, прочитал сведения о файле, точно скопировал двоичные данные и отказал в доступе за пределами выбранных папок. На физическом ПК с Windows и установленным Node чистая установка заняла 6,68 секунды. Прочитанный текст на латышском языке совпал с записанным. Сервер отклонил запрос к файлу за пределами рабочей папки.

Наблюдения за 2026 год · В марте пользователь сообщил, что клиент заменил заданный список папок своим. В этом варианте используется --confine-roots и проверяется фактический список.

Параллельная работа · Пусть файлы в каждой папке изменяет только один чат. Разным папкам можно дать отдельные подключения.

Для сеанса чтения добавьте --read-only. Проверьте, существует ли файл назначения. Команда copy_file откажется его перезаписывать. Обычный веб-чат без локального подключения может вести пользователя по шагам.

[Filesystem MCP · инструменты и правила доступа к папкам](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md)

[Выпуск Filesystem 2.3.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0)

[Настройка приложения для Windows и macOS](https://modelcontextprotocol.io/docs/develop/connect-local-servers)

[Отзыв о доступе к корневым папкам, 16 марта 2026 года](https://github.com/modelcontextprotocol/servers/issues/3602)

[GitHub · modelcontextprotocol/servers](https://api.github.com/repos/modelcontextprotocol/servers)

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/windows-filesystem.json)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 02. REYRUN Task Bridge · 1.0.0

Записи задач · Windows · macOS

Сохраните, на чём остановились, чтобы другой чат мог продолжить работу. У каждого задания своя история версий.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-macOS.command.zip)

Проверка · Компьютер с Windows, Node 24.19, 01:11 по Риге. Два запуска настроили подключение в тестовых папках с пробелами в названиях. Исходная настройка сохранилась. Один клиентский процесс записал первую версию, другой её прочитал. Попытка записи поверх устаревшей версии была отклонена. Четыре локальных клиента одновременно сохранили четыре разные задачи. Когда все четверо попытались изменить одну запись, сохранилось одно изменение. После перезапуска были доступны все пять задач.

Наблюдения за 2026 год · Проверка команды проекта 12 ноября по рижскому времени.

Параллельная работа · Проверены четыре параллельных клиента и восстановление пяти задач.

Профиль сохраняет записи заданий. Для копирования файлов выберите Filesystem.

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

[4 × stdio](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/parallel.json)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 03. Microsoft Playwright MCP · 0.0.85

Отдельный браузер · Windows · macOS · GitHub ★ 39 515

Подходит для проверки собственного сайта: найти кнопку, перейти на следующую страницу, проверить читаемость. Каждой задаче можно дать отдельный профиль браузера.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-macOS.command.zip)

Проверка · На Windows и macOS наш файл запуска открыл отдельный процесс Chrome и передал снимок экрана клиенту чата. Мы открыли пустую страницу и убедились, что полученное изображение PNG читается.

Наблюдения за 2026 год · В японском практическом разборе автор отдельно проверил процессы браузера и состояние входа. Для параллельных задач он рекомендует явно выбирать изолированный профиль.

Параллельная работа · Каждому параллельному сеансу нужны свой процесс и профиль. В нашем тесте открывался один на каждую ОС.

Новый профиль не содержит личных сеансов входа. В стандартном наборе есть выполнение кода. Авторы указывают, что --allowed-origins не гарантирует полной сетевой изоляции. Используйте доверенный тестовый сайт и ограничения инструментов клиента.

[Выпуск Microsoft · 9 ноября 2026 года](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.85)

[Microsoft · профили и параметры браузера](https://github.com/microsoft/playwright-mcp)

[Проверки автора в Windows, macOS и Ubuntu · 11 ноября](https://github.com/microsoft/playwright-mcp/actions/runs/43074928448)

[Автор сравнивает профили (на японском) · 29 июня 2026 года](https://zenn.dev/ruri/articles/playwright-multi-session-isolation)

[GitHub · microsoft/playwright-mcp](https://api.github.com/repos/microsoft/playwright-mcp)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 04. Chrome DevTools MCP · 1.13.0

Отдельный браузер · Windows · macOS · GitHub ★ 55 113

Удобен для визуальной проверки. Ограниченный набор инструментов открывает разрешённую страницу проекта и делает снимок экрана.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-macOS.command.zip)

Проверка · На Windows и macOS наш файл запуска открыл отдельный процесс Chrome и передал снимок экрана клиенту чата. Мы открыли пустую страницу и убедились, что полученное изображение PNG читается.

Наблюдения за 2026 год · Пользователь macOS сообщил, что после аварийного завершения сервера мог остаться тестовый процесс Chrome. Китайский автор отдельно опубликовал результаты проверки в Debian и перечислил непроверенные режимы.

Параллельная работа · В каждом сеансе свой процесс Chrome. В общем профиле вкладки могут смешиваться.

Профиль временный. Для подключения к личной открытой вкладке нужен другой режим. Снимок может содержать частные данные, которые показывает сама тестовая страница. Завершайте сеанс через клиент.

[Выпуск Chrome DevTools · 11 ноября 2026 года](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0)

[Chrome DevTools MCP · настройки](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md)

[Проверки разработчиков в Windows, macOS и Ubuntu · 11 ноября](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43058501937)

[Сообщение о внезапном завершении работы в macOS · 26 августа 2026 года](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/2621)

[Записи о проверке на китайском языке · 21 октября 2026 года](https://friendlyai.top/projects/chrome-devtools-mcp/)

[Более поздняя проверка перед выпуском · ошибка в macOS с Node 22](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43105363963)

[GitHub · ChromeDevTools/chrome-devtools-mcp](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 05. Desktop Commander · Remote / Local

Просмотр файлов · Windows · macOS · GitHub ★ 10 284

Работает с файлами и сеансами терминала в фоновом режиме. Наш локальный файл запуска открывает три инструмента для просмотра одной рабочей папки.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-macOS.command.zip)

Проверка · На компьютере с Windows была версия 0.3.0. Desktop Commander прочитал файл, созданный через Reinis Bridge, и записал в него другой текст. Reinis Bridge прочитал все 22 байта. Так можно передать сведения о выполненной работе. История чатов при этом не переносится. Официальный набор удалённых инструментов позволяет работать с файлами, терминалом и сеансами процессов. При проверке файлов мы не использовали мышь и клавиатуру. Разработчик указывает поддержку Windows, macOS и Linux. Здесь проверен реальный компьютер с Windows.

Наблюдения за 2026 год · 13 октября 2026 года пользователь Windows с версией 0.2.52 сообщил, что start_process выводит окна консоли на передний план. 3 ноября другой пользователь с версией 0.3.1 сообщил о периодических тайм-аутах примерно через 60 секунд, хотя устройство отображалось в сети. Это отдельные случаи. В нашем тесте обмен файлами прошёл успешно.

Параллельная работа · Проверена передача файла между двумя инструментами. Мы не проверяли, сколько чатов можно подключить к одному устройству одновременно.

Файл запуска использует локальный пакет 0.3.2. Remote 0.3.0 — отдельный сервис с привязкой. Элементы интерфейса проверяйте в профиле браузера.

[Локальная версия](https://github.com/wonderwhy-er/DesktopCommanderMCP)

[Удалённая версия](https://github.com/desktop-commander/remote-desktop-commander)

[Справка](https://desktopcommander.app/help/getting-started/what-is-desktop-commander)

[Сообщение об окнах консоли](https://github.com/wonderwhy-er/DesktopCommanderMCP/issues/852)

[Сообщение о тайм-аутах подключения](https://github.com/desktop-commander/remote-desktop-commander/issues/90)

## 06. Reinis Bridge · 1.0.0

Личный рабочий стол · Windows

Репозиторий проекта на GitHub создали в отдельном приватном окне Chrome через OpenBot. После проверки приложение закрылось. Локальный отчёт подтвердил, что пользовательский рабочий стол, принимающий ввод, остался прежним.

Проверка · 12 ноября в 00:58 по рижскому времени через действующий мост запустили две короткие фоновые задачи. Они выполнялись одновременно в течение 5,011 секунды. При повторном запросе с прежним ключом мост вернул уже выполненную задачу. Чтение вывода можно продолжить с сохранённой позиции.

Наблюдения за 2026 год · По опыту Рейниса доступен один интерактивный поток. В нашем тесте одновременно работали две фоновые задачи терминала. Управление рабочим столом из двух разных чатов одновременно мы не проверяли.

Параллельная работа · Один интерактивный рабочий стол. Два фоновых задания выполнялись одновременно 5,011 секунды.

Это личный мост Рейниса для Windows. Программа запуска в этом проекте создаёт отдельное локальное подключение к выбранной вами папке. Она не устанавливает личный мост Рейниса и не даёт доступа к его компьютеру.

[REYRUN · Windows](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

## 07. Git worktree + bundle · Git CLI · проверена версия 2.52.0

Передача работы · Windows · macOS · GitHub ★ 64 269

Для передачи проектных файлов между сеансами без постоянного подключения. Каждая задача получает отдельную рабочую копию и ветку. Пакет переносит сохранённые в Git изменения на другой компьютер.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-macOS.command.zip)

Проверка · В Linux создали две рабочие копии. Изменение в первой не затронуло вторую. Проверенный пакет восстановил тот же коммит и точную копию файла.

Наблюдения за 2026 год · В немецком практическом опыте две задачи проверили в отдельных папках. Авторы воспроизвели действия исполнителей контролируемыми изменениями файлов.

Параллельная работа · Проверены две рабочие копии, каждая в своей ветке.

Рабочие копии используют общую базу объектов Git. Полный пакет ветки может включать её историю. Для передачи создайте отдельный репозиторий только с выбранными файлами. Этот способ не даёт управления устройством, приложениями или мышью.

[Руководство по git worktree](https://git-scm.com/docs/git-worktree)

[Руководство по git bundle](https://git-scm.com/docs/git-bundle)

[Скачать Git для компьютера](https://git-scm.com/downloads)

[Эксперимент с двумя ролями (на немецком) · 9 сентября 2026 года](https://www.bitblokes.de/ki-agenten-git-worktrees/)

[GitHub · git/git](https://api.github.com/repos/git/git)

## 08. REYRUN · Web Crypto

Передача файлов · Windows · macOS · Android · iOS

Откройте готовый скрипт в браузере и одним касанием проверьте пример либо выберите текстовый файл.

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

Проверка · На эмуляторе Android 15 одно касание обработало опубликованный пример без изменений. WebView 124.0.6367.219 вернул 13 байт, две строки и ожидаемую контрольную сумму SHA-256. В предварительном просмотре Chrome получили тот же результат. В симуляторе iPhone SE с iOS 18.5 и WebKit кнопка примера дала тот же результат. Неподдерживаемое действие было отклонено. Испытания прошли на виртуальных устройствах.

Наблюдения за 2026 год · Независимых отзывов о новой демонстрации пока нет.

Параллельная работа · Для каждого задания сохраняется отдельный файл или отчёт. Из меню «Поделиться» на телефоне можно отправлять их по одному.

Отчёт относится к одному файлу. Чтобы чат объяснил ошибку, отдельно приложите нужный фрагмент текста.

[REYRUN](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/web/start)

[MDN · File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API)

[MDN · SubtleCrypto.digest](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest)

[Android 15 · WebView · 2026-11-11](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121791094/job/130863821353)

[iPhone SE · iOS 18.5 · WebKit](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121668999/job/130863410709)

## 09. LocalSend

Передача файлов · Windows · macOS · Android · iOS

Перешлите готовый файл на другое устройство в своей сети Wi-Fi.

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

Проверка · Передача между двумя устройствами здесь не проверялась. Передайте mobile-request.json и сверьте идентификатор и контрольную сумму с результатом проверки на этой странице.

Наблюдения за 2026 год · 25 июня 2026 года xueyexiao на китайском описал, как на Redmi K70 передал файл через меню файлового менеджера, когда у LocalSend не было разрешения на доступ к файлу.

Параллельная работа · Для каждого задания сохраняется отдельный файл или отчёт. Из меню «Поделиться» на телефоне можно отправлять их по одному.

Нужны два соединённых устройства с LocalSend. Выберите файл и получателя.

[LocalSend](https://localsend.org/download)

[Список изменений за 2026 год](https://localsend.org/changelog)

[xueyexiao · Redmi K70 · 中文](https://github.com/localsend/localsend/discussions/835)

[REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 10. Nextcloud Files

Передача файлов · Windows · macOS · Android · iOS

Сохраните подготовленный чатом файл в папке Nextcloud и продолжите работу с ним на компьютере.

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

Проверка · В этой сессии частный сервер не подключали. Проверьте ID и хеш файла, полученного на втором устройстве.

Наблюдения за 2026 год · 28 апреля 2026 года Sanook на немецком описал загрузку фотографии с Android, которая долго ждала в очереди и затем завершилась. В отчёте речь шла о фотографии. Наш тест проводился с другим файлом.

Параллельная работа · Для каждого задания сохраняется отдельный файл или отчёт. Из меню «Поделиться» на телефоне можно отправлять их по одному.

Выбирайте, если у вас уже есть учётная запись и папка. Создание сервера — отдельная задача.

[Nextcloud](https://nextcloud.com/install/)

[iOS · 2026](https://github.com/nextcloud/ios/issues)

[Sanook · Android · Deutsch](https://help.nextcloud.com/t/android-client-warte-auf-hochladen/217584/18)

[REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 11. Termux

Локальный скрипт · Android

Проверьте готовый скрипт в закрытой папке Termux на Android.

[Готовый скрипт для Termux](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-termux.sh)

Проверка · Дважды запущен через sh в Linux. Созданы две отдельные папки и два отчёта с ожидаемой контрольной суммой. Запуск на Android здесь не проверялся.

Наблюдения за 2026 год · 30 апреля 2026 года slondr сообщил о зависании выбора файла на Pixel 9a с Android 16. В той же ветке разработчик сообщил об успешной проверке на двух Samsung.

Параллельная работа · Для каждого задания сохраняется отдельный файл или отчёт. Из меню «Поделиться» на телефоне можно отправлять их по одному.

Используйте при уже установленном Termux. Для обычного чата самый простой старт — веб-пример.

[Termux](https://github.com/termux/termux-app)

[Android 15 · #5150](https://github.com/termux/termux-app/issues/5150)

[Termux · установка](https://github.com/termux/termux-app#installation)

[Termux:API](https://github.com/termux/termux-api)

[slondr · Pixel 9a · English](https://github.com/termux/termux-app/issues/5101)

## 12. Apple Shortcuts

Передача файлов · iOS · macOS

Передайте файл уже настроенной команде Apple через меню «Поделиться».

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

Проверка · Эта последовательность здесь не проверялась на физическом iPhone. Откройте phone-test.txt в «Файлах» и убедитесь, что он содержит REYRUN-OK.

Наблюдения за 2026 год · 28 января 2026 года японский автор anyprogram описал команду для создания и сохранения TXT на iPhone и iPad. В режиме редактирования она перезаписывает выбранный файл.

Параллельная работа · Для каждого задания сохраняется отдельный файл или отчёт. Из меню «Поделиться» на телефоне можно отправлять их по одному.

Нужна ранее добавленная команда, принимающая файлы. Веб-пример можно попробовать сразу.

[Apple · iPhone](https://support.apple.com/guide/shortcuts/launch-a-shortcut-from-another-app-apd163eb9f95/ios)

[Apple · Share](https://support.apple.com/guide/shortcuts/share-shortcuts-apdf01f8c054/ios)

[Apple · руководство по приложению «Команды»](https://support.apple.com/guide/shortcuts/welcome/ios)

[anyprogram · iPhone/iPad · 日本語](https://qiita.com/anyprogram/items/6cc1394569c687ed506c)

[iPhone 16 Pro Max · 2026](https://github.com/net00-1/SW-DLT/issues/133)

[REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 13. Desktop Commander Remote · ChatGPT

Подключённое приложение · Windows · macOS · Linux

Работайте с файлами подключённого компьютера из веб-чата.

[Открыть инструкцию](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#devices)

Проверка · Разработчик описывает Windows, macOS и Linux.

Наблюдения за 2026 год · Документация разработчика.

Параллельная работа · Число одновременных сеансов для этого варианта не измерялось.

Подключение должно работать на целевом компьютере.

[Desktop Commander Remote · ChatGPT](https://desktopcommander.app/help/devices/connect-computer)

## 14. Google Gemini · Device assistance

Подключённое приложение · Android

Попросите Gemini поставить таймер в приложении «Часы».

[Открыть инструкцию](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-android)

Проверка · Google описывает действие в приложении Gemini для Android.

Наблюдения за 2026 год · Документация разработчика.

Параллельная работа · Число одновременных сеансов для этого варианта не измерялось.

Требуется приложение Gemini для Android.

[Google Gemini · помощь в работе с устройством](https://support.google.com/gemini/answer/15235441)

## 15. Claude · Apple Reminders

Подключённое приложение · iOS

Добавьте напоминание в существующий список на iPhone или iPad.

[Открыть инструкцию](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-iphone)

Проверка · Anthropic описывает создание напоминаний с разрешения пользователя.

Наблюдения за 2026 год · Документация разработчика.

Параллельная работа · Число одновременных сеансов для этого варианта не измерялось.

Нужны мобильное приложение Claude и доступ к напоминаниям.

[Claude · Apple Reminders](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)

## Когда работу продолжает другой чат

## Как четырём чатам работать одновременно?

Выделите каждому чату имя задачи и отдельную папку. Текст, сравнение и проверку файлов можно разделить. Изменения в папке игры поручите одному чату. Каждой сессии браузера нужен свой профиль. На общем рабочем столе мышью управляет одна сессия.

## Что делать, если связь прервалась?

Назовите новому чату прежнюю задачу. Попросите прочитать последнюю запись и проверить, какие файлы уже готовы. Если скачивание или копирование прервалось, сначала проверьте сам файл. Если два чата одновременно изменили одну запись, прочитайте сохранённую версию перед следующей правкой.

## Что чат-бот сможет делать на моём компьютере?

Файловый мост открывает одну рабочую папку REYRUN. Игровой вариант добавляет выбранную папку RDR2. Для веб-примера достаточно одного выбранного файла. Система может запросить разрешение на открытие загрузки. При неожиданном запросе можно воспользоваться примером в браузере.

## Как разобраться в ошибке программы?

Положите копию журнала ошибок программы в рабочую папку REYRUN. Попросите ИИ прочитать и объяснить последнюю ошибку. В обычный веб-чат приложите только нужный фрагмент. Веб-пример сообщает контрольную сумму и число строк. Сам текст остаётся на устройстве.

[Инструкция для ИИ](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ai/ru.md) · [Проверки и источники](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/research)

## Где клиент читает настройки подключения?

На Windows готовый файл запуска ищет существующий профиль Claude Desktop в %APPDATA%/Claude, на Mac — в ~/Library/Application Support/Claude. В claude_desktop_config.json добавляется выбранная запись reyrun-… и создаётся копия прежнего файла. Если клиента нет, START.txt укажет веб-пример. Для другого клиента с локальным MCP используйте сгенерированный runtime/reyrun-…-client.json. В нём указан путь к исполняемому файлу именно на этом компьютере.

## Пример передачи задачи

Сохраните последний проверенный результат и один следующий шаг. Новый чат с тем же локальным профилем может вызвать read_checkpoint с прежним job. В обычный веб-чат вставьте запись и приложите нужный файл. Управление окном игры и запросами разрешений оставьте одной сессии.

```json
{
  "name": "save_checkpoint",
  "arguments": {
    "job": "game-check",
    "revision": 0,
    "done": "Тестовый файл прочитан без изменений.",
    "next": "Проверь выбранную папку игры."
  }
}
```
