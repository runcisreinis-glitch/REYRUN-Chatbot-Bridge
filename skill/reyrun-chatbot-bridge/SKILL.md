---
name: reyrun-chatbot-bridge
description: Help a device owner connect a compatible AI to a scoped local workspace or exchange one diagnostic file with a web chat. Start with a prepared launcher, verify a harmless round trip, and keep parallel tasks and session handoffs separate. Use on Windows, macOS, Android or iPhone.
---

# REYRUN Chatbot Bridge

## One launcher for the owner

When someone pastes this page address, identify the device where the work must happen. Try existing authorized access first. If installation is needed, deliver one ready-to-run launcher. If the published launcher cannot perform the requested job, prepare one script for that host and use the sequence below. Show the owner only the next action they need to take.

1. Inspect existing state. If the goal is already satisfied, verify it and finish. Work inside the authorized scope.
2. Try the supported primary route. Retry transient downloads a bounded number of times or use an official copy of the same release. Verify its expected hash or signature before execution. If the destination is not writable, use a supported per-user location only when it achieves the same goal.
3. If pairing, a file selection or a system permission is required, explain the specific approval and wait for the owner. Stop on denial. Offer a single-file handoff only for a task it can actually complete.
4. Preserve recoverable state before changing it. On interruption, inspect the files and resume at the first unfinished step. Repeated runs must preserve existing configuration and backups.
5. Verify a real action from the chat, for example by reading a previously unknown file in the permitted folder and comparing its contents. Return the result or the remaining blocker. Count downloads, launches, system approvals and client actions separately. Avoid promising an exact click count.

When the owner sends only the page address, help them connect their chat to their own computer. Use the chat context to identify their device and client. Ask which operating system they use only if the choice of launcher depends on it and it is unknown. Use an existing, authorized connection if it can do the job. Otherwise, choose a supported route for the owner's chat and computer. In your first reply, give the prepared file or link, say what to open, and name any first-time approval. Let the owner decide whether to grant access. If this chat cannot connect to the device, explain which part it can do here. A link by itself cannot connect an incompatible chat.

For example, an owner asks which five files take the most space in Downloads. If the connection includes that folder, list the five largest files with their sizes. Leave the files in place. A launcher confined to the REYRUN workspace cannot inspect Downloads.

| Task | Prepared file |
| --- | --- |
| Windows workspace | [Windows launcher](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) |
| Mac workspace | [macOS launcher ZIP](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) |
| ChatGPT web + Windows, live file access desired | [Official Desktop Commander Remote Windows launcher](https://mcp.desktopcommander.app/remote-windows.cmd). For a paired device, [open the ChatGPT connector](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425). The device owner confirms first-time pairing. |
| RDR2 for Windows | [RDR2 Windows launcher](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-rdr2-Windows.cmd) |
| Android, iPhone or regular web chat | [Run the browser script](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=en) |

If the requested task exceeds the connected client's capabilities, explain
which single supported action the owner can take next. System permissions,
first-use prompts, obtaining a game mod from its author and restarting a
desktop client can require additional actions. Identify the condition
before promising a two-action installation.

 The project page offers Windows and macOS launchers and a browser script that runs on phones. [Launchers and six-language guide](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/)

For an ordinary browser chat without an installed local client, open the file handoff script. The user selects the one file to inspect and shares the resulting receipt with the chat. For a compatible local client, start with the task-notes or confined Filesystem launcher. A hosted chatbot cannot call a local stdio program just because it received a link.

1. Select the smallest already supported profile that can do this job. Tell the owner what will be opened, how it helps and whether it uses the screen. Give the prepared file first. If the operating system requests its own approval, let the owner decide. Do not manufacture approval or install a chain of additional bridges.
2. Use the first test printed by the launcher. For task notes, call bridge_status, save a checkpoint using revision zero, and read it back. For Filesystem, list approved directories and write/read one small test file. For a browser, read the project page in its own headless browser. A download receipt on its own is not a connection test.
3. Use one distinct job ID and workspace per chat. Before writing, read its last revision. Record completed work and a specific next step. If two chats choose the same revision, re-read and reconcile. A general desktop interface has one foreground input owner. Other chats can operate on independent files or isolated browser instances.
4. After a disconnect, test availability, read the checkpoint and inspect the actual output before repeating a write or download. Keep long work in the application that owns it. Closing a chat does not guarantee an action continues. For a file handoff carry only the job ID, last verified result and next step into the next chat.
5. To install the RDR2 translation, use Windows and confirm the intended folder contains RDR2.exe. Use the dedicated RDR2 filesystem launcher for the selected folder. Then use the [RDR2 installation instructions](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/uzstadisana/). Changing game files belongs to that installation task, not the bridge test.

Use the language guide and evidence table in this package. Distinguish a direct live connector, a private existing installation and a file exchange. Name the device, host, version and test boundary. Never count a desktop or another platform as an iPhone or Android test.

[Latviski](references/START-lv.md) · [English](references/START-en.md) · [Deutsch](references/START-de.md) · [日本語](references/START-ja.md) · [简体中文](references/START-zh.md) · [Русский](references/START-ru.md)

Give the owner the matching downloadable file first. If they only need a diagnosis or
their browser chat has no matching client, offer the ready-made browser file check.
A device's own approval dialog belongs to its owner. Never ask the owner to copy API
keys or grant access to another person's computer. Record the exact verified scope
before moving on to the game-specific installer.
