# Instrukcija MI · REYRUN Tilts

[Latviski](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/) · [English](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/) · [Русский](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/ru/)

[Lejupielādēt Windows palaidēju](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [Lejupielādēt Mac palaidēju](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip) · [Izmēģināt telefonā vai pārlūkā](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=lv)

Lejupielādē un atver. Palaidējs pievieno darba mapi jau uzstādītai Claude Desktop lietotnei. Pilnībā aizver un atver lietotni, kad tev ērti. Citam čatam izvēlies pārlūka paraugu. Mac datorā atver arhīvā esošo .command failu. Pirmajā reizē sistēma var parādīt savu apstiprinājumu.

## Pārbaudes pēc palaidēja atvēršanas

Files lietotnē izsauc list_allowed_directories. Izveido testa failu tikai parādītajā darba mapē un nolasi tā saturu. Ja rezultāts nesakrīt, neveic instalāciju. Task Bridge profilā izsauc bridge_status, pēc tam read_checkpoint. Pirms pirmās save_checkpoint izmanto revision 0. Pēc savienojuma pārrāvuma izsauc read_checkpoint ar to pašu darba nosaukumu.

## 1. Filesystem MCP · 2.3.0

Windows, macOS. Vislabāk der failu sagatavošanai vienā darba mapē. MI palīgs var sakārtot projektu un pārkopēt failus, saglabājot to baitus.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-filesystem-macOS.command.zip)

**Pārbaude.** Linux testa vidē palaidām īsto 2.3.0 serveri. Tas parādīja atļautās mapes, nolasīja faila informāciju, precīzi pārkopēja bināru failu un atteica piekļuvi ārpus izvēlētajām mapēm. Uz fiziska Windows datora svaiga uzstādīšana ar esošu Node aizņēma 6,68 sekundes. Latviešu teksta fails tika ierakstīts un precīzi nolasīts. Piekļuve ārpus darba mapes tika atteikta.

**2026. gada pieredze.** Martā lietotājs ziņoja, ka klienta norādītās mapes aizstāja komandrindas sarakstu. Šeit lietojam --confine-roots un pārbaudām faktisko atļauju sarakstu.

Vienai lasīšanas sesijai pievieno --read-only. Kopējot esošu failu, vispirms pārbaudi, vai mērķis jau pastāv. copy_file nepieļauj pārrakstīšanu. Parasts čats bez vietēja savienojuma dod norādes spēlētājam.

[Filesystem MCP · tools and directory rules](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md) · [Filesystem 2.3.0 release](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) · [Desktop client setup for Windows and macOS](https://modelcontextprotocol.io/docs/develop/connect-local-servers) · [User report on effective roots, 16 March 2026](https://github.com/modelcontextprotocol/servers/issues/3602) · [GitHub · modelcontextprotocol/servers](https://api.github.com/repos/modelcontextprotocol/servers) · [Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/windows-filesystem.json)

## 2. REYRUN Task Bridge · 1.0.0

Windows, macOS. Nodod nākamajam čatam precīzi to vietu, kur darbs apstājās. Katram darbam ir sava pierakstu vēsture.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-jobs-macOS.command.zip)

**Pārbaude.** Windows dators, Node 24.19, plkst. 01.11 Rīgā. Palaidējs divreiz pareizi sagatavoja savienojumu testa mapēs ar atstarpēm nosaukumā un saglabāja iepriekšējo iestatījumu. Viens klienta process ierakstīja 1. redakciju. Otrs to nolasīja. Mēģinājums rakstīt pāri no vecākas redakcijas tika noraidīts. Četri vienlaicīgi lokāli klienti saglabāja četrus atsevišķus darbus. Kopīgajā ierakstā uzvarēja viens no četriem. Pēc restartēšanas varēja nolasīt visus piecus darbus.

**2026. gada pieredze.** Projekta paša 12. novembra pārbaude.

Šis profils glabā darba pierakstus. Failu pārkopēšanai izvēlies Filesystem.

[Windows · JSON](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json) · [4 × stdio](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/parallel.json)

## 3. Microsoft Playwright MCP · 0.0.85

Windows, macOS. Vislabāk der sava projekta tīmekļa pārbaudēm, kad jāatrod poga, jāpāriet uz nākamo lapu vai jāpārbauda salasāmība. Katram darbam var būt savs pārlūka profils.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-playwright-macOS.command.zip)

**Pārbaude.** Linux vidē pārbaudījām MCP savienojumu un rīku sarakstu. Šajā vidē sistēma liedza Chromium izveidot ligzdu, tāpēc savu lapas testa rezultātu neuzrādām. Microsoft 11. novembra pārbaudēs Windows un macOS testi izturēti.

