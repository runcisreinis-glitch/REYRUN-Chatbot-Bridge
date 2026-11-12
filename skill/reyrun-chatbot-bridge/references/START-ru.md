# Инструкция для ИИ · REYRUN Мост

[Latviski](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/) · [English](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/) · [Русский](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/)

[Скачать для Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [Скачать для Mac](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) · [Попробовать на телефоне или в браузере](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

Если вы пользуетесь Claude Desktop, файл для Windows или Mac подключит к нему одну рабочую папку REYRUN. После этого полностью закройте и снова откройте Claude Desktop. На Mac откройте файл .command из архива. При первом запуске система может запросить подтверждение.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-windows) · [Mac · macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-mac) · [Android](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-android) · [iPhone · iPad](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-iphone) · [Linux](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-linux)

[Заметка или письмо на телефоне](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/phone/)

## Пользуетесь ChatGPT в браузере?

[Запуск для ChatGPT на Windows](https://mcp.desktopcommander.app/remote-windows.cmd) · [Открыть подключение в ChatGPT](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

Подключите компьютер с Windows, macOS или Linux по инструкции Desktop Commander. Когда в терминале появится «Device ready», ChatGPT сможет работать с файлами этого компьютера, даже если вы открыли чат на телефоне. Для действий на самом телефоне выберите выше Android или iPhone. [Desktop Commander](https://desktopcommander.app/help/devices/connect-computer) · [Бесплатный план](https://desktopcommander.app/help/account-billing/plans-and-tool-call-limits)

## Проверка после запуска

Для Filesystem вызовите list_allowed_directories. Создайте тестовый файл в показанной папке и прочитайте его. Если содержимое отличается, остановите установку. Для Task Bridge вызовите bridge_status и read_checkpoint. Для первого save_checkpoint используйте revision 0. После обрыва связи вызовите read_checkpoint с прежним именем задания.

## 1. Filesystem MCP · 2.3.0

Windows, macOS. ИИ может навести порядок в выбранной папке и сделать точные копии файлов.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

**Проверка.** В Linux мы проверили сервер версии 2.3.0. Он показал разрешённые папки, прочитал сведения о файле, точно скопировал двоичные данные и отказал в доступе за пределами выбранных папок. На физическом ПК с Windows и установленным Node чистая установка заняла 6,68 секунды. Запись и чтение текста с диакритикой совпали, запрос вне рабочей папки был отклонён.

**Опыт за 2026 год.** В марте пользователь сообщил, что клиент заменил заданный список папок своим. В этом варианте используется --confine-roots и проверяется фактический список.

Для сеанса чтения добавьте --read-only. Проверьте, существует ли файл назначения. Команда copy_file откажется его перезаписывать. Обычный веб-чат без локального подключения может вести пользователя по шагам.

**Параллельная работа.** Назначьте одного автора для каждой папки. Разным папкам можно дать отдельные подключения.

[Filesystem MCP · tools and directory rules](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md) · [Filesystem 2.3.0 release](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) · [Desktop client setup for Windows and macOS](https://modelcontextprotocol.io/docs/develop/connect-local-servers) · [User report on effective roots, 16 March 2026](https://github.com/modelcontextprotocol/servers/issues/3602) · [GitHub · modelcontextprotocol/servers](https://api.github.com/repos/modelcontextprotocol/servers) · [Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/windows-filesystem.json) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 2. REYRUN Task Bridge · 1.0.0

Windows, macOS. Сохраните, на чём остановились, чтобы другой чат мог продолжить работу. У каждого задания своя история версий.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-macOS.command.zip)

**Проверка.** Компьютер с Windows, Node 24.19, 01:11 по Риге. Два запуска настроили подключение в тестовых папках с пробелами в названиях. Исходная настройка сохранилась. Один клиентский процесс записал первую версию, другой её прочитал. Попытка записи поверх устаревшей версии была отклонена. Четыре локальных клиента одновременно сохранили четыре разные задачи. Когда все четверо попытались изменить одну запись, сохранилось одно изменение. После перезапуска были доступны все пять задач.

**Опыт за 2026 год.** Собственное испытание проекта 12 ноября по Риге.

Профиль сохраняет записи заданий. Для копирования файлов выберите Filesystem.

**Параллельная работа.** Проверены четыре параллельных клиента и восстановление пяти задач.

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json) · [4 × stdio](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/parallel.json) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 3. Microsoft Playwright MCP · 0.0.85

Windows, macOS. Подходит для проверки собственного сайта: найти кнопку, перейти на следующую страницу, проверить читаемость. Каждой задаче можно дать отдельный профиль браузера.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-macOS.command.zip)

**Проверка.** На Windows и macOS наш файл запуска открыл отдельный процесс Chrome и передал снимок экрана клиенту чата. Мы открыли пустую страницу и убедились, что полученное изображение PNG читается.

**Опыт за 2026 год.** В японском практическом разборе автор отдельно проверил процессы браузера и состояние входа. Для параллельных задач он рекомендует явно выбирать изолированный профиль.

Новый профиль не содержит личных сеансов входа. В стандартном наборе есть выполнение кода. Авторы указывают, что --allowed-origins не гарантирует полной сетевой изоляции. Используйте доверенный тестовый сайт и ограничения инструментов клиента.

**Параллельная работа.** Каждому параллельному сеансу нужны свой процесс и профиль. В нашем тесте открывался один на каждую ОС.

[Microsoft release · 9 November 2026](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.85) · [Microsoft · browser profiles and documented options](https://github.com/microsoft/playwright-mcp) · [Author tests on Windows, macOS and Ubuntu · 11 November](https://github.com/microsoft/playwright-mcp/actions/runs/43074928448) · [Japanese first-person profile comparison · 29 June 2026](https://zenn.dev/ruri/articles/playwright-multi-session-isolation) · [GitHub · microsoft/playwright-mcp](https://api.github.com/repos/microsoft/playwright-mcp) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 4. Chrome DevTools MCP · 1.13.0

Windows, macOS. Удобен для визуальной проверки. Ограниченный набор инструментов открывает разрешённую страницу проекта и делает снимок экрана.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-macOS.command.zip)

**Проверка.** На Windows и macOS наш файл запуска открыл отдельный процесс Chrome и передал снимок экрана клиенту чата. Мы открыли пустую страницу и убедились, что полученное изображение PNG читается.

**Опыт за 2026 год.** Пользователь macOS сообщил, что после аварийного завершения сервера мог остаться тестовый процесс Chrome. Китайский автор отдельно опубликовал результаты проверки в Debian и перечислил непроверенные режимы.

Профиль временный. Для подключения к личной открытой вкладке нужен другой режим. Снимок может содержать частные данные, которые показывает сама тестовая страница. Завершайте сеанс через клиент.

**Параллельная работа.** В каждом сеансе свой процесс Chrome. В общем профиле вкладки могут смешиваться.

[Chrome DevTools release · 11 November 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0) · [Chrome DevTools MCP · configuration](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md) · [Upstream Windows/macOS/Ubuntu test matrix · 11 November](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43058501937) · [macOS report about abrupt termination · 26 August 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/2621) · [Chinese practitioner’s test log · 21 October 2026](https://friendlyai.top/projects/chrome-devtools-mcp/) · [Later upstream pre-release run · macOS/Node 22 failure](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43105363963) · [GitHub · ChromeDevTools/chrome-devtools-mcp](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 5. Desktop Commander · Remote / Local

Windows, macOS. Работает с файлами и сеансами терминала в фоне. Наш локальный файл запуска открывает три инструмента для просмотра одной рабочей папки.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-macOS.command.zip)

**Проверка.** На компьютере с Windows была версия 0.3.0. Desktop Commander прочитал файл, созданный через Reinis Bridge, и записал в него другой текст. Reinis Bridge прочитал все 22 байта. Так можно передать сведения о выполненной работе. История чатов при этом не переносится. Официальный набор удалённых инструментов позволяет работать с файлами, терминалом и сеансами процессов. При проверке файлов мы не использовали мышь и клавиатуру. Разработчик указывает поддержку Windows, macOS и Linux. Здесь проверен реальный компьютер с Windows.

**Опыт за 2026 год.** 13 октября 2026 года пользователь Windows с версией 0.2.52 сообщил, что start_process выводит окна консоли на передний план. 3 ноября другой пользователь с версией 0.3.1 сообщил о периодических тайм-аутах примерно через 60 секунд, хотя устройство отображалось в сети. Это отдельные случаи. В нашем тесте обмен файлами прошёл успешно.

Файл запуска использует локальный пакет 0.3.2. Remote 0.3.0 — отдельный сервис с привязкой. Элементы интерфейса проверяйте в профиле браузера.

**Параллельная работа.** Проверена передача файла между двумя инструментами. Предел числа одновременных чатов на устройстве не измерялся.

[local](https://github.com/wonderwhy-er/DesktopCommanderMCP) · [remote](https://github.com/desktop-commander/remote-desktop-commander) · [help](https://desktopcommander.app/help/getting-started/what-is-desktop-commander) · [reportFocus](https://github.com/wonderwhy-er/DesktopCommanderMCP/issues/852) · [reportTimeout](https://github.com/desktop-commander/remote-desktop-commander/issues/90)

## 6. Reinis Bridge · 1.0.0

Windows. Репозиторий проекта на GitHub создали в отдельном приватном окне Chrome через OpenBot. После проверки приложение закрылось. Локальный отчёт подтвердил, что пользовательский рабочий стол, принимающий ввод, остался прежним.



**Проверка.** 12 ноября в 00:58 по рижскому времени через действующий мост запустили две короткие фоновые задачи. Они выполнялись одновременно в течение 5,011 секунды. При повторном запросе с прежним ключом мост вернул уже выполненную задачу. Чтение вывода можно продолжить с сохранённой позиции.

**Опыт за 2026 год.** По опыту Рейниса доступен один интерактивный поток. В нашем тесте одновременно работали две фоновые задачи терминала. Управление рабочим столом из двух разных чатов одновременно мы не проверяли.

Это личный мост Рейниса для Windows. Программа запуска в этом проекте создаёт отдельное локальное подключение к выбранной вами папке. Она не устанавливает личный мост Рейниса и не даёт доступа к его компьютеру.

**Параллельная работа.** Один интерактивный рабочий стол. Два фоновых задания выполнялись одновременно 5,011 секунды.

[REYRUN · Windows](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

## 7. Git worktree + bundle · Git CLI · tested 2.52.0

Windows, macOS. Для передачи проектных файлов между сеансами без постоянного подключения. Каждая задача получает отдельную рабочую копию и ветку. Пакет переносит сохранённые в Git изменения на другой компьютер.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-macOS.command.zip)

**Проверка.** В Linux создали две рабочие копии. Изменение в первой не затронуло вторую. Проверенный пакет восстановил тот же коммит и точную копию файла.

**Опыт за 2026 год.** В немецком практическом опыте две задачи проверили в отдельных папках. Авторы воспроизвели действия исполнителей контролируемыми изменениями файлов.

Рабочие копии используют общую базу объектов Git. Полный пакет ветки может включать её историю. Для передачи создайте отдельный репозиторий только с выбранными файлами. Этот способ не даёт управления устройством, приложениями или мышью.

**Параллельная работа.** Проверены две рабочие копии, каждая в своей ветке.

[Git worktree manual](https://git-scm.com/docs/git-worktree) · [Git bundle manual](https://git-scm.com/docs/git-bundle) · [Git desktop downloads](https://git-scm.com/downloads) · [German practical two-role experiment · 9 September 2026](https://www.bitblokes.de/ki-agenten-git-worktrees/) · [GitHub · git/git](https://api.github.com/repos/git/git)

## 8. REYRUN · Web Crypto

Windows, macOS, Android, iOS. Откройте готовый скрипт в браузере и одним касанием проверьте пример либо выберите текстовый файл.

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

**Проверка.** На эмуляторе Android 15 одно касание обработало опубликованный пример без изменений. WebView 124.0.6367.219 вернул 13 байт, две строки и ожидаемую SHA-256. В предварительном просмотре Chrome получили тот же результат. В симуляторе iPhone SE с iOS 18.5 и WebKit кнопка примера дала тот же результат. Неподдерживаемое действие было отклонено. Испытания прошли на виртуальных устройствах.

**Опыт за 2026 год.** Независимых отзывов о новой демонстрации пока нет.

Это квитанция для одного файла. Чтобы чат объяснил ошибку, отдельно приложите нужный фрагмент текста.

**Параллельная работа.** У каждого задания свой файл или квитанция. Меню отправки телефона обслуживает одно действие за раз.

[REYRUN](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/web/start) · [MDN · File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API) · [MDN · SubtleCrypto.digest](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest) · [Android 15 · WebView · 2026-11-11](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121791094/job/130863821353) · [iPhone SE · iOS 18.5 · WebKit](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121668999/job/130863410709)

## 9. LocalSend

Windows, macOS, Android, iOS. Перешлите готовый файл на другое устройство в своей сети Wi-Fi.

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

**Проверка.** Передача между двумя устройствами здесь не проверялась. Передайте mobile-request.json и сравните ID и хеш квитанции с результатом нашей страницы.

**Опыт за 2026 год.** 25 июня 2026 года xueyexiao на китайском описал, как на Redmi K70 передал файл через меню файлового менеджера, когда у выбора файла в LocalSend не было доступа.

Нужны два соединённых устройства с LocalSend. Выберите файл и получателя.

**Параллельная работа.** У каждого задания свой файл или квитанция. Меню отправки телефона обслуживает одно действие за раз.

[LocalSend](https://localsend.org/download) · [2026 · Changelog](https://localsend.org/changelog) · [xueyexiao · Redmi K70 · 中文](https://github.com/localsend/localsend/discussions/835) · [REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 10. Nextcloud Files

Windows, macOS, Android, iOS. Сохраните подготовленный чатом файл в папке Nextcloud и продолжите работу с ним на компьютере.

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

**Проверка.** В этой сессии частный сервер не подключали. Проверьте ID и хеш файла, полученного на втором устройстве.

**Опыт за 2026 год.** 28 апреля 2026 года Sanook на немецком описал загрузку фотографии с Android, которая долго ждала в очереди и затем завершилась. В отчёте речь шла о фотографии.

Выбирайте, если у вас уже есть учётная запись и папка. Создание сервера — отдельная задача.

**Параллельная работа.** У каждого задания свой файл или квитанция. Меню отправки телефона обслуживает одно действие за раз.

[Nextcloud](https://nextcloud.com/install/) · [iOS · 2026](https://github.com/nextcloud/ios/issues) · [Sanook · Android · Deutsch](https://help.nextcloud.com/t/android-client-warte-auf-hochladen/217584/18) · [REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 11. Termux

Android. Проверьте готовый скрипт в закрытой папке Termux на Android.

[Готовый скрипт для Termux](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-termux.sh)

**Проверка.** Дважды запущен через sh в Linux. Созданы две отдельные папки и две квитанции с ожидаемым хешем. Запуск на Android здесь не проверялся.

**Опыт за 2026 год.** 30 апреля 2026 года slondr сообщил о зависании выбора файла на Pixel 9a с Android 16. В той же ветке разработчик сообщил об успешной проверке на двух Samsung.

Используйте при уже установленном Termux. Для обычного чата самый простой старт — веб-пример.

**Параллельная работа.** У каждого задания свой файл или квитанция. Меню отправки телефона обслуживает одно действие за раз.

[Termux](https://github.com/termux/termux-app) · [Android 15 · #5150](https://github.com/termux/termux-app/issues/5150) · [Termux · Installation](https://github.com/termux/termux-app#installation) · [Termux:API](https://github.com/termux/termux-api) · [slondr · Pixel 9a · English](https://github.com/termux/termux-app/issues/5101)

## 12. Apple Shortcuts

iOS, macOS. Передайте файл уже настроенной команде Apple через меню «Поделиться».

[Открыть готовый пример](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/start/)

**Проверка.** Эта последовательность здесь не проверялась на физическом iPhone. Откройте phone-test.txt в «Файлах» и убедитесь, что он содержит REYRUN-OK.

**Опыт за 2026 год.** 28 января 2026 года японский автор anyprogram описал команду для создания и сохранения TXT на iPhone и iPad. В режиме редактирования она перезаписывает выбранный файл.

Нужна ранее добавленная команда, принимающая файлы. Веб-пример можно попробовать сразу.

**Параллельная работа.** У каждого задания свой файл или квитанция. Меню отправки телефона обслуживает одно действие за раз.

[Apple · iPhone](https://support.apple.com/guide/shortcuts/launch-a-shortcut-from-another-app-apd163eb9f95/ios) · [Apple · Share](https://support.apple.com/guide/shortcuts/share-shortcuts-apdf01f8c054/ios) · [Apple · Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios) · [anyprogram · iPhone/iPad · 日本語](https://qiita.com/anyprogram/items/6cc1394569c687ed506c) · [iPhone 16 Pro Max · 2026](https://github.com/net00-1/SW-DLT/issues/133) · [REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 13. Desktop Commander Remote · ChatGPT

Windows, macOS, Linux. Работайте с файлами подключённого компьютера из веб-чата.

[Открыть инструкцию](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#devices)

**Проверка.** Разработчик описывает Windows, macOS и Linux.

**Опыт за 2026 год.** Документация разработчика.

Подключение должно работать на целевом компьютере.

**Параллельная работа.** Число одновременных сеансов для этого варианта не измерялось.

[Desktop Commander Remote · ChatGPT](https://desktopcommander.app/help/devices/connect-computer)

## 14. Google Gemini · Device assistance

Android. Попросите Gemini поставить таймер в приложении Часы.

[Открыть инструкцию](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-android)

**Проверка.** Google описывает действие в приложении Gemini для Android.

**Опыт за 2026 год.** Документация разработчика.

Требуется приложение Gemini для Android.

**Параллельная работа.** Число одновременных сеансов для этого варианта не измерялось.

[Google Gemini · Device assistance](https://support.google.com/gemini/answer/15235441)

## 15. Claude · Apple Reminders

iOS. Добавьте напоминание в существующий список на iPhone или iPad.

[Открыть инструкцию](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/#device-iphone)

**Проверка.** Anthropic описывает создание напоминаний с разрешения пользователя.

**Опыт за 2026 год.** Документация разработчика.

Нужны мобильное приложение Claude и доступ к напоминаниям.

**Параллельная работа.** Число одновременных сеансов для этого варианта не измерялось.

[Claude · Apple Reminders](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)

## Установите латышский перевод RDR2

Для сюжетного режима в Windows. Если в игре уже стоят проверенные сборки Universal RDR2 String Translator и Ultimate ASI Loader x64 9.7.4, закройте игру, скачайте и откройте установщик XML. Он сверит контрольные суммы обоих файлов, сохранит прежний латышский XML и установит проверенный перевод. Если в папке есть другой основной перевод или не хватает плагина, установщик остановится и покажет ссылку на инструкцию.

[Установить латышский XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Install-XML.cmd) · [Восстановить прежний XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Restore-XML.cmd)

Скачайте и откройте файл запуска для Windows. Он ищет игру в библиотеках Steam, Rockstar и Epic и подготавливает проверенный файл латышского перевода в рабочей папке. Если найдётся несколько папок, вы выбираете нужную. Передайте ИИ инструкцию по установке плагина, загрузчика, резервному копированию и проверке в сюжетном режиме. [Открыть инструкцию по переводу](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/ru/install/)

## Как четырём чатам работать одновременно?

Выделите каждому чату имя задачи и отдельную папку. Текст, сравнение и проверку файлов можно разделить. Изменения в папке игры поручите одному чату. Каждой сессии браузера нужен свой профиль. На общем рабочем столе мышью управляет одна сессия.

## Что делать, если связь прервалась?

Назовите новому чату прежнюю задачу. Попросите прочитать последнюю запись и проверить, какие файлы уже готовы. Если скачивание или копирование прервалось, сначала проверьте сам файл. Если два чата одновременно изменили одну запись, прочитайте сохранённую версию перед следующей правкой.

## Что чат-бот сможет делать на моём компьютере?

Файловый мост открывает одну рабочую папку REYRUN. Игровой вариант добавляет выбранную папку RDR2. Для веб-примера достаточно одного выбранного файла. Система может запросить разрешение на открытие загрузки. При неожиданном запросе можно воспользоваться примером в браузере.

## Как разобраться в ошибке программы?

Положите копию журнала ошибок программы в рабочую папку REYRUN. Попросите ИИ прочитать и объяснить последнюю ошибку. В обычный веб-чат приложите только нужный фрагмент. Веб-пример сообщает контрольную сумму и число строк. Сам текст остаётся на устройстве.

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
