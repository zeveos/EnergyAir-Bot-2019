# EnergyAir-Bot-2019
Dieses Script ermöglicht das automatisierte Spielen des Energy Air Games. Nach erfolgreicher Implementation wird der SMS Code automatisiert nach Ablauf der Session eingelesen.
Das Script ist in Python3 geschrieben und benötigt ein Android App um die SMS umleiten zu können.
## Configuration
[Download Python 3.7.4](https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe)\
Nach dem herunterladen der Datei, diese ausführen. Während der Installation gilt es zu beachten, dass der Hacken unter "Add Python 3.7 to PATH" gesetzt ist.\
Nun CMD öffnen und in den Ordner EnergyAir-Bot-2019 navigieren:
```
cd \path\to\your\folder\EnergyAir-Bot-2019
```
Dort muss virtualenv installiert werden:
```
pip3 install virtualenv
virtualenv venv
```
Anschliessend:
```
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Gmail Account needed
  * Klicke auf [Enable The GMAIL API](https://developers.google.com/gmail/api/quickstart/python) und "Download Client Config"
  * In der Gmail Inbox [mail.google.com](https://mail.google.com/) kreiere ein neues "Label".
  * Unter Einstellungen (oben rechts), gehe zu "Filter & blockierte Adressen "Neuen Filter erstellen".
  * Als Betreff: *Forward SMS message from number [+41DEINETELLNR] (sender - Energy (No contact specified))*
  * Enthält die Wörter: *Dein Code für game.energy.ch*
  * Filter erstellen und auf das neu erstellte Label anwenden.
### APP Herunterladen PlayStore
* App Herunterladen [SMS to mail/phone -auto redirect](https://play.google.com/store/apps/details?id=com.gawk.smsforwarder)
* Die App so konfigurieren, dass die SMS an dein vorher konfiguriertes Gmail weitergeleitet wird.
* Achtung: Die App muss im Hintergrund offen bleiben, demnach das App nicht aus den "offenen Apps" löschen. Evtl. Energieplan auf dem Handy anpassen.
### App Iphone (optional)
* Falls du kein Android besitzt, kannst du auch ein entsprechendes App aus dem Appstore nutzen, welche SMS auf Mail umleitet. Die Regex um den Code im String zu finden muss dann entsprechend im gmail_nrg_code.py Script angepasst werden.

### Sonstige Downloads (REQUIRED)
* Download des [Edge Webdrivers](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) in der entsprechenden Version für deinen Browser.\
Webdriver-Version herausfinden:
1. Microsoft Edge öffnen
2. Oben rechts auf die drei Punkte klicken
3. Einstellungen
4. Ganz unten "Info zu dieser App"
* Alternativ können auch Webdriver des Chromes oder IE genutzt werden. Ich habe persönlich die besten Erfahrungen mit dem Edge WD gemacht (entsprechend im Script nggame_2019.py den Webdriver anpassen, wenn gewechselt werden möchte).

## Usage
### Einmalige Ausführung
* credentials.json (GMAIL Api Auth) und WebDriver.exe in den Projektordner platzieren.
* Im gmail_nrg_code.py gibt es eine Stelle (mit Uncomment markiert). Diesen Block einkommentieren (Achtung: Nach dem "#" ist noch ein Leerzeichen, dieses jeweils auch löschen).
* An letzter Stelle im Code die function (main()) einkommentieren und das Script ausführen.
```
python gmail_nrg_code.py
```
* Die id des Labels kopieren und an folgender Codestelle einfügen:
* ```results = service.users().messages().list(userId='me', labelIds=['UNREAD', 'Label_YOURIDHERE'],```
* Code wieder auskommentieren. Auch die function am Ende!

### Ausführen
 ```python nrggame_2019.py```
