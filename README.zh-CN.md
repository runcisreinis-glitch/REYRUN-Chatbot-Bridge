# 让 AI 帮你处理电脑里的事

电脑快没空间了。你问 AI 怎么办，它让你打开设置、找文件、挨个看大小。其实，你想知道的就一件事：到底是哪些文件占了地方？

REYRUN 做的这个“桥”，可以把你平时用来聊天的 AI 连到你允许它访问的文件夹。连好后，你可以直接说：“帮我找出这个文件夹里最大的五个文件，告诉我各有多大。先别删。”这套工具从安装到使用都免费。

**怎么用？** 把这页的网址复制到你平时和 AI 聊天的地方，再说一句你想做什么。它会看你用的是什么设备和聊天软件，告诉你接下来要点哪里。你不用自己写程序。

> 帮我连接这台设备。我想找出下载文件夹里最大的五个文件，先把文件名和大小列给我。请用中文一步一步告诉我，需要我点的时候再说。
> https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/README.zh-CN.md

网页版 AI 聊天默认看不到你的文件。你用的聊天软件如果不支持连接设备，AI 可以帮你选一个能连接的办法。手机上也能用：例如选一份文本，在浏览器里核对文件内容；如果你要处理的是电脑上的文件，也可以从手机和已配对的电脑对话。

<details>
<summary>给 AI 的连接说明</summary>

先阅读[设备连接技能（skill）](skill/reyrun-chatbot-bridge/SKILL.md)。用中文回复，优先复用已经可用的连接，只询问会影响选择的信息。按用户实际使用的聊天客户端、设备和任务选一种连接方式，给出对应的下载或设置入口。公开网页的演示只处理用户选择的文件，不能据此声称已连接设备。

如果需要安装，请按当前系统准备一个可直接运行的脚本，把准备工作和安装后的检查放在里面。如果首选方式不可用，脚本只能改用官方支持、无需扩大权限的备用方式。需要授权时交给用户确认；若没有可用的备用方式，就停止并说清原因。请用一个临时文件实测读写结果。

- **Windows 或 macOS 上的 Claude Desktop**：需要操作文件时，可以用项目的文件夹连接程序。只在已授权的目录内工作。连接后先列出可访问的目录，再用临时测试文件验证读写；如果实际可访问的范围不包括“下载”，请先让用户选择或授权对应文件夹。[Windows 下载](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [macOS 下载](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)
- **网页版聊天**：先查看当前对话是否支持设备连接。网页版 ChatGPT 如可使用 Desktop Commander，可以按其指引配对电脑；若当前聊天只支持文字，请向用户说明并提供可用的入口。[电脑配对说明（英文）](https://desktopcommander.app/help/devices/connect-computer)
- **手机**：先分清要处理的是手机里的文件，还是另一台电脑上的文件。手机浏览器提供本地文件示例；Android 还可以用 Termux，iPhone 和 iPad 可通过分享菜单将所选文件交给快捷指令。[手机浏览器示例](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/start/)

安装时可能要确认系统提示或重新打开聊天软件。请只报告实际完成的步骤。核对文件时先列出结果，按用户要求保留原文件。

</details>

想让 AI 记住上次查资料时哪些办法管用？[看递归深度搜索的中文说明](https://github.com/runcisreinis-glitch/reyrun-recursive-deep-search/blob/main/zh-CN/README.md)。
