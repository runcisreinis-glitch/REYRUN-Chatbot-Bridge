# REYRUN ブリッジ：AI チャットをお使いの端末につなぐ

[Latviski](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/) · [English](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/) · [Deutsch](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/de/) · [日本語](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/) · [简体中文](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/zh/) · [Русский](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/)

## 起動ファイルを一つ渡す

このページのアドレスを受け取ったら、どの端末で作業するかを確かめます。まず、すでに許可された接続を確認します。設定が必要なら、その端末で使える起動ファイルを一つ渡します。公開済みのものが依頼に合わなければ、次の手順に沿ったスクリプトを一つ用意します。利用者に案内するのは、その時点で必要な次の操作だけです。

1. 現在の状態を確認します。依頼が済んでいれば、結果を確認して終了します。作業は許可されたフォルダー内で行います。
2. まずプロジェクトでサポートされている方法を使います。ダウンロードが一時的に途切れたら回数を限って再試行するか、同じ版の公式配布物を使います。実行前に所定のチェックサムか署名を照合します。書き込み権限がなければ、目的を達成できる場合に限り、対応するユーザーフォルダーを選びます。
3. ペアリング、ファイルの選択、システムの許可が必要なときは、何を承認するのかを説明し、所有者の判断を待ちます。拒否されたら停止します。ファイルを一つ渡す方法は、それで完了できる依頼にだけ使います。
4. 変更前に元の状態を復元できるよう保存します。中断後は実際のファイルを調べ、未完了の手順から再開します。再実行しても既存の設定とバックアップを残します。
5. チャットから実際に操作して結果を確認します。たとえば、許可されたフォルダー内で事前に中身を知らなかったファイルを読み、内容を照合します。結果か、残った具体的な問題を伝えます。ダウンロード、起動、システムの許可、クライアントの操作は別々に数えます。クリック回数を約束しません。

## 起動後に確認すること

Filesystem では list_allowed_directories で許可された作業フォルダーを確認し、そこだけにテストファイルを書いて読み戻します。内容が違えば中止します。Task Bridge では bridge_status、read_checkpoint の順に呼びます。初回の save_checkpoint は revision 0 を使います。切断後は同じタスク ID で read_checkpoint を呼びます。

チャットのAIにこのサイトを開く権限がないとき、リンクを開いてほしいと頼んでも断られたとき、エラーなどで開けないときは、手順書を直接渡せます。ファイルをダウンロードして、チャットに添付してください。

[手順書をダウンロード（.md）](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/download/REYRUN-Bridge-Instructions-ja.md)

## AI 用の手順と技術情報

## チャットで使えるスキル（skill）

ユーザーがこのページのアドレスだけを送ったら、チャットをその人のパソコンにつなぐ手順を案内してください。使える接続があれば利用します。OS が分からない場合だけ確認し、対応する起動ファイルか公式の手順を渡します。何を開き、どこで承認するかを示してください。このチャットが接続に対応していなければ、対応するクライアントを紹介してください。

[ZIP](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/download/REYRUN-Bridge-Skill-ja.zip) · [GitHub](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge)

Windows ではファイルを一つダウンロードして開きます。初めて ChatGPT につなぐときは、ブラウザーでも端末を確認します。すでに接続済みなら、そのままファイルについて質問できます。

## チャットに貼り付けるメッセージ

> このチャットを私のパソコンにつないでください。「ダウンロード」フォルダーにあるファイルを容量の大きい順に五つ挙げて、それぞれのサイズを教えてください。何も削除しないでください。REYRUN のスキルを使い、私の操作が必要なときは教えてください。 https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/ https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ai/ja.md

どの端末で作業しますか？

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/#device-windows) · [Mac · macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/#device-mac) · [Android](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/#device-android) · [iPhone · iPad](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/#device-iphone) · [Linux](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/#device-linux)

## 端末の接続方法

## Windows · パソコンのファイルを扱う

