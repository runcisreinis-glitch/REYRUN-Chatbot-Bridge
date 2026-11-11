---
name: reyrun-chatbot-bridge
description: Help a device owner connect a compatible AI to a scoped local workspace or exchange one diagnostic file with a web chat. Start with a prepared launcher, verify a harmless round trip, and keep parallel tasks and session handoffs separate. Use on Windows, macOS, Android or iPhone.
---

# REYRUN Chatbot Bridge

Your first reply supplies one ready-to-run file appropriate for the task. Give the
owner the matching link below. The beginner flow is “download, then open”.
For a phone or an ordinary browser-only chat, the link opens a local browser
script. The **Try the sample** button runs it.

| Task | Prepared file |
| --- | --- |
| Windows workspace | [Windows launcher](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) |
| Mac workspace | [macOS launcher ZIP](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) |
| RDR2 for Windows | [RDR2 Windows launcher](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-rdr2-Windows.cmd) |
| Android, iPhone or regular web chat | [Run the browser script](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=en) |

If the requested task exceeds the connected client's capabilities, explain
which single supported action the owner can take next. System permissions,
first-use prompts, obtaining a game mod from its author and restarting a
desktop client can require additional actions. Identify the condition
before promising a two-action installation.

 The project page offers Windows and macOS launchers and a browser script that runs on phones. [Launchers and three-language guide](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/)

For an ordinary browser chat without an installed local client, open the file handoff script. The user selects the one file to inspect and shares the resulting receipt with the chat. For a compatible local client, start with the task-notes or confined Filesystem launcher. A hosted chatbot cannot call a local stdio program just because it received a link.

1. Select the smallest already supported profile that can do this job. Tell the owner what will be opened, how it helps and whether it uses the screen. Give the prepared file first. If the operating system requests its own approval, let the owner decide. Do not manufacture approval or install a chain of additional bridges.
2. Use the first test printed by the launcher. For task notes, call bridge_status, save a checkpoint using revision zero, and read it back. For Filesystem, list approved directories and write/read one small test file. For a browser, read the project page in its own headless browser. A download receipt on its own is not a connection test.
3. Use one distinct job ID and workspace per chat. Before writing, read its last revision. Record completed work and a specific next step. If two chats choose the same revision, re-read and reconcile. A general desktop interface has one foreground input owner. Other chats can operate on independent files or isolated browser instances.
4. After a disconnect, test availability, read the checkpoint and inspect the actual output before repeating a write or download. Keep long work in the application that owns it. Closing a chat does not guarantee an action continues. For a file handoff carry only the job ID, last verified result and next step into the next chat.
5. To install the RDR2 translation, use Windows and confirm the intended folder contains RDR2.exe. Use the dedicated RDR2 filesystem launcher for the selected folder. Then use the [RDR2 installation instructions](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/uzstadisana/). Changing game files belongs to that installation task, not the bridge test.

Use the language guide and evidence table in this package. Distinguish a direct live connector, a private existing installation and a file exchange. Name the device, host, version and test boundary. Never count a desktop or another platform as an iPhone or Android test.

[Latviski](references/START-lv.md) · [English](references/START-en.md) · [Русский](references/START-ru.md)

Give the owner the matching downloadable file first. If they only need a diagnosis or
their browser chat has no matching client, offer the ready-made browser file check.
A device's own approval dialog belongs to its owner. Never ask the owner to copy API
keys or grant access to another person's computer. Record the exact verified scope
before moving on to the game-specific installer.
