# Guide for AI · REYRUN Bridge

[Latviski](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/) · [English](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/) · [Русский](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/)

[Download Windows launcher](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [Download Mac launcher](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) · [Try it on a phone or in a browser](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/start/)

Download and open the file. It connects a workspace to an existing Claude Desktop installation. Fully quit and reopen the app when convenient. For an ordinary web chat, try the browser sample. On Mac open the .command file inside the ZIP. Your system may show its own first-use confirmation.

## Using ChatGPT on the web?

[Windows launcher for ChatGPT](https://mcp.desktopcommander.app/remote-windows.cmd) · [Open the ChatGPT connector](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

For ChatGPT to work with Windows files, start with Desktop Commander’s official launcher. If your computer is already paired, open the connector and ask it to read one test file. On first use, verify your device code in your account. In November 2026 the free plan includes 10,000 tool calls per month. [Desktop Commander](https://desktopcommander.app/help/devices/connect-computer) · [Free plan](https://desktopcommander.app/help/account-billing/plans-and-tool-call-limits)

## Checks after opening the launcher

For Filesystem, call list_allowed_directories. Write one test file in the returned workspace and read it back. If the contents differ, stop the installation. For Task Bridge call bridge_status, then read_checkpoint. Use revision 0 for the first save_checkpoint. After a disconnect, call read_checkpoint with the same job ID.

## 1. Filesystem MCP · 2.3.0

Windows, macOS. Best for files in a selected job folder. An AI assistant can organize the project and copy files without changing their bytes.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

**Test result.** We ran the actual 2.3.0 server on Linux. It listed the allowed folders, read file metadata, copied binary data intact and refused access outside the selected folders. On a physical Windows PC with Node already present a fresh install took 6.68 seconds. A Unicode note survived a write/read round trip and access outside the workspace was refused.

**2026 field notes.** A March user report showed client roots replacing command-line choices. This recipe uses --confine-roots and checks the effective list.

For a read-only session add --read-only. Check whether the destination exists before copying. The copy_file tool refuses to overwrite an existing file. Browser-only chats without a local connection can guide the user.

**Parallel work.** Assign one writer per folder. Separate folders can use separate connections.

[Filesystem MCP · tools and directory rules](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md) · [Filesystem 2.3.0 release](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) · [Desktop client setup for Windows and macOS](https://modelcontextprotocol.io/docs/develop/connect-local-servers) · [User report on effective roots, 16 March 2026](https://github.com/modelcontextprotocol/servers/issues/3602) · [GitHub · modelcontextprotocol/servers](https://api.github.com/repos/modelcontextprotocol/servers) · [Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/windows-filesystem.json) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 2. REYRUN Task Bridge · 1.0.0

Windows, macOS. Pass an exact stopping point to your next chat. Each job has its own revision history.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-macOS.command.zip)

**Test result.** Physical Windows PC, Node 24.19, 01:11 Riga time. Two launcher runs configured the connection in test folders with spaces in their names, preserving the original setting. One client process saved revision 1. Another read it. A stale write was refused. Four simultaneous local clients saved four separate jobs. One of four writers won the shared record. A fresh process recovered all five jobs.

**2026 field notes.** Project test on 12 November (Riga).

This profile stores job notes. Choose Filesystem for copying files.

**Parallel work.** Four concurrent clients and five recovered jobs tested.

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json) · [4 × stdio](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/parallel.json) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 3. Microsoft Playwright MCP · 0.0.85

Windows, macOS. Best for testing your own web project when you need to find controls, navigate or inspect readable page content. Each job can have a fresh browser profile.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-macOS.command.zip)

**Test result.** On both Windows and macOS our launcher opened a separate Chrome process and returned a screenshot to the chat client. The test decoded the actual PNG pixels. The page used in this check was blank.

**2026 field notes.** A Japanese hands-on comparison tested browser processes and sign-in state separately. The author recommends explicitly selecting isolated profiles for parallel jobs.

The new profile starts without your personal sign-in. The default tool list includes code execution. The project says --allowed-origins is not a complete network boundary. Use a trusted test site and client-side tool permissions.

**Parallel work.** Use a separate process and profile per concurrent browser session. Our check opened one per operating system.

[Microsoft release · 9 November 2026](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.85) · [Microsoft · browser profiles and documented options](https://github.com/microsoft/playwright-mcp) · [Author tests on Windows, macOS and Ubuntu · 11 November](https://github.com/microsoft/playwright-mcp/actions/runs/43074928448) · [Japanese first-person profile comparison · 29 June 2026](https://zenn.dev/ruri/articles/playwright-multi-session-isolation) · [GitHub · microsoft/playwright-mcp](https://api.github.com/repos/microsoft/playwright-mcp) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 4. Chrome DevTools MCP · 1.13.0

Windows, macOS. Choose it for visual checks. A restricted tool set can navigate to an approved project page and take a screenshot.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-macOS.command.zip)

**Test result.** On both Windows and macOS our launcher opened a separate Chrome process and returned a screenshot to the chat client. The test decoded the actual PNG pixels. The page used in this check was blank.

**2026 field notes.** A macOS user reported a test Chrome process persisting after abnormal server termination. A Chinese practitioner separately published a Debian test log and identified the modes they did not test.

This profile is temporary. Existing personal tabs belong to a different connection mode. Screenshots can contain private data displayed on the test page. Stop the session through the client.

**Parallel work.** Each session has its own Chrome process. A shared profile can mix up tabs.

[Chrome DevTools release · 11 November 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0) · [Chrome DevTools MCP · configuration](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md) · [Upstream Windows/macOS/Ubuntu test matrix · 11 November](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43058501937) · [macOS report about abrupt termination · 26 August 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/2621) · [Chinese practitioner’s test log · 21 October 2026](https://friendlyai.top/projects/chrome-devtools-mcp/) · [Later upstream pre-release run · macOS/Node 22 failure](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43105363963) · [GitHub · ChromeDevTools/chrome-devtools-mcp](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 5. Desktop Commander · Remote / Local

Windows, macOS. Use files and terminal sessions in the background. Our local launcher offers three inspection tools in one workspace.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-macOS.command.zip)

**Test result.** The Windows device reported version 0.3.0. Desktop Commander read a sample file created through Reinis Bridge, then wrote a replacement. Reinis Bridge read back all 22 bytes. A shared file can carry a checkpoint. It does not transfer the conversations themselves. The official remote tools cover files, the terminal and process sessions. Our file operations used no mouse or keyboard. The vendor lists Windows, macOS and Linux. This physical test used Windows.

**2026 field notes.** On 13 October 2026 a Windows user running 0.2.52 reported that start_process brought console windows to the foreground. On 3 November a user running 0.3.1 reported intermittent timeouts of about 60 seconds while their device still appeared online. These are individual reports. Our file handoff succeeded.

The launcher uses local package 0.3.2. Remote 0.3.0 is a separate, paired service. Use a browser profile to inspect graphical controls.

**Parallel work.** File handoff between two tools was tested. The maximum live-chat count per device was not measured.

[local](https://github.com/wonderwhy-er/DesktopCommanderMCP) · [remote](https://github.com/desktop-commander/remote-desktop-commander) · [help](https://desktopcommander.app/help/getting-started/what-is-desktop-commander) · [reportFocus](https://github.com/wonderwhy-er/DesktopCommanderMCP/issues/852) · [reportTimeout](https://github.com/desktop-commander/remote-desktop-commander/issues/90)

## 6. Reinis Bridge · 1.0.0

Windows. The project’s GitHub repository was created in an isolated OpenBot Chrome session. Afterwards the private app closed. Its local close receipt confirmed that the user’s input desktop stayed the same.



**Test result.** At 00:58 Riga time on 12 November, two short background jobs ran on the existing bridge. Their execution windows overlapped for 5.011 seconds. Repeating the second request with its original key returned the completed job. Saved output offsets allow a client to resume reading.

**2026 field notes.** Reinis has experienced one interactive stream. We measured two concurrent background terminal jobs. Simultaneous desktop control from two separate chats was not tested.

This is Reinis’s personal Windows bridge. The Windows launcher in this project creates your own local connection to a folder you select. It does not install his private bridge or grant access to his PC.

**Parallel work.** One interactive desktop. Two observed background jobs overlapped by 5.011 seconds.

[REYRUN · Windows](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

## 7. Git worktree + bundle · Git CLI · tested 2.52.0

Windows, macOS. Use for handing project files between sessions without a live connection. Each job gets a separate checkout and branch. A bundle carries the committed changes to another computer.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-macOS.command.zip)

**Test result.** On Linux we made two worktrees, changed one and confirmed the other was untouched. We verified the bundle and cloned the same commit and file bytes from it.

**2026 field notes.** A German practical test checked two jobs in separate folders. The authors simulated the workers through controlled file changes.

Worktrees share the Git object store. A full branch bundle may include its earlier history. For sharing, create a dedicated repository containing only selected files. This route does not give control over the device, apps or mouse.

**Parallel work.** Two working copies tested, each on its own branch.

[Git worktree manual](https://git-scm.com/docs/git-worktree) · [Git bundle manual](https://git-scm.com/docs/git-bundle) · [Git desktop downloads](https://git-scm.com/downloads) · [German practical two-role experiment · 9 September 2026](https://www.bitblokes.de/ki-agenten-git-worktrees/) · [GitHub · git/git](https://api.github.com/repos/git/git)

## 8. REYRUN · Web Crypto

Windows, macOS, Android, iOS. Open a ready-made browser script and check the sample with one tap or pick a text file.

[Open the ready-made sample](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/start/)

**Test result.** On the Android 15 emulator a single screen tap processed the unchanged public sample. WebView 124.0.6367.219 returned 13 bytes, two lines and the expected SHA-256. A Chrome preview gave the same result. In an iPhone SE simulator running iOS 18.5 and WebKit the sample button gave the same result. An unsupported action was rejected. These runs used simulated devices.

**2026 field notes.** We have no independent user reports about this new demo yet.

This is a receipt for one file. Share a relevant excerpt separately if you want the chat to interpret an error.

**Parallel work.** Give each job its own file or receipt. One action uses the phone share sheet at a time.

[REYRUN](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/web/start) · [MDN · File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API) · [MDN · SubtleCrypto.digest](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest) · [Android 15 · WebView · 2026-11-11](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121791094/job/130863821353) · [iPhone SE · iOS 18.5 · WebKit](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121668999/job/130863410709)

## 9. LocalSend

Windows, macOS, Android, iOS. Send the prepared file to another device on your Wi-Fi.

[Open the ready-made sample](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/start/)

**Test result.** We did not test a two-device transfer here. Send mobile-request.json to the other device and compare the receipt ID and digest with our page.

**2026 field notes.** On 25 June 2026 xueyexiao reported in Chinese that sharing from the Android file manager worked on a Redmi K70 when the LocalSend picker lacked access.

Needs two connected devices with LocalSend. Choose the file and the recipient.

**Parallel work.** Give each job its own file or receipt. One action uses the phone share sheet at a time.

[LocalSend](https://localsend.org/download) · [2026 · Changelog](https://localsend.org/changelog) · [xueyexiao · Redmi K70 · 中文](https://github.com/localsend/localsend/discussions/835) · [REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 10. Nextcloud Files

Windows, macOS, Android, iOS. Save a file prepared by the chat to your Nextcloud folder and pick it up on your computer.

[Open the ready-made sample](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/start/)

**Test result.** We did not connect a private server. Verify the ID and digest of the file fetched on the second device.

**2026 field notes.** On 28 April 2026 Sanook described a queued Android photo upload in German. It finished later. Their observation concerned a photo.

Choose it if you already have an account and folder. Setting up a new server is a separate task.

**Parallel work.** Give each job its own file or receipt. One action uses the phone share sheet at a time.

[Nextcloud](https://nextcloud.com/install/) · [iOS · 2026](https://github.com/nextcloud/ios/issues) · [Sanook · Android · Deutsch](https://help.nextcloud.com/t/android-client-warte-auf-hochladen/217584/18) · [REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 11. Termux

Android. Check a ready-made script in Termux’s private directory on Android.

[Ready-made Termux script](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-termux.sh)

**Test result.** Run twice with sh on Linux. Each run created a separate folder and receipt with the expected digest. Execution on Android was not tested here.

**2026 field notes.** On 30 April 2026 slondr reported a stuck file picker on a Pixel 9a with Android 16. A project developer reported working selection on two Samsung phones in the same thread.

Use with Termux already installed. The browser sample is the quick start from a plain chat.

**Parallel work.** Give each job its own file or receipt. One action uses the phone share sheet at a time.

[Termux](https://github.com/termux/termux-app) · [Android 15 · #5150](https://github.com/termux/termux-app/issues/5150) · [Termux · Installation](https://github.com/termux/termux-app#installation) · [Termux:API](https://github.com/termux/termux-api) · [slondr · Pixel 9a · English](https://github.com/termux/termux-app/issues/5101)

## 12. Apple Shortcuts

iOS, macOS. Pass a file to an existing Apple shortcut through the share sheet.

[Open the ready-made sample](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/start/)

**Test result.** We did not run this sequence on a physical iPhone. Open the saved phone-test.txt in Files and verify that it reads REYRUN-OK.

**2026 field notes.** On 28 January 2026 Japanese author anyprogram documented an iPhone/iPad shortcut for creating and saving TXT files. Its edit-existing mode overwrites the selected file.

Requires an existing shortcut configured to accept files. The browser sample is ready to try immediately.

**Parallel work.** Give each job its own file or receipt. One action uses the phone share sheet at a time.

[Apple · iPhone](https://support.apple.com/guide/shortcuts/launch-a-shortcut-from-another-app-apd163eb9f95/ios) · [Apple · Share](https://support.apple.com/guide/shortcuts/share-shortcuts-apdf01f8c054/ios) · [Apple · Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios) · [anyprogram · iPhone/iPad · 日本語](https://qiita.com/anyprogram/items/6cc1394569c687ed506c) · [iPhone 16 Pro Max · 2026](https://github.com/net00-1/SW-DLT/issues/133) · [REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## Install RDR2 in Latvian

For Story Mode on Windows. If your game already has the tested builds of Universal RDR2 String Translator and Ultimate ASI Loader x64 9.7.4, close the game, download the XML installer and open it. It checks both plug-ins by checksum, saves a copy of any previous Latvian XML and installs the verified translation. If it finds a different base translation or a missing plug-in, it stops and gives you the installation guide.

[Install Latvian XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Install-XML.cmd) · [Restore previous XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Restore-XML.cmd)

Download and open the Windows launcher. It looks for the game in Steam, Rockstar and Epic libraries and stages a verified Latvian translation file in the workspace. If several folders match, you choose the right one. Give your AI the installer guide for the plug-in, loader, backup and Story Mode check. [Open translation instructions](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/install/)

## How can four chats work at once?

Give each chat its own job ID and folder. Text, comparisons and checks can run separately. Assign one chat to change a game installation. Give each browser session its own profile. Only one session controls the pointer on a shared desktop.

## What if the connection drops?

Give the new chat the same job ID. Ask it to read the last checkpoint and inspect files already written. After a timeout, look up the existing job first. Retry a download or copy only after checking whether it finished. If two chats try to save the same revision, read the winner before writing again.

## What access does the chatbot get?

The file launcher exposes one REYRUN workspace. The game launcher adds the selected RDR2 folder. The browser sample only needs the file you select. Your system may ask you to allow a downloaded file to open. You can choose the browser sample if an unexpected request appears.

## How can I diagnose an app problem?

Put a copy of the app’s error log in the REYRUN workspace. Ask your AI to read the last error and explain it. With a plain web chat, attach just the relevant text excerpt. The browser sample reports the checksum and line count. The log text stays on the device.

## Where does the client read its connection?

On Windows the ready-made launcher looks for an existing Claude Desktop profile in %APPDATA%/Claude. On Mac it uses ~/Library/Application Support/Claude. It adds the selected reyrun-… entry to claude_desktop_config.json and backs up the existing file before changing it. If the client is absent, START.txt gives the browser sample. For another compatible local MCP client, use the generated runtime/reyrun-…-client.json. Its executable path belongs to this computer.

## Example of a handoff

Save the last verified result and one next action. A new chat connected to the same local profile can call read_checkpoint with the same job. For a regular web chat, paste the checkpoint and attach the needed file. Give one session control of the game window and permission prompts.


```json
{
  "name": "save_checkpoint",
  "arguments": {
    "job": "game-check",
    "revision": 0,
    "done": "Test note read back exactly.",
    "next": "Verify the selected game folder."
  }
}
```
