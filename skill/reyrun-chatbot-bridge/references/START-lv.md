# Instrukcija MI · REYRUN Tilts

[Latviski](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/) · [English](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/) · [Русский](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/)

[Lejupielādēt Windows palaidēju](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [Lejupielādēt Mac palaidēju](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) · [Izmēģināt telefonā vai pārlūkā](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/)

Gatavais failu palaidējs pieslēdz vienu darba mapi jau uzstādītai Claude Desktop lietotnei. Pēc palaidēja atvēršanas pilnībā aizver un vēlreiz atver Claude Desktop. Mac datorā atver arhīvā esošo .command failu. Pirmajā reizē sistēma var parādīt savu apstiprinājumu.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/#device-windows) · [Mac · macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/#device-mac) · [Android](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/#device-android) · [iPhone · iPad](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/#device-iphone) · [Linux](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/#device-linux)

[Piezīme vai e-pasts telefonā](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/phone/)

## Vai lieto ChatGPT pārlūkā?

[Windows palaidējs ChatGPT](https://mcp.desktopcommander.app/remote-windows.cmd) · [Atvērt ChatGPT savienotāju](https://chatgpt.com/apps/remote-desktop-commander/asdk_app_6a057d268ebc81919918d37eec718425)

Piesaisti savu Windows, Mac vai Linux datoru, sekojot Desktop Commander pamācībai. Kad terminālī redzi “Device ready”, ChatGPT var strādāt ar šī datora failiem arī tad, kad pats čatu atver telefonā. Lai veiktu darbību pašā telefonā, augstāk izvēlies Android vai iPhone. [Desktop Commander](https://desktopcommander.app/help/devices/connect-computer) · [Bezmaksas plāns](https://desktopcommander.app/help/account-billing/plans-and-tool-call-limits)

## Pārbaudes pēc palaidēja atvēršanas

Files lietotnē izsauc list_allowed_directories. Izveido testa failu tikai parādītajā darba mapē un nolasi tā saturu. Ja rezultāts nesakrīt, neveic instalāciju. Task Bridge profilā izsauc bridge_status, pēc tam read_checkpoint. Pirms pirmās save_checkpoint izmanto revision 0. Pēc savienojuma pārrāvuma izsauc read_checkpoint ar to pašu darba nosaukumu.

## 1. Filesystem MCP · 2.3.0

Windows, macOS. Vislabāk der failu sagatavošanai vienā darba mapē. MI palīgs var sakārtot projektu un pārkopēt failus, saglabājot to baitus.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

**Pārbaude.** Linux testa vidē palaidām īsto 2.3.0 serveri. Tas parādīja atļautās mapes, nolasīja faila informāciju, precīzi pārkopēja bināru failu un atteica piekļuvi ārpus izvēlētajām mapēm. Uz fiziska Windows datora svaiga uzstādīšana ar esošu Node aizņēma 6,68 sekundes. Latviešu teksta fails tika ierakstīts un precīzi nolasīts. Piekļuve ārpus darba mapes tika atteikta.

**2026. gada pieredze.** Martā lietotājs ziņoja, ka klienta norādītās mapes aizstāja komandrindas sarakstu. Šeit lietojam --confine-roots un pārbaudām faktisko atļauju sarakstu.

Vienai lasīšanas sesijai pievieno --read-only. Kopējot esošu failu, vispirms pārbaudi, vai mērķis jau pastāv. copy_file nepieļauj pārrakstīšanu. Parasts čats bez vietēja savienojuma dod norādes spēlētājam.

**Vienlaicīgs darbs.** Vienas mapes rakstīšanu uztici vienam čatam. Atsevišķām mapēm var izmantot atsevišķus savienojumus.

[Filesystem MCP · tools and directory rules](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md) · [Filesystem 2.3.0 release](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) · [Desktop client setup for Windows and macOS](https://modelcontextprotocol.io/docs/develop/connect-local-servers) · [User report on effective roots, 16 March 2026](https://github.com/modelcontextprotocol/servers/issues/3602) · [GitHub · modelcontextprotocol/servers](https://api.github.com/repos/modelcontextprotocol/servers) · [Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/windows-filesystem.json) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 2. REYRUN Task Bridge · 1.0.0

Windows, macOS. Nodod nākamajam čatam precīzi to vietu, kur darbs apstājās. Katram darbam ir sava pierakstu vēsture.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-macOS.command.zip)

**Pārbaude.** Windows dators, Node 24.19, plkst. 01.11 Rīgā. Palaidējs divreiz pareizi sagatavoja savienojumu testa mapēs ar atstarpēm nosaukumā un saglabāja iepriekšējo iestatījumu. Viens klienta process ierakstīja 1. redakciju. Otrs to nolasīja. Mēģinājums rakstīt pāri no vecākas redakcijas tika noraidīts. Četri vienlaicīgi lokāli klienti saglabāja četrus atsevišķus darbus. Kopīgajā ierakstā uzvarēja viens no četriem. Pēc restartēšanas varēja nolasīt visus piecus darbus.

**2026. gada pieredze.** Projekta paša 12. novembra pārbaude.

Šis profils glabā darba pierakstus. Failu pārkopēšanai izvēlies Filesystem.

**Vienlaicīgs darbs.** Pārbaudīti četri vienlaicīgi klienti un pieci atgūti darbi.

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json) · [4 × stdio](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/parallel.json) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 3. Microsoft Playwright MCP · 0.0.85

Windows, macOS. Vislabāk der sava projekta tīmekļa pārbaudēm, kad jāatrod poga, jāpāriet uz nākamo lapu vai jāpārbauda salasāmība. Katram darbam var būt savs pārlūka profils.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-macOS.command.zip)

**Pārbaude.** Mūsu Windows un macOS pārbaudēs palaidējs atvēra atsevišķu Chrome procesu un nosūtīja čata klientam ekrānattēlu. Pārbaude atspieda reālos PNG pikseļus. Šajā testā pārlūkā bija tukša lapa.

**2026. gada pieredze.** Japāņu praktiskajā salīdzinājumā autors atsevišķi pārbaudīja pārlūka procesu un pieteikšanās stāvokli. Paralēliem darbiem viņš iesaka skaidri izvēlēties izolētu profilu.

Profils sākas bez tavas personiskās pieteikšanās. Standarta rīku saraksts ietver arī koda izpildi. --allowed-origins pats par sevi negarantē pilnīgu tīkla izolāciju. Izmanto savu uzticamu testa vietni un klienta rīku atļaujas.

**Vienlaicīgs darbs.** Katrai vienlaicīgai sesijai savs pārlūka process un profils. Mūsu pārbaudē atvērts viens vienā operētājsistēmā.

[Microsoft release · 9 November 2026](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.85) · [Microsoft · browser profiles and documented options](https://github.com/microsoft/playwright-mcp) · [Author tests on Windows, macOS and Ubuntu · 11 November](https://github.com/microsoft/playwright-mcp/actions/runs/43074928448) · [Japanese first-person profile comparison · 29 June 2026](https://zenn.dev/ruri/articles/playwright-multi-session-isolation) · [GitHub · microsoft/playwright-mcp](https://api.github.com/repos/microsoft/playwright-mcp) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 4. Chrome DevTools MCP · 1.13.0

Windows, macOS. Izvēlies vienkāršai vizuālai pārbaudei. Ierobežots rīku komplekts var atvērt atļauto projekta lapu un uzņemt tās ekrānattēlu.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-macOS.command.zip)

**Pārbaude.** Mūsu Windows un macOS pārbaudēs palaidējs atvēra atsevišķu Chrome procesu un nosūtīja čata klientam ekrānattēlu. Pārbaude atspieda reālos PNG pikseļus. Šajā testā pārlūkā bija tukša lapa.

**2026. gada pieredze.** macOS lietotājs ziņoja, ka pēc servera avārijas var palikt atvērts testa Chrome process. Ķīniešu autors atsevišķi aprakstīja praktisku pārbaudi Debian vidē un precīzi norādīja neizmēģinātās iespējas.

Šis profils ir īslaicīgs. Lai izmantotu jau atvērtu personisko cilni, būtu jāizvēlas cits režīms. Attēlos var būt privāti dati no pašas testa lapas. Aizver sesiju ar klienta apturēšanas darbību.

**Vienlaicīgs darbs.** Katrā sesijā savs Chrome process. Kopīgs pārlūka profils sajauktu cilnes.

[Chrome DevTools release · 11 November 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0) · [Chrome DevTools MCP · configuration](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md) · [Upstream Windows/macOS/Ubuntu test matrix · 11 November](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43058501937) · [macOS report about abrupt termination · 26 August 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/2621) · [Chinese practitioner’s test log · 21 October 2026](https://friendlyai.top/projects/chrome-devtools-mcp/) · [Later upstream pre-release run · macOS/Node 22 failure](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43105363963) · [GitHub · ChromeDevTools/chrome-devtools-mcp](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp) · [Windows + macOS · CI](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43119957278)

## 5. Desktop Commander · Remote / Local

Windows, macOS. Fonā strādā ar failiem un termināļa sesijām. Šejienes lokālais palaidējs dod čatam trīs rīkus vienas darba mapes apskatei.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-macOS.command.zip)

**Pārbaude.** Windows ierīce ziņoja versiju 0.3.0. Desktop Commander nolasīja caur Reinis Bridge izveidotu testa failu un ierakstīja tajā otro tekstu. Reinis Bridge nolasīja visus 22 baitus. Šāda nodošana saglabā darba stāvokli failā. Atsevišķu sarunu vēstures joprojām ir jānodod pašam. Oficiālais attālais rīku saraksts aptver failus, termināli un procesu sesijas. Failu pārbaudei nelietojām peli un tastatūru. Windows, macOS un Linux atbalstu norāda izstrādātājs. Šeit fiziski pārbaudīts Windows.

**2026. gada pieredze.** 2026. gada 13. oktobrī Windows lietotājs ar 0.2.52 ziņoja, ka start_process atvēra konsoles virs citām programmām. 3. novembrī cits lietotājs ar 0.3.1 ziņoja par aptuveni 60 sekunžu noildzēm, arī ja ierīce rādījās tiešsaistē. Tie ir divi konkrēti gadījumi. Šīs pārbaudes laikā failu apmaiņa izdevās.

Palaidējs lieto lokālo 0.3.2 pakotni. Attālais 0.3.0 ir atsevišķs produkts ar konta piesaisti. Grafiskās pogas var pārbaudīt pārlūka profilā.

**Vienlaicīgs darbs.** Divu rīku failu apmaiņa pārbaudīta. Vienas ierīces maksimālais vienlaicīgo čatu skaits nav izmērīts.

[local](https://github.com/wonderwhy-er/DesktopCommanderMCP) · [remote](https://github.com/desktop-commander/remote-desktop-commander) · [help](https://desktopcommander.app/help/getting-started/what-is-desktop-commander) · [reportFocus](https://github.com/wonderwhy-er/DesktopCommanderMCP/issues/852) · [reportTimeout](https://github.com/desktop-commander/remote-desktop-commander/issues/90)

## 6. Reinis Bridge · 1.0.0

Windows. Atsevišķā OpenBot privātajā Chrome logā tika izveidots šā projekta GitHub repozitorijs. Pēc pārbaudes lietotne aizvērās, un lokālā aizvēršanas kvīts apliecināja, ka lietotāja ievades darbvirsma palikusi tā pati.



**Pārbaude.** Rīgā 12. novembrī plkst. 00.58 pa esošo tiltu palaidām divus īsus fona darbus. To izpildes laiki pārklājās 5,011 sekundes. Atkārtots pieprasījums ar to pašu darba atslēgu atgrieza jau pabeigto darbu. Korekti atsākt var arī lasīšanu no pēdējās saglabātās vietas.

**2026. gada pieredze.** Reiņa novērojums ir viena interaktīvā plūsma. Divi fona termināļa darbi darbojās vienlaikus. Divu atsevišķu čatu vienlaicīga darbvirsmas vadība šajā testā nav izmēģināta.

Šis ir Reiņa personīgais Windows tilts. Projekta Windows palaidējs dod savu, lokālu savienojumu ar izvēlētu mapi. Tas neinstalē Reiņa privāto tiltu un neprasa piekļuvi viņa datoram.

**Vienlaicīgs darbs.** Viena interaktīva darbvirsma. Divi mūsu fona darbi pārklājās 5,011 sekundes.

[REYRUN · Windows](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

## 7. Git worktree + bundle · Git CLI · tested 2.52.0

Windows, macOS. Projekta failiem, kurus vari nodot starp sesijām bez dzīva savienojuma. Katrs uzdevums saņem savu darba kopiju un zaru. Uz citu datoru var pārnest saglabāto izmaiņu pakotni.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-macOS.command.zip)

**Pārbaude.** Linux vidē izveidojām divas darba kopijas. Vienas izmaiņas atstāja otru neskartu. Pārbaudījām pakotni un no tās atjaunojām to pašu komitu un identiskus faila baitus.

**2026. gada pieredze.** Vācu autoru izmēģinājumā divu darbu izmaiņas pārbaudītas atsevišķās mapēs. Izmēģinājumā abu darba lomas atveidoja ar failu izmaiņām.

Darba kopijām ir kopīga Git objektu glabātava. Pilnā zara pakotnē var būt tā iepriekšējā vēsture. Dalīšanai veido atsevišķu repozitoriju tikai ar izvēlētajiem failiem. Šis ceļš pats nedod iespēju vadīt datoru, programmas vai peli.

**Vienlaicīgs darbs.** Pārbaudītas divas darba kopijas, katrai savs zars.

[Git worktree manual](https://git-scm.com/docs/git-worktree) · [Git bundle manual](https://git-scm.com/docs/git-bundle) · [Git desktop downloads](https://git-scm.com/downloads) · [German practical two-role experiment · 9 September 2026](https://www.bitblokes.de/ki-agenten-git-worktrees/) · [GitHub · git/git](https://api.github.com/repos/git/git)

## 8. REYRUN · Web Crypto

Windows, macOS, Android, iOS. Atver gatavu skriptu savā pārlūkā un ar vienu pieskārienu pārbaudi paraugu vai izvēlies teksta failu.

[Atvērt gatavo paraugu](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/)

**Pārbaude.** Android 15 emulatorā viens pieskāriens ekrānam apstrādāja nemainīto publisko paraugu. WebView 124.0.6367.219 atdeva 13 baitus, 2 rindas un paredzēto SHA-256. Tādu pašu rezultātu ieguvām Chrome priekšskatījumā. iPhone SE simulatorā ar iOS 18.5 un WebKit parauga poga deva to pašu rezultātu. Neatbalstīta darbība tika noraidīta. Tās ir operētājsistēmu simulācijas.

**2026. gada pieredze.** Šai jaunajai demonstrācijai neatkarīgu lietotāju atsauksmju vēl nav.

Šis ir viena faila apliecinājums. Lai čats izlasītu kļūdas tekstu, iedod tam vajadzīgo fragmentu.

**Vienlaicīgs darbs.** Katram darbam savs fails vai kvīts. Tālruņa kopīgošanas izvēlni izmanto viena darbība reizē.

[REYRUN](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/web/start) · [MDN · File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API) · [MDN · SubtleCrypto.digest](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest) · [Android 15 · WebView · 2026-11-11](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121791094/job/130863821353) · [iPhone SE · iOS 18.5 · WebKit](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/actions/runs/43121668999/job/130863410709)

## 9. LocalSend

Windows, macOS, Android, iOS. Pārsūti sagatavotu failu uz otru ierīci savā Wi-Fi tīklā.

[Atvērt gatavo paraugu](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/)

**Pārbaude.** Šeit divu ierīču pārsūtīšana nav izmēģināta. Pašpārbaudei nosūti mobile-request.json, tad salīdzini ID un kontrolsummu mūsu lapā.

**2026. gada pieredze.** 25.06.2026. xueyexiao ķīniešu valodā aprakstīja, kā Redmi K70 failu nosūtīja no Android failu lietotnes kopīgošanas izvēlnes, kad LocalSend atlasītājam pietrūka atļaujas.

Vajadzīgas divas savienotas ierīces ar LocalSend. Izvēlies failu un saņēmēju.

**Vienlaicīgs darbs.** Katram darbam savs fails vai kvīts. Tālruņa kopīgošanas izvēlni izmanto viena darbība reizē.

[LocalSend](https://localsend.org/download) · [2026 · Changelog](https://localsend.org/changelog) · [xueyexiao · Redmi K70 · 中文](https://github.com/localsend/localsend/discussions/835) · [REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 10. Nextcloud Files

Windows, macOS, Android, iOS. Saglabā čata sagatavoto failu savā Nextcloud mapē un turpini tajā pašā mapē no datora.

[Atvērt gatavo paraugu](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/)

**Pārbaude.** Sesijā nepieslēdzām privātu serveri. Pārbaudes kritērijs ir pareizais ID un kontrolsumma failam, kas saņemts otrā ierīcē.

**2026. gada pieredze.** 28.04.2026. Sanook vāciski aprakstīja gaidošu Android fotoattēla augšupielādi. Vēlāk tā pabeidzās. Tas bija novērojums par foto, nevis mūsu testa failu.

Izvēlies, ja tev jau ir Nextcloud konts un mape. Jauna servera izveide ir atsevišķs darbs.

**Vienlaicīgs darbs.** Katram darbam savs fails vai kvīts. Tālruņa kopīgošanas izvēlni izmanto viena darbība reizē.

[Nextcloud](https://nextcloud.com/install/) · [iOS · 2026](https://github.com/nextcloud/ios/issues) · [Sanook · Android · Deutsch](https://help.nextcloud.com/t/android-client-warte-auf-hochladen/217584/18) · [REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 11. Termux

Android. Android telefonā pārbaudi gatavu skriptu Termux privātajā mapē.

[Gatavais Termux skripts](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-termux.sh)

**Pārbaude.** Palaists divreiz Linux vidē ar sh. Iegūtas divas atsevišķas mapes un divi JSON ar pareizo kontrolsummu. Android izpildi neesam izmēģinājuši.

**2026. gada pieredze.** 30.04.2026. slondr ziņoja par iestrēgušu failu atlasītāju Pixel 9a ar Android 16. Projekta izstrādātājs tajā pašā diskusijā minēja divus Samsung, kuros atlase darbojās.

Izmanto jau uzstādītā Termux vidē. Ātrākais ceļš no parasta čata ir pārlūka paraugs.

**Vienlaicīgs darbs.** Katram darbam savs fails vai kvīts. Tālruņa kopīgošanas izvēlni izmanto viena darbība reizē.

[Termux](https://github.com/termux/termux-app) · [Android 15 · #5150](https://github.com/termux/termux-app/issues/5150) · [Termux · Installation](https://github.com/termux/termux-app#installation) · [Termux:API](https://github.com/termux/termux-api) · [slondr · Pixel 9a · English](https://github.com/termux/termux-app/issues/5101)

## 12. Apple Shortcuts

iOS, macOS. Nodod failu jau iestatītai Apple komandai caur kopīgošanas izvēlni.

[Atvērt gatavo paraugu](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/)

**Pārbaude.** Šo darbību secību fiziskā iPhone neesam izmēģinājuši. Lietotnē Files atver saglabāto phone-test.txt un pārbaudi, ka redzams REYRUN-OK.

**2026. gada pieredze.** 28.01.2026. japāņu autors anyprogram parādīja savu iPhone un iPad saīsni TXT failu izveidei un saglabāšanai. Viņa esoša faila rediģēšanas režīms pārraksta izvēlēto failu.

Šim variantam vajadzīga jau pievienota komanda, kas pieņem failus. Šeit ir pārlūka paraugs, kuru var izmēģināt tūlīt.

**Vienlaicīgs darbs.** Katram darbam savs fails vai kvīts. Tālruņa kopīgošanas izvēlni izmanto viena darbība reizē.

[Apple · iPhone](https://support.apple.com/guide/shortcuts/launch-a-shortcut-from-another-app-apd163eb9f95/ios) · [Apple · Share](https://support.apple.com/guide/shortcuts/share-shortcuts-apdf01f8c054/ios) · [Apple · Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios) · [anyprogram · iPhone/iPad · 日本語](https://qiita.com/anyprogram/items/6cc1394569c687ed506c) · [iPhone 16 Pro Max · 2026](https://github.com/net00-1/SW-DLT/issues/133) · [REYRUN · mobile-request.json](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-request.json)

## 13. Desktop Commander Remote · ChatGPT

Windows, macOS, Linux. Strādā ar piesaistītā datora failiem no tīmekļa čata.

[Atvērt pamācību](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/#devices)

**Pārbaude.** Izstrādātājs dokumentē Windows, macOS un Linux.

**2026. gada pieredze.** Izstrādātāja dokumentācija.

Savienojumam jādarbojas mērķa datorā.

**Vienlaicīgs darbs.** Vienlaicīgu savienojumu skaits šim variantam nav mērīts.

[Desktop Commander Remote · ChatGPT](https://desktopcommander.app/help/devices/connect-computer)

## 14. Google Gemini · Device assistance

Android. Palūdz Gemini iestatīt taimeri telefona lietotnē Pulkstenis.

[Atvērt pamācību](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/#device-android)

**Pārbaude.** Google apraksta darbību Gemini Android lietotnē.

**2026. gada pieredze.** Izstrādātāja dokumentācija.

Jāizmanto Gemini Android lietotne.

**Vienlaicīgs darbs.** Vienlaicīgu savienojumu skaits šim variantam nav mērīts.

[Google Gemini · Device assistance](https://support.google.com/gemini/answer/15235441)

## 15. Claude · Apple Reminders

iOS. Izveido atgādinājumu jau esošā iPhone vai iPad sarakstā.

[Atvērt pamācību](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/#device-iphone)

**Pārbaude.** Anthropic apraksta atgādinājumu izveidi ar lietotāja atļauju.

**2026. gada pieredze.** Izstrādātāja dokumentācija.

Vajadzīga Claude mobilā lietotne un atļauja atgādinājumiem.

**Vienlaicīgs darbs.** Vienlaicīgu savienojumu skaits šim variantam nav mērīts.

[Claude · Apple Reminders](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps)

## Uzstādi RDR2 tulkojumu

Stāsta režīmam Windows datorā. Ja spēlei jau ir pārbaudītās Universal RDR2 String Translator un Ultimate ASI Loader x64 9.7.4 versijas, aizver spēli, lejupielādē un atver XML uzstādītāju. Tas atpazīst zināmos spraudņu failus pēc kontrolsummas, saglabā veco latviešu XML un uzstāda pārbaudīto tulkojumu. Ja atrod citu pamata tulkojumu vai trūkst spraudņa, palaidējs apstājas un parāda pamācības saiti.

[Uzstādīt latviešu XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Install-XML.cmd) · [Atjaunot iepriekšējo XML](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-RDR2-Restore-XML.cmd)

Lejupielādē un atver Windows palaidēju. Tas meklē spēli Steam, Rockstar un Epic bibliotēkās un sagatavo pārbaudītu latviešu tulkojuma failu darba mapē. Ja der vairākas mapes, spēlētājs izvēlas īsto. Tad iedod MI uzstādīšanas instrukciju. Tajā ir spraudnis, ielādētājs, rezerves kopija un spēles pārbaude stāsta režīmā. [Atvērt tulkojuma instrukciju](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/uzstadisana/)

## Kā strādā četri čati reizē?

Katram čatam piešķir savu darba nosaukumu un atsevišķu mapi. Tekstu, failu salīdzināšanu un pārbaudes var dalīt. Par izmaiņām vienā spēles mapē atbild viens čats. Pārlūkprogrammai katrai sesijai dod savu profilu. Uz kopīgas darbvirsmas peli vada tikai viena sesija.

## Ko darīt, kad savienojums pārtrūkst?

Jaunajā čatā nosauc to pašu darbu. Palūdz nolasīt pēdējo saglabāto soli un pārbaudīt, kuri faili jau izveidoti. Pēc noildzes vispirms pārbaudi esošo darbu. Lejupielādi vai kopēšanu atkārto tikai tad, kad redzams, ka tā nav pabeigta. Diviem čatiem saglabājot vienu redakciju, jaunākais ieraksts ir jāizlasa pirms nākamā mēģinājuma.

## Ko čatbots drīkst darīt manā datorā?

Failu palaidējs atver vienu REYRUN darba mapi. Spēles variantam pievienojas izvēlētā RDR2 mape. Pārlūka paraugam pietiek ar vienu izvēlētu failu. Pirmajā reizē sistēma var prasīt atļauju atvērt lejupielādi. Ja redzi negaidītu pieprasījumu, vari palikt pie pārlūka parauga.

## Kā atrast programmas kļūdu?

Ieliec programmas kļūdas žurnāla kopiju REYRUN darba mapē. Lūdz savam MI sameklēt pēdējo kļūdu un paskaidrot to. Ja lieto parastu tīmekļa čatu, pievieno tam tikai attiecīgo teksta fragmentu. Pārlūka paraugs apliecina faila kontrolsummu un rindu skaitu. Pats žurnāla teksts paliek ierīcē.

## Kur pārbaudīt savienojumu?

Windows vidē gatavais palaidējs nolasa esošās Claude Desktop konfigurācijas mapi %APPDATA%/Claude. Mac datorā tā ir ~/Library/Application Support/Claude. Iestatījumu failā claude_desktop_config.json tas pievieno vienīgi izvēlēto reyrun-… ierakstu un saglabā iepriekšējo versiju. Ja klienta nav, START.txt norāda pārlūka paraugu. Ja citam klientam ir vietējais MCP, izmanto palaidēja izveidoto runtime/reyrun-…-client.json. Tur norādīta tieši šim datoram atbilstošā izpildāmā faila atrašanās vieta.

## Piemērs darba nodošanai

Pēc pārbaudes saglabā pēdējo pierādīto rezultātu un vienu nākamo darbību. Ja jaunam čatam ir tas pats lokālais profils, tas var izsaukt read_checkpoint ar to pašu job. Parasts tīmekļa čats var turpināt, ja tajā ielīmē šo pierakstu un pievieno vajadzīgo failu. Spēles logu un atļauju dialogus vada viena sesija.


```json
{
  "name": "save_checkpoint",
  "arguments": {
    "job": "game-check",
    "revision": 0,
    "done": "Testa fails precīzi nolasīts.",
    "next": "Pārbaudi izvēlēto spēles mapi."
  }
}
```
