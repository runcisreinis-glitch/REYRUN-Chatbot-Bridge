# REYRUN 桥接工具：把 AI 聊天助手连到您的设备

[Latviski](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/) · [English](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/) · [Deutsch](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/de/) · [日本語](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/) · [简体中文](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/) · [Русский](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/)

## 给设备所有者一个启动文件

收到本页地址后，先确认要在哪台设备上完成任务，并检查已经获得授权的连接。确实需要设置时，给用户一个可直接运行的启动文件。如果现有启动文件不适合这项任务，就按下面的步骤为这台设备准备一个脚本。每次只告诉用户接下来需要做什么。

1. 检查当前状态。如果任务已经完成，验证结果后结束。只在获得授权的文件夹内操作。
2. 先采用项目支持的方法。下载暂时中断时，限定重试次数，或改用同一版本的官方副本。运行前核对预期的校验值或签名。没有写入权限时，只有在能够实现同一目标的情况下，才改用软件支持的用户目录。
3. 如需配对、选择文件或授予系统权限，说明需要确认的具体事项，等待设备所有者决定。被拒绝后停止。只有任务确实能靠交接一个文件完成时，才采用这种方式。
4. 更改前保存可恢复的状态。中断后先检查实际完成的步骤，再从第一个未完成的步骤继续。重复运行时保留已有设置和备份。
5. 从聊天中实际执行一项操作，核验结果。例如，读取授权文件夹中一份事先不知道内容的文件，并比对内容。说明结果或尚未解决的具体问题。下载、打开文件、系统授权和客户端操作分别计数。不要承诺固定的点击次数。

## 启动后的检查

使用 Filesystem 时，调用 list_allowed_directories，只在返回的工作文件夹内写入一个测试文件并读回。内容不一致就停止。使用 Task Bridge 时，先调用 bridge_status，再调用 read_checkpoint。首次 save_checkpoint 使用 revision 0。断开后，使用相同的任务标识再次调用 read_checkpoint。

如果聊天里的 AI 打不开这个网站、没有访问权限，或者拒绝打开链接，您可以直接把说明发给它。下载文件，作为附件发到对话里即可。

[下载说明（.md）](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/download/REYRUN-Bridge-Instructions-zh.md)

## 给 AI 的操作说明和技术资料

## 聊天助手使用的技能（skill）

如果用户只发来本页地址，请帮他把聊天助手连到自己的电脑。已有合适的连接就直接用。只有不知道操作系统时才询问。给出对应的启动文件或官方安装链接，说明需要打开什么、确认什么。如果当前聊天工具不支持连接，请指出可以使用的客户端。

[ZIP](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/download/REYRUN-Bridge-Skill-zh.zip) · [GitHub](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge)

在 Windows 上，下载并打开一个文件即可。首次连接 ChatGPT 时还要在浏览器里确认设备。已经连过，就可以直接问它有关文件的问题。

## 可粘贴到聊天窗口的消息

> 请帮我把这个聊天窗口连到我的电脑。找出“下载”文件夹里最大的五个文件，告诉我各有多大。不要删除任何文件。请使用 REYRUN 技能，需要我点击时告诉我。 https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/ https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ai/zh.md

您想让聊天助手在哪台设备上操作？

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/#device-windows) · [Mac · macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/#device-mac) · [Android](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/#device-android) · [iPhone · iPad](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/#device-iphone) · [Linux](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/#device-linux)

## 连接您的设备

## Windows · 处理电脑上的文件

## ChatGPT · Desktop Commander Remote

打开 Windows 官方启动程序。在 ChatGPT 中连接 Remote Desktop Commander 并登录。核对设备代码与终端里的代码，一致后确认，保持终端打开。让助手列出已连接的设备，并读取测试文件中的一行。按 Ctrl+C 可断开连接。