**2026. gada pieredze.** Japāņu praktiskajā salīdzinājumā autors atsevišķi pārbaudīja pārlūka procesu un pieteikšanās stāvokli. Paralēliem darbiem viņš iesaka skaidri izvēlēties izolētu profilu.

Profils sākas bez tavas personiskās pieteikšanās. Standarta rīku saraksts ietver arī koda izpildi. --allowed-origins pats par sevi negarantē pilnīgu tīkla izolāciju. Izmanto savu uzticamu testa vietni un klienta rīku atļaujas.

[Microsoft release · 9 November 2026](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.85) · [Microsoft · browser profiles and documented options](https://github.com/microsoft/playwright-mcp) · [Author tests on Windows, macOS and Ubuntu · 11 November](https://github.com/microsoft/playwright-mcp/actions/runs/43074928448) · [Japanese first-person profile comparison · 29 June 2026](https://zenn.dev/ruri/articles/playwright-multi-session-isolation) · [GitHub · microsoft/playwright-mcp](https://api.github.com/repos/microsoft/playwright-mcp)

## 4. Chrome DevTools MCP · 1.13.0

Windows, macOS. Izvēlies vienkāršai vizuālai pārbaudei. Ierobežots rīku komplekts var atvērt atļauto projekta lapu un uzņemt tās ekrānattēlu.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-devtools-macOS.command.zip)

**Pārbaude.** Linux vidē pārbaudījām 1.13.0 savienojumu. Ar norādītajiem ierobežojumiem serveris piedāvāja tieši divus rīkus: navigate un screenshot. Vietējā testa pārlūks netika palaists. Autoru Windows un macOS pārbaudes citā tās pašas dienas izpildē izturētas. Vēlāk tajā dienā citā pirmslaidiena izpildē neizturēja macOS tests ar Node 22.

**2026. gada pieredze.** macOS lietotājs ziņoja, ka pēc servera avārijas var palikt atvērts testa Chrome process. Ķīniešu autors atsevišķi aprakstīja praktisku pārbaudi Debian vidē un precīzi norādīja neizmēģinātās iespējas.

Šis profils ir īslaicīgs. Lai izmantotu jau atvērtu personisko cilni, būtu jāizvēlas cits režīms. Attēlos var būt privāti dati no pašas testa lapas. Aizver sesiju ar klienta apturēšanas darbību.

[Chrome DevTools release · 11 November 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0) · [Chrome DevTools MCP · configuration](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md) · [Upstream Windows/macOS/Ubuntu test matrix · 11 November](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43058501937) · [macOS report about abrupt termination · 26 August 2026](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/2621) · [Chinese practitioner’s test log · 21 October 2026](https://friendlyai.top/projects/chrome-devtools-mcp/) · [Later upstream pre-release run · macOS/Node 22 failure](https://github.com/ChromeDevTools/chrome-devtools-mcp/actions/runs/43105363963) · [GitHub · ChromeDevTools/chrome-devtools-mcp](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp)

## 5. Desktop Commander · Remote / Local

Windows, macOS. Fonā strādā ar failiem un termināļa sesijām. Šejienes lokālais palaidējs dod čatam trīs rīkus vienas darba mapes apskatei.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-commander-macOS.command.zip)

**Pārbaude.** Windows ierīce ziņoja versiju 0.3.0. Desktop Commander nolasīja caur Reinis Bridge izveidotu testa failu un ierakstīja tajā otro tekstu. Reinis Bridge nolasīja visus 22 baitus. Šāda nodošana saglabā darba stāvokli failā. Atsevišķu sarunu vēstures joprojām ir jānodod pašam. Oficiālais attālais rīku saraksts aptver failus, termināli un procesu sesijas. Failu pārbaudei nelietojām peli un tastatūru. Windows, macOS un Linux atbalstu norāda izstrādātājs. Šeit fiziski pārbaudīts Windows.

**2026. gada pieredze.** 2026. gada 13. oktobrī Windows lietotājs ar 0.2.52 ziņoja, ka start_process atvēra konsoles virs citām programmām. 3. novembrī cits lietotājs ar 0.3.1 ziņoja par aptuveni 60 sekunžu noildzēm, arī ja ierīce rādījās tiešsaistē. Tie ir divi konkrēti gadījumi. Šīs pārbaudes laikā failu apmaiņa izdevās.

Palaidējs lieto lokālo 0.3.2 pakotni. Attālais 0.3.0 ir atsevišķs produkts ar konta piesaisti. Grafiskās pogas var pārbaudīt pārlūka profilā.