## ChatGPT · Desktop Commander Remote

Windows 用の公式ランチャーを開きます。ChatGPT で Remote Desktop Commander を接続し、サインインします。端末コードとターミナルのコードが一致したら承認し、ターミナルは開いたままにしてください。チャットで接続中の端末の一覧と、テストファイルの一行を読み出してもらいます。切断するには Ctrl+C を押します。

[Windows 用ランチャーをダウンロード →](https://mcp.desktopcommander.app/remote-windows.cmd) · [公式の設定手順 →](https://desktopcommander.app/help/devices/connect-computer) · [ChatGPT で接続 →](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

## Claude Desktop · REYRUN

Claude Desktop をインストールしたパソコンで REYRUN のランチャーをダウンロードして開きます。Claude Desktop を終了して開き直し、作業フォルダーにメモを作って、書いた内容を読み取るよう頼んでください。

[REYRUN · Windows →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd)

## Mac · macOS · パソコンのファイルを扱う

## ChatGPT · Desktop Commander Remote

公式手順の Mac 用コマンドをターミナルで実行します。ChatGPT で Remote Desktop Commander を接続し、サインインします。端末コードとターミナルのコードが一致したら承認し、ターミナルは開いたままにしてください。チャットで接続中の端末の一覧と、テストファイルの一行を読み出してもらいます。切断するには Ctrl+C を押します。

[公式の設定手順 →](https://desktopcommander.app/help/devices/connect-computer) · [ChatGPT で接続 →](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

## Claude Desktop · REYRUN

Claude Desktop が入った Mac でランチャーをダウンロードし、ZIP を展開して中の .command ファイルを開きます。Claude Desktop を再起動し、作業フォルダーにメモを書いて、その内容を読めるか試してください。

[REYRUN · macOS →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

## Android · タイマー、ファイル、メモ

## Google Gemini · Android

スマートフォンの Gemini に「5分のタイマーをセットして」と頼み、「時計」アプリで残り時間を確認します。設定できない場合は、接続済みアプリで Device assistance（旧 Utilities）が有効か確かめてください。

[Google Play · Gemini →](https://play.google.com/store/apps/details?id=com.google.android.apps.bard) · [Google のヘルプ →](https://support.google.com/gemini/answer/15235441)

## ChatGPT · Desktop Commander Remote

Android のファイルを扱うには、Termux を使う実験的な方法が開発元から案内されています。接続後に空き容量を聞いてみてください。操作範囲は Termux の権限内で、バックグラウンドでは Android が接続を止めることがあります。

[開発元の Android 向け手順 →](https://desktopcommander.app/help/devices/connect-android-phone)

## ほかのオンラインチャットを使う場合

チャットにメモやメールの下書きを書いてもらい、スマートフォンで内容を確認します。そのままファイルに保存するか、メールアプリで下書きを開けます。送信するのはご本人です。

[メモやメールを作成 →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/phone/) · [ファイルのチェックサムを確認 →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/start/)

## iPhone · iPad · リマインダーとメモ

## Claude · Apple Reminders

iPhone または iPad の Claude に、既存のリストに「REYRUN テスト」というリマインダーを追加するよう頼みます。確認が出たらアクセスを許可し、「リマインダー」で登録を確かめてください。許可は端末設定の Claude の項目で取り消せます。

[App Store · Claude →](https://apps.apple.com/app/id6473753684) · [Anthropic のヘルプ →](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)

## ほかのオンラインチャットを使う場合

チャットにメモやメールの下書きを書いてもらい、スマートフォンで内容を確認します。そのままファイルに保存するか、メールアプリで下書きを開けます。送信するのはご本人です。

[メモやメールを作成 →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/phone/) · [ファイルのチェックサムを確認 →](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/start/)

## Linux · パソコンのファイルを扱う

## ChatGPT · Desktop Commander Remote

公式手順の Linux 用コマンドをターミナルで実行します。ChatGPT で Remote Desktop Commander を接続し、サインインします。端末コードとターミナルのコードが一致したら承認し、ターミナルは開いたままにしてください。チャットで接続中の端末の一覧と、テストファイルの一行を読み出してもらいます。切断するには Ctrl+C を押します。

[公式の設定手順 →](https://desktopcommander.app/help/devices/connect-computer) · [ChatGPT で接続 →](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

## Claude Desktop をお使いの場合

Windows または Mac のランチャーを使うと、Claude Desktop から REYRUN の作業フォルダー一つにアクセスできます。Mac では ZIP 内の .command ファイルを開きます。その後 Claude Desktop を再起動してください。初回は OS が確認を求める場合があります。

[Windows 用ランチャーをダウンロード](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [Mac 用ランチャーをダウンロード](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) · [AI 用手順書（.zip）](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/download/REYRUN-Bridge-Skill-ja.zip)

## ブラウザーで ChatGPT をお使いですか？

[ChatGPT 用 Windows ランチャー](https://mcp.desktopcommander.app/remote-windows.cmd) · [Mac と Linux の設定](https://desktopcommander.app/help/devices/connect-computer) · [ChatGPT の接続設定を開く](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

Desktop Commander の案内に従ってパソコンを接続します。Windows、Mac、Linux に対応しています。ターミナルに「Device ready」と出れば、スマートフォンの ChatGPT からもそのパソコンのファイルを扱えます。スマートフォン自体の操作には上の Android または iPhone の手順を使います。

[Desktop Commander](https://desktopcommander.app/help/devices/connect-computer) · [無料プラン](https://desktopcommander.app/help/account-billing/plans-and-tool-call-limits)

## RDR2 にラトビア語訳を入れる

Windows のストーリーモード用です。検証済みの Universal RDR2 String Translator と Ultimate ASI Loader x64 9.7.4 がある場合はゲームを終了し、XML インストーラーをダウンロードして開きます。両プラグインのチェックサムを調べ、以前のラトビア語 XML をバックアップしてから翻訳を入れます。別の基礎翻訳やプラグインの不足が見つかると停止し、手順を表示します。

[ラトビア語 XML をインストール](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Install-XML.cmd) · [以前の XML に戻す](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Restore-XML.cmd)

ダウンロードした Windows ランチャーを開くと、Steam、Rockstar、Epic のライブラリでゲームを探し、検証済みのラトビア語ファイルを作業フォルダーに用意します。候補が複数あればお使いのフォルダーを選びます。その後、プラグイン、ローダー、バックアップ、ストーリーモードでの確認手順を AI に渡してください。

[RDR2 用ランチャーをダウンロード](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-rdr2-Windows.cmd) · [翻訳の導入手順を開く](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/ja/install/)

## そのほかの接続方法と検証結果

お使いの端末を選び、ツール名を開いてください。用途、検証した内容、資料を確認できます。

## 01. Filesystem MCP · 2.3.0

作業フォルダーのファイル · Windows · macOS · GitHub ★ 91 934

選んだフォルダーのファイルを AI が整理し、内容を変えずにコピーできます。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

検証結果 · Linux でサーバー 2.3.0 を検証しました。許可されたフォルダー一覧とファイル情報を読み、バイナリファイルを同じ内容でコピーできました。範囲外へのアクセスは拒否されました。Node のある Windows 機では設定に6.68秒かかり、作業フォルダー内で ラトビア語のメモを書き込み、同じ内容を読み戻せました。Windows でも作業フォルダーの外にあるファイルにはアクセスできませんでした。

2026年の利用報告 · 3月の利用報告では、コマンドラインで指定したフォルダーがクライアントの設定に置き換わりました。ここでは --confine-roots を使い、実際の許可リストを確認します。

並行作業 · 一つのフォルダーに書き込むチャットは一つにします。別のフォルダーには別の接続を使えます。

読み取り専用にするには --read-only を指定します。コピー先に同名のファイルがないか確認してください。copy_file は既存ファイルを上書きしません。ローカル接続がないチャットでは手順の案内を受けられます。

[Filesystem MCP · ツールとフォルダーの権限](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md)

[Filesystem 2.3.0 のリリース情報](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0)

[Windows・macOS のデスクトップ設定](https://modelcontextprotocol.io/docs/develop/connect-local-servers)

[許可されるフォルダーに関する利用報告 · 2026年3月16日](https://github.com/modelcontextprotocol/servers/issues/3602)

[GitHub · modelcontextprotocol/servers](https://api.github.com/repos/modelcontextprotocol/servers)

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/windows-filesystem.json)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 02. REYRUN Task Bridge · 1.0.0

作業記録 · Windows · macOS

作業の途中経過を保存すると、別のチャットに引き継げます。履歴はタスクごとに残ります。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-macOS.command.zip)

検証結果 · リガ時間1時11分、Node 24.19 の Windows 実機で検証しました。名前に空白を含むテストフォルダーでランチャーを2回実行しても以前の設定は残りました。一方のクライアントが保存した第1版をもう一方が読み、古い版からの更新は拒否されました。4クライアントで別々の4件を同時に保存でき、同じ記録を更新した場合は1件だけ成功しました。再起動後も全5件を読めました。

2026年の利用報告 · 11月12日（リガ時間）にプロジェクト内で検証。

並行作業 · 4クライアントが同時に動作し、再起動後も5件すべての記録が残っていました。

このプロファイルには作業記録を保存します。ファイルのコピーには Filesystem を使います。

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

[4 × stdio](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/parallel.json)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 03. Microsoft Playwright MCP · 0.0.85

独立したブラウザー · Windows · macOS · GitHub ★ 39 515

自分のサイトのボタンを探す、別ページに移る、表示内容を読むといった動作確認に使えます。タスクごとに新しいブラウザープロファイルを使えます。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-macOS.command.zip)

検証結果 · Windows と macOS の両方で、ランチャーが別の Chrome プロセスを開き、チャットにスクリーンショットを返しました。空白ページで、返された PNG を開けることも確認しました。

2026年の利用報告 · 日本の利用者がブラウザーのプロセスとログイン状態を別々に比較し、並行作業には独立したプロファイルを明示的に選ぶよう勧めています。

並行作業 · 並行するセッションごとに別のプロセスとプロファイルを使います。今回の検証は各 OS で1セッションずつです。

新しいプロファイルでは個人アカウントにログインしていません。標準ツールにはコード実行機能があります。開発元によると --allowed-origins だけではネットワークを完全には隔離できません。信頼できるテストサイトを選び、クライアント側のツール権限を確認してください。

[Microsoft リリース · 2026年11月9日](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.85)

[Microsoft · ブラウザープロファイルと設定](https://github.com/microsoft/playwright-mcp)

[開発元の Windows・macOS・Ubuntu 検証 · 11月11日](https://github.com/microsoft/playwright-mcp/actions/runs/43074928448)

[日本の利用者によるプロファイル比較 · 2026年6月29日](https://zenn.dev/ruri/articles/playwright-multi-session-isolation)

[GitHub · microsoft/playwright-mcp](https://api.github.com/repos/microsoft/playwright-mcp)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 04. Chrome DevTools MCP · 1.13.0

独立したブラウザー · Windows · macOS · GitHub ★ 55 113

見た目の確認に使えます。許可されたプロジェクトのページを限られたツールで開き、スクリーンショットを撮れます。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-macOS.command.zip)

検証結果 · Windows と macOS の両方で、ランチャーが別の Chrome プロセスを開き、チャットにスクリーンショットを返しました。空白ページで、返された PNG を開けることも確認しました。

2026年の利用報告 · macOS では、サーバーが異常終了したあともテスト用 Chrome が残ったという報告があります。中国の利用者は Debian での検証記録を公開し、未確認のモードを明記しています。

並行作業 · セッションごとに別の Chrome プロセスを使います。共通プロファイルではタブが混ざる場合があります。

このプロファイルは一時的なものです。すでに開いている個人用タブには別の接続方式が必要です。テストページに個人情報が表示されていれば画像にも映ります。セッションはクライアントで終了します。

[Chrome DevTools リリース · 2026年11月11日](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0)

[Chrome DevTools MCP · 設定](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md)

[開発元の Windows・macOS・Ubuntu テスト結果 · 11月11日](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43058501937)

[macOS の異常終了に関する報告 · 2026年8月26日](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/2621)

[中国の利用者の検証記録 · 2026年10月21日](https://friendlyai.top/projects/chrome-devtools-mcp/)

[その後のリリース前テスト · macOS・Node 22 でのエラー](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43105363963)

[GitHub · ChromeDevTools/chrome-devtools-mcp](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp)

[Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 05. Desktop Commander · リモート／ローカル

ファイル確認 · Windows · macOS · GitHub ★ 10 284

ファイルやターミナルをバックグラウンドで操作できます。ローカルランチャーには、一つの作業フォルダーを確認するためのツールが三つあります。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-macOS.command.zip)

検証結果 · 実機は Windows、バージョンは 0.3.0 でした。Reinis Bridge が作ったファイルを Desktop Commander が読み書きし、Reinis Bridge が書き換え後の22バイトを読み戻しました。共有ファイルで作業状況を渡せますが、会話履歴は別途引き継ぎます。公式のリモートツールはファイル、ターミナル、プロセスに対応します。この試験ではマウスやキーボードは使いませんでした。開発元は Windows、macOS、Linux を案内しています。

2026年の利用報告 · 2026年10月13日、Windows の 0.2.52 で start_process がコンソールを前面に出すとの報告がありました。11月3日には 0.3.1 で端末がオンラインでも約60秒でタイムアウトすることがあるという別の報告があります。今回のファイル受け渡しは成功しました。

並行作業 · 両ツール間でのファイル受け渡しを確認しました。1台に同時接続できるチャット数の上限は測っていません。

ランチャーにはローカルパッケージ 0.3.2 を使います。Remote 0.3.0 は端末のペアリングを行う別サービスです。画面のボタンなどはブラウザープロファイルで確認できます。

[ローカル版](https://github.com/wonderwhy-er/DesktopCommanderMCP)

[リモート版](https://github.com/desktop-commander/remote-desktop-commander)

[使い方](https://desktopcommander.app/help/getting-started/what-is-desktop-commander)

[コンソールウィンドウの報告](https://github.com/wonderwhy-er/DesktopCommanderMCP/issues/852)

[接続タイムアウトの報告](https://github.com/desktop-commander/remote-desktop-commander/issues/90)

## 06. Reinis Bridge · 1.0.0

専用デスクトップ · Windows

このプロジェクトの GitHub リポジトリは OpenBot 専用の Chrome セッションで作成しました。アプリを閉じたあとの端末側の記録で、ユーザーが操作しているデスクトップが変わっていないことを確かめました。

検証結果 · 11月12日リガ時間0時58分、既存の接続で短いバックグラウンド処理を2件実行し、5.011秒間重なりました。同じキーで再度要求すると完了済みの結果が返り、出力は保存位置から読み続けられました。

2026年の利用報告 · レイニスが実際に使った対話セッションは一つです。ターミナルのバックグラウンド処理は2件同時に動きました。二つのチャットによるデスクトップの同時操作は未検証です。

並行作業 · 対話用デスクトップは一つです。バックグラウンドの2件は5.011秒間並行して動作しました。

これはレイニス個人の Windows 接続です。公開ランチャーはご自身のパソコンの指定フォルダーにローカル接続を作ります。レイニスの専用ブリッジがインストールされたり、彼のパソコンにアクセスしたりすることはありません。

[REYRUN · Windows](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

## 07. Git worktree + bundle · Git CLI · 検証版 2.52.0

ファイルの引き継ぎ · Windows · macOS · GitHub ★ 64 269

常時接続がなくてもプロジェクトのファイルを引き継げます。タスクごとに作業コピーとブランチを分け、コミットした変更を bundle にまとめて別のパソコンへ移せます。

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-macOS.command.zip)

検証結果 · Linux で作業ツリーを二つ作り、一方の変更がもう一方に及ばないことを確認しました。bundle を検証し、同じコミットとバイト単位で同一のファイルを復元しました。

2026年の利用報告 · ドイツ語の実験記録では、別々のフォルダーで二つの作業を試し、ファイルを意図的に変更して両担当者の操作を再現しています。

並行作業 · 別々のブランチにある二つの作業コピーを検証しました。

作業ツリーは Git のオブジェクトを共有します。ブランチ全体の bundle には過去の履歴も含まれることがあります。人に渡す場合は選んだファイルだけのリポジトリを作ってください。この方法では端末やアプリ、マウスは操作できません。

[git worktree マニュアル](https://git-scm.com/docs/git-worktree)

[git bundle マニュアル](https://git-scm.com/docs/git-bundle)

[パソコン用 Git をダウンロード](https://git-scm.com/downloads)

[ドイツ語の二役による実験 · 2026年9月9日](https://www.bitblokes.de/ki-agenten-git-worktrees/)

[GitHub · git/git](https://api.github.com/repos/git/git)

## 08. REYRUN · Web Crypto

ファイルの受け渡し · Windows · macOS · Android · iOS

ブラウザーで用意済みのスクリプトを開き、タップして見本を確認します。自分のテキストファイルも選べます。

[サンプルを開く](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/start/)

検証結果 · Android 15 エミュレーターで公開サンプルを1回タップすると、WebView 124.0.6367.219 は13バイト・2行と想定どおりの SHA-256 を返しました。Chrome のプレビューと iOS 18.5・WebKit の iPhone SE シミュレーターでも同じ結果でした。非対応の操作は拒否されました。いずれも仮想端末での検証です。

2026年の利用報告 · この新しいサンプルについて、第三者の利用報告はまだ集まっていません。

並行作業 · 作業ごとにファイルや確認結果を分けます。スマートフォンの共有メニューで送れる操作は一度に一つです。

結果は1ファイル分です。エラーの説明が必要な場合は、該当する文章もチャットに渡してください。

[REYRUN](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/web/start)

[MDN · File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API)

[MDN · SubtleCrypto.digest](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest)

[Android 15 · WebView · 2026-11-11](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121791094/job/130863821353)

[iPhone SE · iOS 18.5 · WebKit](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121668999/job/130863410709)

## 09. LocalSend

ファイルの受け渡し · Windows · macOS · Android · iOS

用意したファイルを同じ Wi-Fi 上の別の端末に送れます。

[サンプルを開く](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/start/)

検証結果 · 実際の2台間の転送は今回試していません。mobile-request.json をもう一方の端末に送り、ID とハッシュ値をこのページの結果と照合してください。

2026年の利用報告 · 2026年6月25日、xueyexiao は Redmi K70 で LocalSend のファイル選択に権限がなくても、Android のファイル管理アプリの共有メニューから送れたと中国語で報告しました。

並行作業 · 作業ごとにファイルや確認結果を分けます。スマートフォンの共有メニューで送れる操作は一度に一つです。

両方の端末を接続し、それぞれで LocalSend を使います。ファイルと送信先を選んでください。

[LocalSend](https://localsend.org/download)

[2026年の変更履歴](https://localsend.org/changelog)

[xueyexiao · Redmi K70 · 中文](https://github.com/localsend/localsend/discussions/835)

[REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 10. Nextcloud Files

ファイルの受け渡し · Windows · macOS · Android · iOS

チャットが用意したファイルを Nextcloud フォルダーに保存し、パソコンで同じファイルを開けます。

[サンプルを開く](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/start/)

検証結果 · 今回は個人のサーバーには接続していません。もう一方の端末で受け取ったファイルの ID とハッシュ値を確認してください。

2026年の利用報告 · 2026年4月28日、Sanook は Android からの写真アップロードが待機状態になり、後から完了したとドイツ語で報告しました。この報告の対象は写真で、今回のテストファイルとは別のものです。

並行作業 · 作業ごとにファイルや確認結果を分けます。スマートフォンの共有メニューで送れる操作は一度に一つです。

すでにアカウントとフォルダーがある方に向いています。サーバーを新しく用意するには別に設定が必要です。

[Nextcloud](https://nextcloud.com/install/)

[iOS · 2026](https://github.com/nextcloud/ios/issues)

[Sanook · Android · Deutsch](https://help.nextcloud.com/t/android-client-warte-auf-hochladen/217584/18)

[REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 11. Termux

ローカルスクリプト · Android

Android の Termux 専用フォルダーで用意済みのスクリプトを試せます。

[Termux 用スクリプト](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-termux.sh)

検証結果 · Linux の sh で2回実行し、毎回別のフォルダーと期待どおりのハッシュ値を含む結果を得ました。Android 上での実行は今回の検証に含まれていません。

2026年の利用報告 · 2026年4月30日、slondr は Android 16 の Pixel 9a でファイル選択が止まると報告しました。同じスレッドで開発者は Samsung の端末2台で選択できたと述べています。

並行作業 · 作業ごとにファイルや確認結果を分けます。スマートフォンの共有メニューで送れる操作は一度に一つです。

Termux がすでに入っている場合に使ってください。通常のチャットからすぐ試すにはブラウザーのサンプルが使えます。

[Termux](https://github.com/termux/termux-app)

[Android 15 · #5150](https://github.com/termux/termux-app/issues/5150)

[Termux · インストール](https://github.com/termux/termux-app#installation)

[Termux:API](https://github.com/termux/termux-api)

[slondr · Pixel 9a · English](https://github.com/termux/termux-app/issues/5101)

## 12. Apple Shortcuts

ファイルの受け渡し · iOS · macOS

共有メニューから設定済みの Apple ショートカットへファイルを渡します。

[サンプルを開く](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/start/)

検証結果 · この一連の操作は iPhone 実機で試していません。保存した phone-test.txt を「ファイル」で開き、REYRUN-OK があるか確認します。

2026年の利用報告 · 2026年1月28日、anyprogram は iPhone と iPad で TXT ファイルを作成・保存するショートカットを公開しました。既存ファイルの編集モードでは選んだファイルを上書きします。

並行作業 · 作業ごとにファイルや確認結果を分けます。スマートフォンの共有メニューで送れる操作は一度に一つです。

ファイル入力を受け取るショートカットの設定が必要です。ブラウザーのサンプルはすぐに試せます。

[Apple · iPhone](https://support.apple.com/guide/shortcuts/launch-a-shortcut-from-another-app-apd163eb9f95/ios)

[Apple · ショートカットの共有](https://support.apple.com/guide/shortcuts/share-shortcuts-apdf01f8c054/ios)

[Apple · ショートカットユーザガイド](https://support.apple.com/guide/shortcuts/welcome/ios)

[anyprogram · iPhone/iPad · 日本語](https://qiita.com/anyprogram/items/6cc1394569c687ed506c)

[iPhone 16 Pro Max · 2026](https://github.com/net00-1/SW-DLT/issues/133)

[REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 13. Desktop Commander Remote · ChatGPT

連携アプリ · Windows · macOS · Linux

オンラインのチャットから接続済みパソコンのファイルを扱えます。

[設定手順を開く](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/#devices)

検証結果 · 開発元は Windows、macOS、Linux の手順を公開しています。

2026年の利用報告 · 開発元の資料。

並行作業 · この方法で同時に接続できるセッション数は測定していません。

接続するパソコン側でサービスを動かす必要があります。

[Desktop Commander Remote · ChatGPT](https://desktopcommander.app/help/devices/connect-computer)

## 14. Google Gemini · Device assistance

連携アプリ · Android

Gemini に頼んで、スマートフォンの「時計」アプリにタイマーを設定できます。

[設定手順を開く](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/#device-android)

検証結果 · Google が Android 版 Gemini アプリでの手順を案内しています。

2026年の利用報告 · 開発元の資料。

並行作業 · この方法で同時に接続できるセッション数は測定していません。

Android 版の Gemini アプリが必要です。

[Google Gemini · Device assistance](https://support.google.com/gemini/answer/15235441)

## 15. Claude · Apple Reminders

連携アプリ · iOS

iPhone または iPad の既存のリストにリマインダーを追加します。

[設定手順を開く](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ja/#device-iphone)

検証結果 · Anthropic の資料では、許可を得てリマインダーを作成する方法を説明しています。

2026年の利用報告 · 開発元の資料。

並行作業 · この方法で同時に接続できるセッション数は測定していません。

Claude のモバイルアプリと「リマインダー」へのアクセス許可が必要です。

[Claude · Apple Reminders](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)

## 別のチャットに作業を引き継ぐ

## 四つのチャットで同時に作業するには？

チャットごとに別のタスク ID とフォルダーを割り当てます。文章作成、比較、確認は分担できます。ゲームのインストール先を変更する担当は一つに絞ります。ブラウザーはセッションごとにプロファイルを分け、共有デスクトップのマウス操作は一度に1セッションとします。

## 接続が途切れたら？

新しいチャットに同じタスク ID を渡し、最後の記録と完成済みのファイルを確認してもらいます。コピーやダウンロードが途切れたら、やり直す前にファイルを調べてください。二つのチャットが同じ記録を変えた場合も、次の変更前に保存済みの版を読みます。

## チャットボットはどこまで操作できますか？

ファイル用ランチャーが開くのは REYRUN の作業フォルダー一つです。ゲーム用では選んだ RDR2 フォルダーも加わります。ブラウザーのサンプルには選んだファイル一つで十分です。ダウンロードしたファイルを初めて開くと、OS が確認を求める場合があります。予期しない確認画面が出た場合は、ブラウザーのサンプルを選べます。

## アプリのエラーを調べるには？

エラーログのコピーを REYRUN 作業フォルダーに置き、最後のエラーを読んで説明するよう頼みます。通常のウェブチャットなら該当部分だけを添付してください。ブラウザーのサンプルが報告するのはチェックサムと行数で、ログ本文は端末に残ります。

[AI 用の手順](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ai/ja.md) · [検証結果と出典](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/research)

## クライアントはどこから接続設定を読みますか？

Windows ではランチャーが %APPDATA%/Claude、Mac では ~/Library/Application Support/Claude を調べます。claude_desktop_config.json をバックアップし、選んだ reyrun-… の項目だけを追加します。クライアントがないときは START.txt にブラウザーのサンプルが案内されます。ほかの対応 MCP クライアントには生成された runtime/reyrun-…-client.json を使えます。実行ファイルのパスはこの端末用です。

## 作業の引き継ぎ例

最後に確認した結果と次の作業を一つ記録します。同じローカルプロファイルなら、次のチャットは同じタスク ID で read_checkpoint を呼べます。通常のチャットには記録を貼り付け、必要なファイルを添付してください。ゲーム画面と承認画面を操作するのは一つのセッションだけにします。

```json
{
  "name": "save_checkpoint",
  "arguments": {
    "job": "game-check",
    "revision": 0,
    "done": "テストファイルを読み戻し、元の内容と一致することを確認しました。",
    "next": "選択されたゲームフォルダーを確認してください。"
  }
}
```
