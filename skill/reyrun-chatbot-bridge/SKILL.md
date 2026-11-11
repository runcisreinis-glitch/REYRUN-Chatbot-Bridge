---
name: reyrun-chatbot-bridge
description: Help a device owner connect a compatible AI to a scoped local workspace or exchange one diagnostic file with a web chat. Start with a prepared launcher, verify a harmless round trip, and keep parallel tasks and session handoffs separate. Use on Windows, macOS, Android or iPhone.
---

# REYRUN Chatbot Bridge

Start by giving the owner one direct launcher for the right device. The project page offers Windows and macOS launchers and a browser script that runs on phones. [Launchers and three-language guide](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/)

For an ordinary browser chat without an installed local client, open the file handoff script. The user selects the one file to inspect and shares the resulting receipt with the chat. For a compatible local client, start with the task-notes or confined Filesystem launcher. A hosted chatbot cannot call a local stdio program just because it received a link.

1. Select the smallest already supported profile that can do this job. Tell the owner what will be opened, how it helps and whether it uses the screen. Give the prepared file first. If the operating system requests its own approval, let the owner decide. Do not manufacture approval or install a chain of additional bridges.
2. Use the first test printed by the launcher. For task notes, call bridge_status, save a checkpoint using revision zero, and read it back. For Filesystem, list approved directories and write/read one small test file. For a browser, read the project page in its own headless browser. A download receipt on its own is not a connection test.
3. Use one distinct job ID and workspace per chat. Before writing, read its last revision. Record completed work and a specific next step. If two chats choose the same revision, re-read and reconcile. A general desktop interface has one foreground input owner. Other chats can operate on independent files or isolated browser instances.
4. After a disconnect, test availability, read the checkpoint and inspect the actual output before repeating a write or download. Keep long work in the application that owns it. Closing a chat does not guarantee an action continues. For a file handoff carry only the job ID, last verified result and next step into the next chat.
5. To install the RDR2 translation, use Windows and confirm the intended folder contains RDR2.exe. Use the dedicated RDR2 filesystem launcher for the selected folder. Then use the [RDR2 installation instructions](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/uzstadisana/). Changing game files belongs to that installation task, not the bridge test.

Use the language guide and evidence table in this package. Distinguish a direct live connector, a private existing installation and a file exchange. Name the device, host, version and test boundary. Never count a desktop or another platform as an iPhone or Android test.
