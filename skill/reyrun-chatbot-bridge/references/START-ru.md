# Инструкция для ИИ · REYRUN Мост

[Latviski](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/) · [English](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/) · [Русский](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/)

[Скачать для Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [Скачать для Mac](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) · [Попробовать на телефоне или в браузере](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=ru)

Скачайте и откройте файл. Он подключит рабочую папку к уже установленному Claude Desktop. Полностью закройте и снова откройте приложение, когда вам удобно. Для обычного веб-чата откройте пример в браузере. На Mac откройте файл .command из архива. При первом запуске система может запросить подтверждение.

## Проверка после запуска

Для Filesystem вызовите list_allowed_directories. Создайте тестовый файл в показанной папке и прочитайте его. Если содержимое отличается, остановите установку. Для Task Bridge вызовите bridge_status и read_checkpoint. Для первого save_checkpoint используйте revision 0. После обрыва связи вызовите read_checkpoint с прежним именем задания.

## 1. Filesystem MCP · 2.3.0

Windows, macOS. Подходит для файлов в выбранной рабочей папке. Помощник может упорядочить проект и скопировать файлы без изменения их содержимого.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

**Проверка.** В Linux запущен настоящий сервер 2.3.0. Он показал разрешённые папки, прочитал сведения о файле, точно скопировал двоичные данные и отказал в доступе за пределами выбранных папок. На физическом ПК с Windows и установленным Node чистая установка заняла 6,68 секунды. Запись и чтение текста с диакритикой совпали, запрос вне рабочей папки был отклонён.

**Опыт за 2026 год.** В марте пользователь сообщил, что клиент заменил заданный список папок своим. В этом варианте используется --confine-roots и проверяется фактический список.

Для сеанса чтения добавьте --read-only. Проверьте, существует ли файл назначения. Команда copy_file откажется его перезаписывать. Обычный веб-чат без локального подключения может вести пользователя по шагам.

[Filesystem MCP · tools and directory rules](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md) · [Filesystem 2.3.0 release](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) · [Desktop client setup for Windows and macOS](https://modelcontextprotocol.io/docs/develop/connect-local-servers) · [User report on effective roots, 16 March 2026](https://github.com/modelcontextprotocol/servers/issues/3602) · [GitHub · modelcontextprotocol/servers](https://api.github.com/repos/modelcontextprotocol/servers) · [Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/windows-filesystem.json)

## 2. REYRUN Task Bridge · 1.0.0

Windows, macOS. Передайте следующему чату точную точку остановки. У каждого задания своя история версий.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-macOS.command.zip)

**Проверка.** Компьютер с Windows, Node 24.19, 01:11 по Риге. Два запуска настроили подключение в тестовых папках с пробелами в названиях. Исходная настройка сохранилась. Один клиентский процесс записал первую версию, другой её прочитал. Попытка записи поверх устаревшей версии была отклонена. Четыре локальных клиента одновременно сохранили четыре разные задачи. При общей записи сработала одна из четырёх попыток. После перезапуска были доступны все пять задач.

**Опыт за 2026 год.** Собственное испытание проекта 12 ноября по Риге.

Профиль сохраняет записи заданий. Для копирования файлов выберите Filesystem.

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json) · [4 × stdio](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/parallel.json)

## 3. Microsoft Playwright MCP · 0.0.85

Windows, macOS. Подходит для проверки собственного сайта: найти кнопку, перейти на следующую страницу, проверить читаемость. Каждой задаче можно дать отдельный профиль браузера.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-macOS.command.zip)

**Проверка.** В Linux проверены подключение MCP и список инструментов. Среда запретила Chromium создать сокет, поэтому локальный тест не подтвердил отображение страницы. 11 ноября проверки Microsoft прошли в Windows и macOS.

**Опыт за 2026 год.** В японском практическом разборе автор отдельно проверил процессы браузера и состояние входа. Для параллельных задач он рекомендует явно выбирать изолированный профиль.

Новый профиль не содержит личных сеансов входа. В стандартном наборе есть выполнение кода. Авторы указывают, что --allowed-origins не гарантирует полной сетевой изоляции. Используйте доверенный тестовый сайт и ограничения инструментов клиента.

[Microsoft release · 9 November 2026](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.85) · [Microsoft · browser profiles and documented options](https://github.com/microsoft/playwright-mcp) · [Author tests on Windows, macOS and Ubuntu · 11 November](https://github.com/microsoft/playwright-mcp/actions/runs/43074928448) · [Japanese first-person profile comparison · 29 June 2026](https://zenn.dev/ruri/articles/playwright-multi-session-isolation) · [GitHub · microsoft/playwright-mcp](https://api.github.com/repos/microsoft/playwright-mcp)

## 4. Chrome DevTools MCP · 1.13.0

Windows, macOS. Удобен для визуальной проверки. Ограниченный набор инструментов открывает разрешённую страницу проекта и делает снимок экрана.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-macOS.command.zip)

**Проверка.** В Linux установлено соединение с 1.13.0. При указанных ограничениях сервер предоставил ровно два инструмента: navigate и screenshot. В нашей среде браузер не запустился. По ссылке приведён успешный прогон авторов в Windows и macOS за ту же дату. В более позднем предрелизном прогоне в тот же день проверка macOS с Node 22 не прошла.

