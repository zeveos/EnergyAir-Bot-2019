# EnergyAir-Bot-2019
Dieses Script ermöglicht das automatisierte Spielen des Energy Air Games. Nach erfolgreicher Implementation wird der SMS Code automatisiert nach Ablauf der Session eingelesen.
Das Script ist in Python3 geschrieben und benötigt ein Android App um die SMS umleiten zu können.
## Configuration
[Download Python](https://www.python.org/downloads/windows/)
```
python3 -m venv /path/to/new/Energy-Bot/folder
venv\Scripts\activate.bat
pip install -r requirements.txt
```
### Gmail Account needed
  * Klicke auf [Enable The GMAIL API](https://developers.google.com/gmail/api/quickstart/python) und "Download Client Config"
  * In der Gmail Inbox [https://mail.google.com/](mail.google.com) kreiere ein neues "Label".
  * Unter Einstellungen (oben rechts), gehe zu "Filter & blockierte Adressen "Neuen Filter erstellen".
  * Als Betreff: *Forward SMS message from number [+41DEINETELLNR] (sender - Energy (No contact specified))*
  * Enthält die Wörter: *Dein Code für game.energy.ch*
  * Filter erstellen.
### APP Herunterladen PlayStore
* App Herunterladen [SMS to mail/phone -auto redirect](https://play.google.com/store/apps/details?id=com.gawk.smsforwarder)
* Die App so konfigurieren, dass die SMS an dein vorher konfiguriertes Gmail weitergeleitet wird.
* Achtung: Die App muss im Hintergrund offen bleiben, demnach das App nicht aus den "offenen Apps" löschen.
### App Iphone (optional)
* Falls du kein Android besitzt, kannst du auch ein entsprechendes App aus dem Appstore nutzen, welche SMS auf Mail umleitet. Die Regex um den Code im String zu finden muss dann entsprechend im gmail_nrg_code.py Script angepasst werden.

### Sonstige Downloads (REQUIRED)
* Download des [Edge Webdrivers](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) in der entsprechenden Version für deinen Browser.
* Alternativ können auch Webdriver des Chromes oder IE genutzt werden. Ich habe persönlich die besten Erfahrungen mit dem Edge WD gemacht (entsprechend im Script nggame_2019.py den Webdriver anpassen).
## Usage
### Einmalige Ausführung
* Im gmail_nrg_code.py gibt es eine Stelle (mit Uncomment markiert). Diesen Block einkommentieren.
* An letzter Stelle im Code die function einkommentieren und das Script ausführen.
* Die id des Labels kopieren und an folgender Codestelle einfügen:
* ```results = service.users().messages().list(userId='me', labelIds=['UNREAD', 'Label_5591763986028835289'],```
* code wieder auskommentieren.

### Ausführen
 ```python3 nrggame_2019.py```
