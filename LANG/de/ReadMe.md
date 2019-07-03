# Caster [![Build Status](https://travis-ci.org/dictation-toolbox/Caster.svg?branch=master)](https://travis-ci.org/dictation-toolbox/Caster)

[Caster](https://github.com/dictation-toolbox/Caster) ist eine Sammlung von Tools, die darauf abzielen, die Programmierung und den Zugriff ausschließlich über die auf der [Dragonfly-](https://github.com/dictation-toolbox/dragonfly) API basierende Sprache zu ermöglichen.

**Hinweis für PyPi-Benutzer** : Das PIP-Paket ist ( *Alpha* ). Verwenden Sie nicht die PIP-Installation. Alternativ können Sie den [Master-Zweig](https://gihttps://github.com/dictation-toolbox/Caster) mit klassischer Installation verwenden, um die bestmögliche Funktionserfahrung zu erzielen.

- Videos von der Caster Community. 
    -  [Caster Demo](https://www.youtube.com/watch?v=oIwh3z2jXD4) 
    -  [VimGolf und Project Euler](https://www.youtube.com/watch?v=T1bKAqDhH_E) 
    -  [Diktieren von Mathe in ein wissenschaftliches Notizbuch](https://www.youtube.com/watch?v=oq8EoPu0cGY&t=3s) und [Diktieren von Mathe durch Stimme mit Caster](https://www.youtube.com/watch?v=z-iHvPmjcas) 
- [Anleitung zur Installation](https://caster.readthedocs.io/en/latest/Installation/)
- Dokumentation zu Caster [ [ReadTheDocs](https://caster.readthedocs.io/en/latest/) ] und Dragonfly [ [ReadTheDocs](https://dragonfly2.readthedocs.io/en/latest/) ]
- [Wie man Code spricht](https://caster.readthedocs.io/en/latest/readthedocs/Examples/Speaking/Examples/) - Beispieldokument
- Caster-Befehlsreferenzhandbücher 
    -  [Caster](https://github.com/dictation-toolbox/Caster/blob/master/CasterQuickReference.pdf) - Befehle zum Einstieg. Universelle Navigation und Bearbeitung - Diese Befehle sind ständig aktiv und bieten Eingabebefehle für Buchstaben, Zahlen und Satzzeichen sowie die Möglichkeit, Fenster und Text auf einfache Weise zu bearbeiten. 
        -  `window right` verschiebt das aktive Fenster auf die rechte Seite des Bildschirms. 
        -  `prekris` fügt ein Paar Klammern `()` und bewegt den Cursor darin. 
        -  `shackle` wählt die aktuelle Linie. 
    -  [Anwendungen](https://caster.readthedocs.io/en/latest/readthedocs/Application_Commands_Quick_Reference/) - Anwendungsspezifische Steuerung - Diese Befehle werden nur aktiviert, wenn ein bestimmtes Programm das aktive Fenster ist. Sie bieten Unterstützung für Texteditoren, IDEs, Webbrowser usw., während beispielsweise der Sublime-Texteditor das aktive Fenster ist 
        -  `find` führt einen Tastendruck mit der `ctrl-f` und `ctrl-f` die Eingabeaufforderung zum Suchen und Ersetzen auf. 
        -  `open file` führt einen Tastendruck mit `ctrl-o` . 
        -  `edit next <n>` - `ctrl-d` n-mal, wobei die nächsten n Instanzen des aktuell ausgewählten Wortes ausgewählt werden. 
    -  [Programmiersprachen](https://caster.readthedocs.io/en/latest/readthedocs/CCR_languages_Quick_Reference/) - Sprachspezifische Codierung - Diese Module werden mit dem `enable/disable <language>` aktiviert und deaktiviert. Sagen Sie zum Beispiel " `enable python` . 
        -  `for loop` die `for i in range(0, ):` 
        -  `print to console` `print()` - `print()` 
        -  `open file` - `open('filename', 'r') as f:` 
- [Mitmachen / Wie kann ich helfen?](https://caster.readthedocs.io/en/latest/Contributing/)
- Möchten Sie die Caster-Entwicklung finanziell unterstützen? Spenden Sie bei [![Kopfgeldquelle](https://www.bountysource.com/badge/team?team_id=407907&style=bounties_posted)](https://www.bountysource.com/teams/caster-dictation/bounties?utm_source=Bountysource&utm_medium=shield&utm_campaign=bounties_posted)
- [Erstellen Sie Ihre eigenen Dragonfly- und Caster-Regeln,](https://caster.readthedocs.io/en/latest/readthedocs/Examples/Rule_Construction/) die durch [Entwicklungsbefehle](https://caster.readthedocs.io/en/latest/readthedocs/CCR_languages_Quick_Reference/#VoiceDevCommands) erweitert werden
- Benötigen Sie Unterstützung oder sind Sie einfach nur neugierig? Treten Sie unserer Community bei [![Besuchen Sie den Chat unter https://gitter.im/synkarius/caster](https://badges.gitter.im/Join%20Chat.svg) und](https://gitter.im/dictation-toolbox/home) [Zwietracht](https://discord.gg/9eAAsCJ) für Voice-Chat.
- Der [Sprachindex](https://caster.readthedocs.io/en/latest/readthedocs/Voice_Index/) ist eine kuratierte Informationsquelle: Videos, Blogs, Repositories, Präsentationen usw. in Bezug auf Dragonfly, Sprachprogrammierung und Barrierefreiheit.

# Funktionsliste

- Konfigurierbare Einstellungen in `C:\Users\%USERNAME%\.caster`

- Passen Sie Befehle, auch bekannt als `Specs` und ihre Aktionen über [vereinfachte Filterregeln](https://caster.readthedocs.io/en/latest/readthedocs/CCR/#rule-filters-simplified) und [Filterregeln](https://caster.readthedocs.io/en/latest/readthedocs/CCR/#Rule-Filters) (WIP) an. Codebeispiele für `.caster\filters\examples` finden Sie unter `.caster\filters\examples` .

- Kompatible Spracherkennungsmodule

    - [Dragon NaturallySpeaking](https://www.nuance.com/dragon.html) v13 und höher
    - [Windows-Spracherkennung](https://support.microsoft.com/en-us/help/17208/windows-10-use-speech-recognition)

- Unterstützte [Programmiersprachen](https://caster.readthedocs.io/en/latest/readthedocs/CCR_languages_Quick_Reference/) - Verbessert durch die [kontinuierliche](https://caster.readthedocs.io/en/latest/readthedocs/CCR/) Befehlserkennung von Caster - [Demo](https://www.youtube.com/watch?v=Obdegwr_LFc&index=5&list=PLV6JPhkq1x8LHu02YefhUU9rXiB2PK8tc)

    - Python, Java, Bash, C ++, C #, Rust, Go, HTML, CSS, JavaScript, SQL, Dart, Latex, Matlab, R, Prolog, VHDL und Haxe

- Unterstützte [Anwendungen](https://caster.readthedocs.io/en/latest/readthedocs/Application_Commands_Quick_Reference/)

    - IDEs / Editoren: Microsoft Visual C ++, Visual Studio, Eclipse, Jetbrains IDEs, Emacs, Sublime, Atom, Visual Studio-Code, Editor ++, FlashDevelop, SQL Developer und SQL Server Management Studio
    - Entwicklungstools: Eingabeaufforderung, GitBash, KDiff3
    - Statistik: RStudio und Lyx
    - Browser: Firefox, Chrome und Internet Explorer
    - Git Client: Github Desktop
    - Anwendungen: Foxit Reader, Gitter, Total Commander, Typora, Microsoft Word, Outlook und Excel

- [Bearbeitung und Navigation](https://github.com/dictation-toolbox/Caster/blob/master/CasterQuickReference.pdf)

    - Vier zusätzliche [Maus-Navigationsmodi](https://caster.readthedocs.io/en/latest/readthedocs/Mouse/) : Curse, Douglas, Legion und Rainbow - [Demo](https://www.youtube.com/watch?v=UISjQBMmQ-I&feature=youtu.be)
    - [Textnavigationsbefehle](https://caster.readthedocs.io/en/latest/readthedocs/Text_Manipulation/) - [Demo](https://www.youtube.com/watch?v=xj8IzNlfM70) , Befehle zur Textformatierung
    - Eingabebefehle für Buchstaben, Zahlen und Satzzeichen
    - Befehle zur Interaktion mit allgemeinen Dateidialogen.

- Nutzen Sie leistungsstarke Befehle

    - " [Alias](https://caster.readthedocs.io/en/latest/readthedocs/Alias/) " -Befehle - On-the-Fly-Befehle, die durch Hervorheben von Elementen erstellt werden
    - " [Record From History](https://caster.readthedocs.io/en/latest/readthedocs/Record_Macros/) " - verwandelt zuvor gesprochene Befehle in ein Sprachmakro

- Drittanbieter-Integrationen

    - [Sikulix](http://sikulix.com/) - [Setup](https://caster.readthedocs.io/en/latest/readthedocs/Sikuli/) : Automatisiert alles, was Sie auf dem Bildschirm Ihres Desktop-Computers sehen. - [Demo](https://youtu.be/RFdsD2OgDzk?list=PLV6JPhkq1x8LHu02YefhUU9rXiB2PK8tc&t=512)
    - [Aenea](https://github.com/dictation-toolbox/aenea) - [Setup](https://caster.readthedocs.io/en/latest/readthedocs/Aenea/) : Eine Client-Server-Bibliothek zur Verwendung von Sprachmakros von Dragon NaturallySpeaking und Dragonfly auf Remote- / Nicht-Windows-Hosts.
    - [Autohotkey](https://www.autohotkey.com/) : Eine Skriptsprache, mit der verschiedene Aufgaben in Windows automatisiert werden können. Installieren Sie einfach die neueste Version. Wenn es installiert ist, kann es einige Befehle um einige Sekunden beschleunigen - z. B. das [Auschecken oder Aktualisieren einer Pull-Anfrage von github](https://caster.readthedocs.io/en/latest/readthedocs/Application_Commands_Quick_Reference/#google-chrome) .

- Caster erweitert die Dragonfly-API um noch leistungsstärkere Befehle.

    - Der [Kontextstapel](https://caster.readthedocs.io/en/latest/readthedocs/ContextStack/) - Erstellen Sie asynchrone und kontextsuchende Befehle
    - [Spezifikationsreduktion](https://caster.readthedocs.io/en/latest/readthedocs/NodeRule/) über [NodeRule](https://caster.readthedocs.io/en/latest/readthedocs/NodeRule/) (WIP)