**Опыт за 2026 год.** Пользователь macOS сообщил, что после аварийного завершения сервера мог остаться тестовый процесс Chrome. Китайский автор отдельно опубликовал результаты проверки в Debian и перечислил непроверенные режимы.

Профиль временный. Для подключения к личной открытой вкладке нужен другой режим. Снимок может содержать частные данные, которые показывает сама тестовая страница. Завершайте сеанс через клиент.

[Chrome DevTools release · 11 November 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0) · [Chrome DevTools MCP · configuration](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md) · [Upstream Windows/macOS/Ubuntu test matrix · 11 November](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43058501937) · [macOS report about abrupt termination · 26 August 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/2621) · [Chinese practitioner’s test log · 21 October 2026](https://friendlyai.top/projects/chrome-devtools-mcp/) · [Later upstream pre-release run · macOS/Node 22 failure](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43105363963) · [GitHub · ChromeDevTools/chrome-devtools-mcp](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp)

## 5. Desktop Commander · Remote / Local

Windows, macOS. Работает с файлами и сеансами терминала в фоне. Наш локальный файл запуска открывает три инструмента для просмотра одной рабочей папки.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-macOS.command.zip)

**Проверка.** На компьютере с Windows была версия 0.3.0. Desktop Commander прочитал файл, созданный через Reinis Bridge, и записал в него другой текст. Reinis Bridge прочитал все 22 байта. Так можно передать сведения о выполненной работе. История чатов при этом не переносится. Официальный набор удалённых инструментов позволяет работать с файлами, терминалом и сеансами процессов. При проверке файлов мы не использовали мышь и клавиатуру. Разработчик указывает поддержку Windows, macOS и Linux. Здесь проверен реальный компьютер с Windows.

**Опыт за 2026 год.** 13 октября 2026 года пользователь Windows с версией 0.2.52 сообщил, что start_process выводит окна консоли на передний план. 3 ноября другой пользователь с версией 0.3.1 сообщил о периодических тайм-аутах примерно через 60 секунд, хотя устройство отображалось в сети. Это отдельные случаи. В нашем тесте обмен файлами прошёл успешно.

Файл запуска использует локальный пакет 0.3.2. Remote 0.3.0 — отдельный сервис с привязкой. Элементы интерфейса проверяйте в профиле браузера.

[local](https://github.com/wonderwhy-er/DesktopCommanderMCP) · [remote](https://github.com/desktop-commander/remote-desktop-commander) · [help](https://desktopcommander.app/help/getting-started/what-is-desktop-commander) · [reportFocus](https://github.com/wonderwhy-er/DesktopCommanderMCP/issues/852) · [reportTimeout](https://github.com/desktop-commander/remote-desktop-commander/issues/90)

## 6. Reinis Bridge · 1.0.0

Windows. Репозиторий проекта на GitHub создали в отдельном приватном окне Chrome через OpenBot. После проверки приложение закрылось. Локальный отчёт подтвердил, что пользовательский рабочий стол, принимающий ввод, остался прежним.



**Проверка.** 12 ноября в 00:58 по рижскому времени через действующий мост запустили две короткие фоновые задачи. Они выполнялись одновременно в течение 5,011 секунды. При повторном запросе с прежним ключом мост вернул уже выполненную задачу. Чтение вывода можно продолжить с сохранённой позиции.

**Опыт за 2026 год.** По опыту Рейниса доступен один интерактивный поток. В нашем тесте одновременно работали две фоновые задачи терминала. Управление рабочим столом из двух разных чатов одновременно мы не проверяли.

Это личный мост Рейниса для Windows. Программа запуска в этом проекте создаёт отдельное локальное подключение к выбранной вами папке. Она не устанавливает личный мост Рейниса и не даёт доступа к его компьютеру.

[REYRUN · Windows](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

## 7. Git worktree + bundle · Git CLI · tested 2.52.0

Windows, macOS. Для передачи проектных файлов между сеансами без постоянного подключения. Каждая задача получает отдельную рабочую копию и ветку. Пакет переносит сохранённые в Git изменения на другой компьютер.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-macOS.command.zip)

**Проверка.** В Linux создали две рабочие копии. Изменение в первой не затронуло вторую. Проверенный пакет восстановил тот же коммит и точную копию файла.

**Опыт за 2026 год.** В немецком практическом опыте две задачи проверили в отдельных папках. Авторы воспроизвели действия исполнителей контролируемыми изменениями файлов.

Рабочие копии используют общую базу объектов Git. Полный пакет ветки может включать её историю. Для передачи создайте отдельный репозиторий только с выбранными файлами. Этот способ не даёт управления устройством, приложениями или мышью.

[Git worktree manual](https://git-scm.com/docs/git-worktree) · [Git bundle manual](https://git-scm.com/docs/git-bundle) · [Git desktop downloads](https://git-scm.com/downloads) · [German practical two-role experiment · 9 September 2026](https://www.bitblokes.de/ki-agenten-git-worktrees/) · [GitHub · git/git](https://api.github.com/repos/git/git)

## 8. REYRUN · Web Crypto

Windows, macOS, Android, iOS. Откройте готовый скрипт в браузере и одним касанием проверьте пример либо выберите текстовый файл.

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=ru)

**Проверка.** В примере «REYRUN» и «Rīga» 13 байт и две строки. Результат содержит контрольную сумму SHA-256.

**Опыт за 2026 год.** Собственная проверка REYRUN, ноябрь 2026 года.

Это квитанция для одного файла. Чтобы чат объяснил ошибку, отдельно приложите нужный фрагмент текста.

[REYRUN](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/web/start)

## 9. LocalSend

Windows, macOS, Android, iOS. Перешлите готовый файл на другое устройство в своей сети Wi-Fi.

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=ru)