[下载 Windows 启动程序 →](https://mcp.desktopcommander.app/remote-windows.cmd) · [官方设置指南 →](https://desktopcommander.app/help/devices/connect-computer) · [在 ChatGPT 中连接 →](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

## Claude Desktop · REYRUN

在装有 Claude Desktop 的电脑上下载并打开 REYRUN 启动程序。完全退出并重新打开 Claude Desktop，让它在工作文件夹里建一份笔记，再读出其中的内容。

[REYRUN · Windows →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd)

## Mac · macOS · 处理电脑上的文件

## ChatGPT · Desktop Commander Remote

打开官方指南，在终端运行 Mac 部分的设置命令。在 ChatGPT 中连接 Remote Desktop Commander 并登录。核对设备代码与终端里的代码，一致后确认，保持终端打开。让助手列出已连接的设备，并读取测试文件中的一行。按 Ctrl+C 可断开连接。

[官方设置指南 →](https://desktopcommander.app/help/devices/connect-computer) · [在 ChatGPT 中连接 →](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

## Claude Desktop · REYRUN

在装有 Claude Desktop 的 Mac 上下载 REYRUN 启动程序。解压 ZIP 并打开其中的 .command 文件。重新启动 Claude Desktop，让它在工作文件夹里写一份笔记，再读出内容。

[REYRUN · macOS →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

## Android · 计时器、文件和笔记

## Google Gemini · Android

打开手机上的 Gemini，让它设一个五分钟的计时器，然后到“时钟”应用查看倒计时。如果没有成功，在已连接的应用中检查 Device assistance（原名 Utilities）是否已启用。

[Google Play · Gemini →](https://play.google.com/store/apps/details?id=com.google.android.apps.bard) · [Google 使用指南 →](https://support.google.com/gemini/answer/15235441)

## ChatGPT · Desktop Commander Remote

开发者提供了一个通过 Termux 访问安卓文件的实验性方案。配对后可以问助手手机还剩多少空间。访问范围取决于 Termux 的权限，Android 可能会中断后台连接。

[开发者的 Android 指南 →](https://desktopcommander.app/help/devices/connect-android-phone)

## 使用其他在线聊天助手

让助手写一份笔记或邮件草稿。您可以在手机上核对内容，然后保存为文件，或在邮件应用中打开草稿。何时发送由您决定。

[准备笔记或邮件 →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/phone/) · [查看文件校验值 →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/start/)

## iPhone · iPad · 提醒事项和笔记

## Claude · Apple Reminders

在 iPhone 或 iPad 上，让 Claude 在已有列表中添加一项名为“REYRUN 测试”的提醒。出现提示时允许访问，再打开“提醒事项”核对记录。您可以在设备设置中撤销 Claude 的权限。

[App Store · Claude →](https://apps.apple.com/app/id6473753684) · [Anthropic 使用指南 →](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)

## 使用其他在线聊天助手

让助手写一份笔记或邮件草稿。您可以在手机上核对内容，然后保存为文件，或在邮件应用中打开草稿。何时发送由您决定。

[准备笔记或邮件 →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/phone/) · [查看文件校验值 →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/start/)

## Linux · 处理电脑上的文件

## ChatGPT · Desktop Commander Remote

打开官方指南，在终端运行 Linux 部分的安装命令。在 ChatGPT 中连接 Remote Desktop Commander 并登录。核对设备代码与终端里的代码，一致后确认，保持终端打开。让助手列出已连接的设备，并读取测试文件中的一行。按 Ctrl+C 可断开连接。

[官方设置指南 →](https://desktopcommander.app/help/devices/connect-computer) · [在 ChatGPT 中连接 →](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

## 如果您使用 Claude Desktop

Windows 或 Mac 启动程序会为 Claude Desktop 连接一个 REYRUN 工作文件夹。Mac 用户请打开 ZIP 内的 .command 文件。退出并重新启动 Claude Desktop。首次运行时系统可能要求确认。

[下载 Windows 启动程序](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [下载 Mac 启动程序](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) · [给 AI 的说明（.zip）](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/download/REYRUN-Bridge-Skill-zh.zip)

## 在浏览器里使用 ChatGPT？

[ChatGPT 的 Windows 启动程序](https://mcp.desktopcommander.app/remote-windows.cmd) · [Mac 和 Linux 设置](https://desktopcommander.app/help/devices/connect-computer) · [打开 ChatGPT 连接器](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

按 Desktop Commander 指南配对 Windows、Mac 或 Linux 电脑。终端出现“Device ready”后，即使在手机上打开 ChatGPT，也能处理这台电脑的文件。要操作手机本身，请查看上面的 Android 或 iPhone 指南。

[Desktop Commander](https://desktopcommander.app/help/devices/connect-computer) · [免费方案](https://desktopcommander.app/help/account-billing/plans-and-tool-call-limits)

## 为 RDR2 安装拉脱维亚语翻译

适用于 Windows 故事模式。如果已安装测试过的 Universal RDR2 String Translator 和 Ultimate ASI Loader x64 9.7.4，请退出游戏，下载并打开 XML 安装程序。它会核对两个插件的校验值，备份已有的拉脱维亚语 XML，再安装经过核验的翻译。如发现基础翻译不匹配或缺少插件，会停止并显示操作指南。

[安装拉脱维亚语 XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Install-XML.cmd) · [恢复原来的 XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Restore-XML.cmd)

下载并打开 Windows 启动程序。它会在 Steam、Rockstar 和 Epic 游戏库中查找游戏，把核验过的翻译存入工作文件夹。如找到多处安装，请选择正确的文件夹，再把插件、加载器、备份和故事模式验证的说明交给助手。

[下载 RDR2 启动程序](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-rdr2-Windows.cmd) · [打开翻译安装指南](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/zh/install/)

## 其他连接方式及测试结果

选择设备，再展开工具说明，就能看到它能做什么、做过哪些测试，以及资料来源。

## 01. Filesystem MCP · 2.3.0

工作文件夹 · Windows · macOS · GitHub ★ 91 934

AI 可以整理所选文件夹中的文件，并制作完全相同的副本。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

测试结果 · 在 Linux 测试中，2.3.0 版服务器列出了授权文件夹，读取了文件信息，原样复制了二进制文件，并拒绝访问授权范围之外的文件。在已装 Node 的 Windows 电脑上，设置耗时 6.68 秒，写入和读出的拉脱维亚语笔记内容一致，访问范围限于工作文件夹。

2026 年使用记录 · 一位用户在 3 月报告，客户端指定的根目录覆盖了命令行的选择。本方案使用 --confine-roots，并检查实际生效的授权目录。

并行工作 · 每个文件夹只由一个助手写入。不同文件夹可以分别连接。

如只需读取，请添加 --read-only。复制前先检查目标位置是否已有同名文件，copy_file 不会覆盖现有文件。未建立本地连接的网页助手可以指导您操作。

[Filesystem MCP · 工具和目录权限](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md)

[Filesystem 2.3.0 发布说明](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0)

[Windows 和 macOS 桌面客户端设置](https://modelcontextprotocol.io/docs/develop/connect-local-servers)

[实际授权目录的用户报告 · 2026 年 3 月 16 日](https://github.com/modelcontextprotocol/servers/issues/3602)

[GitHub · modelcontextprotocol/servers](https://api.github.com/repos/modelcontextprotocol/servers)

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/windows-filesystem.json)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 02. REYRUN Task Bridge · 1.0.0

任务记录 · Windows · macOS

保存当前进度，另一个助手就能接着做。每项任务都有独立的版本记录。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-macOS.command.zip)

测试结果 · 里加时间 01:11，在运行 Node 24.19 的 Windows 实机上测试。两次启动都能在名称含空格的测试文件夹建立连接，并保留原设置。一个客户端保存第 1 版，另一个可以读取；基于旧版本的写入被拒绝。四个本地客户端同时保存了四项不同任务。四者同时改同一条记录时，只有一次成功。重启后五项任务仍可读取。

2026 年使用记录 · 项目于 11 月 12 日在里加进行测试。

并行工作 · 四个客户端可同时工作。重启后五项任务都能找回。

此配置用于保存任务记录。要复制文件，请选择 Filesystem。

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

[4 × stdio](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/parallel.json)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 03. Microsoft Playwright MCP · 0.0.85

独立浏览器 · Windows · macOS · GitHub ★ 39 515

适合测试自己的网页，包括查找按钮、翻页和检查内容能否正常阅读。每项任务都可以用单独的浏览器配置。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-macOS.command.zip)

测试结果 · 在 Windows 和 macOS 上，启动程序均打开独立的 Chrome 进程，并将截图返回聊天客户端。我们打开空白页，确认返回的 PNG 可以正常读取。

2026 年使用记录 · 一位日本作者分别测试了浏览器进程和登录状态，建议并行任务明确使用隔离的浏览器配置。

并行工作 · 每个并行会话使用独立进程和配置。本次在每个操作系统上各测试了一个会话。

新配置不会登录您的个人账户。默认工具可以执行代码。项目文档说明，单靠 --allowed-origins 不能完全隔离网络。请选用可信的测试站点，并检查客户端的工具权限。

[Microsoft 发布说明 · 2026 年 11 月 9 日](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.85)

[Microsoft · 浏览器配置与选项](https://github.com/microsoft/playwright-mcp)

[开发者的 Windows、macOS 和 Ubuntu 测试 · 11 月 11 日](https://github.com/microsoft/playwright-mcp/actions/runs/43074928448)

[日本用户的配置对比实测 · 2026 年 6 月 29 日](https://zenn.dev/ruri/articles/playwright-multi-session-isolation)

[GitHub · microsoft/playwright-mcp](https://api.github.com/repos/microsoft/playwright-mcp)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 04. Chrome DevTools MCP · 1.13.0

独立浏览器 · Windows · macOS · GitHub ★ 55 113

适合检查页面外观。受限的工具集可打开获准查看的项目页面并截图。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-macOS.command.zip)

测试结果 · 在 Windows 和 macOS 上，启动程序均打开独立的 Chrome 进程，并将截图返回聊天客户端。我们打开空白页，确认返回的 PNG 可以正常读取。

2026 年使用记录 · 一位 macOS 用户报告，服务器异常退出后，测试用 Chrome 进程仍在运行。另一位中国用户发布了 Debian 实测记录，并注明未测试的模式。

并行工作 · 每个会话使用独立的 Chrome 进程，共用配置可能会混淆标签页。

此配置是临时的。要操作已打开的个人标签页，需使用另一种连接模式。测试页显示的个人信息也会出现在截图里。请在客户端结束会话。

[Chrome DevTools 发布说明 · 2026 年 11 月 11 日](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0)

[Chrome DevTools MCP · 配置](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md)

[上游 Windows、macOS、Ubuntu 测试记录 · 11 月 11 日](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43058501937)

[macOS 异常退出报告 · 2026 年 8 月 26 日](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/2621)

[中文实测记录 · 2026 年 10 月 21 日](https://friendlyai.top/projects/chrome-devtools-mcp/)

[后续预发布测试 · macOS 和 Node 22 下的错误](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43105363963)

[GitHub · ChromeDevTools/chrome-devtools-mcp](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 05. Desktop Commander · 远程／本地

文件检查 · Windows · macOS · GitHub ★ 10 284

可在后台处理文件和终端会话。本地启动程序提供三种工具，用于检查一个工作文件夹。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-macOS.command.zip)

测试结果 · Windows 实机报告版本 0.3.0。Desktop Commander 读取 Reinis Bridge 创建的测试文件，写入另一段文本，随后 Reinis Bridge 完整读回 22 个字节。共享文件可以传递工作进度，聊天记录需另行交接。官方远程工具可操作文件、终端和进程会话，本次文件操作没有使用鼠标或键盘。开发者列出 Windows、macOS 和 Linux；本次实机测试使用 Windows。

2026 年使用记录 · 2026 年 10 月 13 日，有 Windows 用户报告 0.2.52 版的 start_process 会将控制台窗口置于前台。11 月 3 日，另一位 0.3.1 用户报告，设备虽显示在线，有时约 60 秒后仍会超时。以上是个别使用记录，本次文件交接成功。

并行工作 · 已验证两个工具之间的文件交接。单台设备支持的最大并发聊天数未测量。

启动程序使用本地软件包 0.3.2。远程版 0.3.0 是需要配对的独立服务。可使用浏览器配置检查图形控件。

[本地版](https://github.com/wonderwhy-er/DesktopCommanderMCP)

[远程版](https://github.com/desktop-commander/remote-desktop-commander)

[使用指南](https://desktopcommander.app/help/getting-started/what-is-desktop-commander)

[控制台窗口问题报告](https://github.com/wonderwhy-er/DesktopCommanderMCP/issues/852)

[连接超时报告](https://github.com/desktop-commander/remote-desktop-commander/issues/90)

## 06. Reinis Bridge · 1.0.0

专用桌面 · Windows

这个项目的 GitHub 仓库是在 OpenBot 的独立 Chrome 会话中创建的。专用应用关闭后，本地记录确认用户操作的桌面没有切换。

测试结果 · 里加时间 11 月 12 日 00:58，两项短后台任务通过已有连接运行，执行时间重叠了 5.011 秒。用原任务键再次请求，会返回已完成的任务。客户端可从已保存的位置继续读取输出。

2026 年使用记录 · 雷尼斯实际使用过一路交互会话。测试中两项后台终端任务可同时运行，未测试两个聊天助手同时控制桌面。

并行工作 · 一个交互桌面，两项后台任务有 5.011 秒同时运行。

这是雷尼斯个人使用的 Windows 连接。本项目的公开启动程序会在您自己的电脑上连接所选文件夹，不会安装他的专用桥接工具，也不会让您访问他的电脑。

[REYRUN · Windows](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

## 07. Git worktree + bundle · Git CLI · 已测试 2.52.0

文件交接 · Windows · macOS · GitHub ★ 64 269

不需要实时连接也能交接项目文件。每项任务用独立工作副本和分支，通过 bundle 将已提交的改动转移到另一台电脑。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-macOS.command.zip)

测试结果 · 在 Linux 上建立了两个工作树，修改其中一个后，另一个保持原样。核验 bundle 后重新克隆，提交和文件字节均与原件一致。

2026 年使用记录 · 一篇德语实测在两个文件夹分别检查两项任务，作者用受控的文件改动模拟两位执行者的操作。

并行工作 · 已测试两个工作副本，各使用独立分支。

工作树共用 Git 对象库。完整的分支 bundle 可能包含历史记录。对外分享时，请新建只包含所选文件的仓库。此方式仅用于文件交接，不能控制设备、应用或鼠标。

[git worktree 手册](https://git-scm.com/docs/git-worktree)

[git bundle 手册](https://git-scm.com/docs/git-bundle)

[下载电脑端 Git](https://git-scm.com/downloads)

[德语双角色实验 · 2026 年 9 月 9 日](https://www.bitblokes.de/ki-agenten-git-worktrees/)

[GitHub · git/git](https://api.github.com/repos/git/git)

## 08. REYRUN · Web Crypto

文件交接 · Windows · macOS · Android · iOS

在浏览器中打开现成的脚本，轻点一下即可检查示例，也可以选择自己的文本文件。

[打开示例](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/start/)

测试结果 · 在 Android 15 模拟器上轻点一次，WebView 124.0.6367.219 对公开示例给出 13 字节、2 行和预期的 SHA-256。Chrome 预览及采用 iOS 18.5 和 WebKit 的 iPhone SE 模拟器得到相同结果。不支持的操作被拒绝。这些测试均在模拟设备上完成。

2026 年使用记录 · 这个新示例暂时还没有独立用户的使用报告。

并行工作 · 每项任务使用单独的文件或报告。手机的分享菜单一次处理一项操作。

报告仅针对一个文件。要让助手解释错误，还需单独提供相关的文字片段。

[REYRUN](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/web/start)

[MDN · File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API)

[MDN · SubtleCrypto.digest](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest)

[Android 15 · WebView · 2026-11-11](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121791094/job/130863821353)

[iPhone SE · iOS 18.5 · WebKit](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121668999/job/130863410709)

## 09. LocalSend

文件交接 · Windows · macOS · Android · iOS

把准备好的文件发送到同一 Wi-Fi 网络里的另一台设备。

[打开示例](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/start/)

测试结果 · 这里没有实测两台设备之间的传输。您可以把 mobile-request.json 发到第二台设备，对照此页核验报告的标识和校验值。

2026 年使用记录 · 2026 年 6 月 25 日，xueyexiao 在中文讨论中提到，Redmi K70 上的 LocalSend 文件选择器权限不足，但从 Android 文件管理器的分享菜单仍可发送。

并行工作 · 每项任务使用单独的文件或报告。手机的分享菜单一次处理一项操作。

需两台已联网且装有 LocalSend 的设备。请选择文件和接收方。

[LocalSend](https://localsend.org/download)

[2026 年更新记录](https://localsend.org/changelog)

[xueyexiao · Redmi K70 · 中文](https://github.com/localsend/localsend/discussions/835)

[REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 10. Nextcloud Files

文件交接 · Windows · macOS · Android · iOS

将助手准备的文件存入 Nextcloud 文件夹，随后可在电脑上打开。

[打开示例](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/start/)

测试结果 · 本次没有连接私人服务器。可在第二台设备上核对接收文件的标识和校验值。

2026 年使用记录 · 2026 年 4 月 28 日，Sanook 用德语记录了一次 Android 照片上传：先是排队等待，后来上传完成。记录里上传的是一张照片，和我们使用的测试文件不同。

并行工作 · 每项任务使用单独的文件或报告。手机的分享菜单一次处理一项操作。

适合已有账号和文件夹的用户。搭建新服务器是另一项工作。

[Nextcloud](https://nextcloud.com/install/)

[iOS · 2026](https://github.com/nextcloud/ios/issues)

[Sanook · Android · Deutsch](https://help.nextcloud.com/t/android-client-warte-auf-hochladen/217584/18)

[REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 11. Termux

本地脚本 · Android

在 Android 的 Termux 私有目录中测试现成脚本。

[Termux 脚本](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-termux.sh)

测试结果 · 在 Linux 上用 sh 运行两次，每次都生成独立文件夹和报告，校验值符合预期。本次没有在 Android 上运行。

2026 年使用记录 · 2026 年 4 月 30 日，slondr 报告采用 Android 16 的 Pixel 9a 上文件选择器卡住。同一讨论中，开发者表示两台三星手机可正常选择。

并行工作 · 每项任务使用单独的文件或报告。手机的分享菜单一次处理一项操作。

此方式适用于已安装 Termux 的情况。普通网页聊天助手可先使用浏览器示例。

[Termux](https://github.com/termux/termux-app)

[Android 15 · #5150](https://github.com/termux/termux-app/issues/5150)

[Termux · 安装](https://github.com/termux/termux-app#installation)

[Termux:API](https://github.com/termux/termux-api)

[slondr · Pixel 9a · English](https://github.com/termux/termux-app/issues/5101)

## 12. Apple Shortcuts

文件交接 · iOS · macOS

通过分享菜单把文件传给已设置好的 Apple 快捷指令。

[打开示例](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/start/)

测试结果 · 本次没有在实体 iPhone 上验证这套流程。请在“文件”中打开已保存的 phone-test.txt，检查里面是否有 REYRUN-OK。

2026 年使用记录 · 2026 年 1 月 28 日，日本作者 anyprogram 介绍了在 iPhone 和 iPad 上创建、保存 TXT 文件的快捷指令。编辑已有文件的模式会覆盖所选文件。

并行工作 · 每项任务使用单独的文件或报告。手机的分享菜单一次处理一项操作。

需预先设置能接收文件的快捷指令。浏览器示例可直接使用。

[Apple · iPhone](https://support.apple.com/guide/shortcuts/launch-a-shortcut-from-another-app-apd163eb9f95/ios)

[Apple · 分享快捷指令](https://support.apple.com/guide/shortcuts/share-shortcuts-apdf01f8c054/ios)

[Apple · 快捷指令使用手册](https://support.apple.com/guide/shortcuts/welcome/ios)

[anyprogram · iPhone/iPad · 日本語](https://qiita.com/anyprogram/items/6cc1394569c687ed506c)

[iPhone 16 Pro Max · 2026](https://github.com/net00-1/SW-DLT/issues/133)

[REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 13. Desktop Commander Remote · ChatGPT

已连接的应用 · Windows · macOS · Linux

从网页聊天窗口操作已配对电脑中的文件。

[打开设置指南](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/#devices)

测试结果 · 开发者提供了 Windows、macOS 和 Linux 的操作说明。

2026 年使用记录 · 来自开发者文档。

并行工作 · 此方式的并发会话数未测量。

连接服务必须在目标电脑上运行。

[Desktop Commander Remote · ChatGPT](https://desktopcommander.app/help/devices/connect-computer)

## 14. Google Gemini · Device assistance

已连接的应用 · Android

让 Gemini 在手机的“时钟”应用中设置计时器。

[打开设置指南](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/#device-android)

测试结果 · Google 的文档介绍了这一功能在 Android 版 Gemini 中的用法。

2026 年使用记录 · 来自开发者文档。

并行工作 · 此方式的并发会话数未测量。

需要 Android 版 Gemini 应用。

[Google Gemini · Device assistance](https://support.google.com/gemini/answer/15235441)

## 15. Claude · Apple Reminders

已连接的应用 · iOS

在 iPhone 或 iPad 已有的列表中添加提醒事项。

[打开设置指南](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/#device-iphone)

测试结果 · Anthropic 文档说明了如何在获得许可后创建提醒事项。

2026 年使用记录 · 来自开发者文档。

并行工作 · 此方式的并发会话数未测量。

需要 Claude 移动应用和“提醒事项”的访问权限。

[Claude · Apple Reminders](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)

## 让另一个助手接手

## 怎样让四个聊天助手同时工作？

为每个助手分配单独的任务标识和文件夹。写作、比较和检查可分开进行。游戏安装目录只交给一个助手修改。每个浏览器会话使用独立配置，共用桌面时一次只让一个会话控制鼠标。

## 连接中断了怎么办？

把同一个任务标识交给新助手，让它先读上次保存的记录，检查哪些文件已完成。下载或复制中断时，先检查已有文件再重试。若两个助手改过同一条记录，下次修改前要先读当前保存的版本。

## 聊天助手能访问什么？

文件启动程序开放一个 REYRUN 工作文件夹，游戏版还会加入您所选的 RDR2 目录。浏览器示例只使用您选择的一个文件。首次打开下载文件时，系统可能要求授权。如果出现意外请求，可以先使用浏览器示例。

## 如何定位应用程序错误？

把错误日志的副本放入 REYRUN 工作文件夹，让助手读出并解释最后一条错误。使用普通网页聊天时，只需附上相关文字。浏览器示例提供校验值和行数，日志内容仍保留在设备上。

[给 AI 的说明](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ai/zh.md) · [测试与来源](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/research)

## 客户端从哪里读取连接设置？

启动程序在 Windows 上查找 %APPDATA%/Claude，在 Mac 上查找 ~/Library/Application Support/Claude。修改前备份 claude_desktop_config.json，只添加选定的 reyrun-… 条目。如未安装客户端，START.txt 会指向浏览器示例。其他兼容的本地 MCP 客户端可以使用生成的 runtime/reyrun-…-client.json，里面的可执行文件路径针对本机。

## 任务交接示例

保存最后核验的结果和下一项操作。使用相同本地配置的新助手可以用相同任务标识调用 read_checkpoint。普通网页助手则可接收粘贴的进度和所需附件。游戏窗口和授权对话框一次只交给一个会话操作。

```json
{
  "name": "save_checkpoint",
  "arguments": {
    "job": "game-check",
    "revision": 0,
    "done": "已读回测试文件，内容与原文一致。",
    "next": "核对选定的游戏文件夹。"
  }
}
```