[local](https://github.com/wonderwhy-er/DesktopCommanderMCP) · [remote](https://github.com/desktop-commander/remote-desktop-commander) · [help](https://desktopcommander.app/help/getting-started/what-is-desktop-commander) · [reportFocus](https://github.com/wonderwhy-er/DesktopCommanderMCP/issues/852) · [reportTimeout](https://github.com/desktop-commander/remote-desktop-commander/issues/90)

## 6. Reinis Bridge · 1.0.0

Windows. Atsevišķā OpenBot privātajā Chrome logā tika izveidots šā projekta GitHub repozitorijs. Pēc pārbaudes lietotne aizvērās, un lokālā aizvēršanas kvīts apliecināja, ka lietotāja ievades darbvirsma palikusi tā pati.



**Pārbaude.** Rīgā 12. novembrī plkst. 00.58 pa esošo tiltu palaidām divus īsus fona darbus. To izpildes laiki pārklājās 5,011 sekundes. Atkārtots pieprasījums ar to pašu darba atslēgu atgrieza jau pabeigto darbu. Korekti atsākt var arī lasīšanu no pēdējās saglabātās vietas.

**2026. gada pieredze.** Reiņa novērojums ir viena interaktīvā plūsma. Divi fona termināļa darbi darbojās vienlaikus. Divu atsevišķu čatu vienlaicīga darbvirsmas vadība šajā testā nav izmēģināta.

Šis ir Reiņa personīgais Windows tilts. Projekta Windows palaidējs dod savu, lokālu savienojumu ar izvēlētu mapi. Tas neinstalē Reiņa privāto tiltu un neprasa piekļuvi viņa datoram.

[REYRUN · Windows](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/blob/main/research/reinis.json)

## 7. Git worktree + bundle · Git CLI · tested 2.52.0

Windows, macOS. Projekta failiem, kurus vari nodot starp sesijām bez dzīva savienojuma. Katrs uzdevums saņem savu darba kopiju un zaru. Uz citu datoru var pārnest saglabāto izmaiņu pakotni.

[Windows](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-Windows.cmd) · [macOS](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-git-handoff-macOS.command.zip)

**Pārbaude.** Linux vidē izveidojām divas darba kopijas. Vienas izmaiņas atstāja otru neskartu. Pārbaudījām pakotni un no tās atjaunojām to pašu komitu un identiskus faila baitus.

**2026. gada pieredze.** Vācu autoru izmēģinājumā divu darbu izmaiņas pārbaudītas atsevišķās mapēs. Izmēģinājumā abu darba lomas atveidoja ar failu izmaiņām.

Darba kopijām ir kopīga Git objektu glabātava. Pilnā zara pakotnē var būt tā iepriekšējā vēsture. Dalīšanai veido atsevišķu repozitoriju tikai ar izvēlētajiem failiem. Šis ceļš pats nedod iespēju vadīt datoru, programmas vai peli.

[Git worktree manual](https://git-scm.com/docs/git-worktree) · [Git bundle manual](https://git-scm.com/docs/git-bundle) · [Git desktop downloads](https://git-scm.com/downloads) · [German practical two-role experiment · 9 September 2026](https://www.bitblokes.de/ki-agenten-git-worktrees/) · [GitHub · git/git](https://api.github.com/repos/git/git)

## 8. REYRUN · Web Crypto

Windows, macOS, Android, iOS. Atver gatavu skriptu savā pārlūkā un ar vienu pieskārienu pārbaudi paraugu vai izvēlies teksta failu.

[Atvērt gatavo paraugu](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=lv)

**Pārbaude.** Paraugs «REYRUN» un «Rīga» satur 13 baitus divās rindās. Rezultātā ir SHA-256 kontrolsumma.

**2026. gada pieredze.** Pašas REYRUN pārbaude, 2026. gada novembris.

Šis ir viena faila apliecinājums. Lai čats izlasītu kļūdas tekstu, iedod tam vajadzīgo fragmentu.

[REYRUN](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge/tree/main/web/start)

## 9. LocalSend

Windows, macOS, Android, iOS. Pārsūti sagatavotu failu uz otru ierīci savā Wi-Fi tīklā.

[Atvērt gatavo paraugu](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=lv)

**Pārbaude.** Projekts piedāvā lietotnes visām četrām platformām. 1.18.2 izlaidums datēts ar 2026. gada 21. augustu.

**2026. gada pieredze.** Augustā izstrādātāji pievienoja Android failu pārsūtīšanu fonā un kontrolsummu pārbaudi.

Vajadzīgas divas savienotas ierīces ar LocalSend. Izvēlies failu un saņēmēju.

[LocalSend](https://localsend.org/download) · [2026 · Changelog](https://localsend.org/changelog)

## 10. Nextcloud Files

Windows, macOS, Android, iOS. Saglabā čata sagatavoto failu savā Nextcloud mapē un turpini tajā pašā mapē no datora.

[Atvērt gatavo paraugu](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=lv)

**Pārbaude.** Oficiālās lietotnes nodrošina failu apmaiņu ar jau pievienotu Nextcloud kontu.

**2026. gada pieredze.** iOS lietotāji aprakstīja augšupielādes bez redzama progresa. Pirms darba turpināšanas pārbaudi saņemto failu otrajā ierīcē.

Izvēlies, ja tev jau ir Nextcloud konts un mape. Jauna servera izveide ir atsevišķs darbs.

[Nextcloud](https://nextcloud.com/install/) · [iOS · 2026](https://github.com/nextcloud/ios/issues)

## 11. Termux

Android. Android telefonā pārbaudi gatavu skriptu Termux privātajā mapē.

[Gatavais Termux skripts](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/mobile-termux.sh)

**Pārbaude.** Skripts darbojas bez tīkla, izveido paraugu un izdrukā tā kontrolsummu. Pārbaudīta POSIX čaulas izpilde.

**2026. gada pieredze.** Jūnijā viens Android 15 lietotājs ziņoja par pārtrauktiem ilgiem fona procesiem. Īsais paraugs saglabā kvīti uzreiz.

Izmanto jau uzstādītā Termux vidē. Ātrākais ceļš no parasta čata ir pārlūka paraugs.

[Termux](https://github.com/termux/termux-app) · [Android 15 · #5150](https://github.com/termux/termux-app/issues/5150)

## 12. Apple Shortcuts

iOS, macOS. Nodod failu jau iestatītai Apple komandai caur kopīgošanas izvēlni.

[Atvērt gatavo paraugu](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/start/?lang=lv)

**Pārbaude.** Apple dokumentācijā ir aprakstīta faila saņemšana no citas iPhone lietotnes. Gatavais pārlūka paraugs piedāvā kopīgot tā kvīti, ja ierīce to atbalsta.

**2026. gada pieredze.** Apple iOS 26 rokasgrāmata norāda, ka komandas redzamību nosaka tās pieņemtais ievades veids.

Šim variantam vajadzīga jau pievienota komanda, kas pieņem failus. Šeit ir pārlūka paraugs, kuru var izmēģināt tūlīt.

[Apple · iPhone](https://support.apple.com/guide/shortcuts/launch-a-shortcut-from-another-app-apd163eb9f95/ios) · [Apple · Share](https://support.apple.com/guide/shortcuts/share-shortcuts-apdf01f8c054/ios)

## Uzstādi RDR2 tulkojumu

Lejupielādē un atver Windows palaidēju. Tas meklē spēli Steam, Rockstar un Epic bibliotēkās un sagatavo pārbaudītu latviešu tulkojuma failu darba mapē. Ja der vairākas mapes, spēlētājs izvēlas īsto. Tad iedod MI uzstādīšanas instrukciju. Tajā ir spraudnis, ielādētājs, rezerves kopija un spēles pārbaude stāsta režīmā. [Atvērt tulkojuma instrukciju](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/uzstadisana/)

## Kā strādā četri čati reizē?

Katram čatam piešķir savu darba nosaukumu un atsevišķu mapi. Tekstu, failu salīdzināšanu un pārbaudes var dalīt. Par izmaiņām vienā spēles mapē atbild viens čats. Pārlūkprogrammai katrai sesijai dod savu profilu. Uz kopīgas darbvirsmas peli vada tikai viena sesija.

## Ko darīt, kad savienojums pārtrūkst?

Jaunajā čatā nosauc to pašu darbu. Palūdz nolasīt pēdējo saglabāto soli un pārbaudīt, kuri faili jau izveidoti. Pēc noildzes vispirms pārbaudi esošo darbu. Lejupielādi vai kopēšanu atkārto tikai tad, kad redzams, ka tā nav pabeigta. Diviem čatiem saglabājot vienu redakciju, jaunākais ieraksts ir jāizlasa pirms nākamā mēģinājuma.

## Ko čatbots drīkst darīt manā datorā?

Failu palaidējs atver vienu REYRUN darba mapi. Spēles variantam pievienojas izvēlētā RDR2 mape. Pārlūka paraugam pietiek ar vienu izvēlētu failu. Pirmajā reizē sistēma var prasīt atļauju atvērt lejupielādi. Ja redzi negaidītu pieprasījumu, vari palikt pie pārlūka parauga.

## Kā atrast programmas kļūdu?

Ieliec programmas kļūdas žurnāla kopiju REYRUN darba mapē. Lūdz savam MI sameklēt pēdējo kļūdu un paskaidrot to. Ja lieto parastu tīmekļa čatu, pievieno tam tikai attiecīgo teksta fragmentu. Pārlūka paraugs apliecina faila kontrolsummu un rindu skaitu. Pats žurnāla teksts paliek ierīcē.