**Проверка.** Проект выпускает приложения для всех четырёх платформ. Версия 1.18.2 вышла 21 августа 2026 года.

**Опыт за 2026 год.** В августе разработчики добавили на Android фоновую передачу и проверку контрольной суммы.

Нужны два соединённых устройства с LocalSend. Выберите файл и получателя.

[LocalSend](https://localsend.org/download) · [2026 · Changelog](https://localsend.org/changelog)

## 10. Nextcloud Files

Windows, macOS, Android, iOS. Сохраните подготовленный чатом файл в папке Nextcloud и продолжите работу с ним на компьютере.

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=ru)

**Проверка.** Официальные приложения передают файлы через уже подключённую учётную запись Nextcloud.

**Опыт за 2026 год.** Пользователи iOS описали загрузки без видимого прогресса. Проверьте полученный файл на втором устройстве, прежде чем продолжать.

Выбирайте, если у вас уже есть учётная запись и папка. Создание сервера — отдельная задача.

[Nextcloud](https://nextcloud.com/install/) · [iOS · 2026](https://github.com/nextcloud/ios/issues)

## 11. Termux

Android. Проверьте готовый скрипт в закрытой папке Termux на Android.

[Готовый скрипт для Termux](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-termux.sh)

**Проверка.** Скрипт работает без сети, создаёт образец и печатает контрольную сумму. Проверено выполнение в POSIX-оболочке.

**Опыт за 2026 год.** В июне пользователь Android 15 сообщил об остановке длительных фоновых процессов. Короткий пример сразу сохраняет квитанцию.

Используйте при уже установленном Termux. Для обычного чата самый простой старт — веб-пример.

[Termux](https://github.com/termux/termux-app) · [Android 15 · #5150](https://github.com/termux/termux-app/issues/5150)

## 12. Apple Shortcuts

iOS, macOS. Передайте файл уже настроенной команде Apple через меню «Поделиться».

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=ru)

**Проверка.** Apple документирует получение файлов из другого приложения iPhone. Веб-пример предложит поделиться квитанцией, если устройство это поддерживает.

**Опыт за 2026 год.** Руководство Apple для iOS 26 указывает, что появление команды в меню зависит от поддерживаемого типа данных.

Нужна ранее добавленная команда, принимающая файлы. Веб-пример можно попробовать сразу.

[Apple · iPhone](https://support.apple.com/guide/shortcuts/launch-a-shortcut-from-another-app-apd163eb9f95/ios) · [Apple · Share](https://support.apple.com/guide/shortcuts/share-shortcuts-apdf01f8c054/ios)

## Установите латышский перевод RDR2

Скачайте и откройте файл запуска для Windows. Он ищет игру в библиотеках Steam, Rockstar и Epic и подготавливает проверенный файл латышского перевода в рабочей папке. Если найдётся несколько папок, вы выбираете нужную. Передайте ИИ инструкцию по установке плагина, загрузчика, резервному копированию и проверке в сюжетном режиме. [Открыть инструкцию по переводу](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/install/)

## Как четырём чатам работать одновременно?

Выделите каждому чату имя задачи и отдельную папку. Текст, сравнение и проверку файлов можно разделить. Изменения в папке игры поручите одному чату. Каждой сессии браузера нужен свой профиль. На общем рабочем столе мышью управляет одна сессия.

## Что делать при обрыве связи?

Назовите новому чату то же имя задачи. Попросите прочитать последнюю запись и проверить созданные файлы. После тайм-аута сначала проверьте прежнее задание. Повторяйте скачивание или копирование только после проверки результата. При конфликте версий сначала прочитайте сохранённую запись.

## Что чат-бот сможет делать на моём компьютере?

Файловый мост открывает одну рабочую папку REYRUN. Игровой вариант добавляет выбранную папку RDR2. Для веб-примера достаточно одного выбранного файла. Система может запросить разрешение на открытие загрузки. При неожиданном запросе можно воспользоваться примером в браузере.

## Как разобраться в ошибке программы?

Положите копию журнала ошибок программы в рабочую папку REYRUN. Попросите ИИ прочитать и объяснить последнюю ошибку. В обычный веб-чат приложите только нужный фрагмент. Веб-пример сообщает контрольную сумму и число строк. Сам текст остаётся на устройстве.
