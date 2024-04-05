
# Git-Repository klonen bzw. herunterladen und zum Verzeichnis wechseln
$ git clone https://github.com/abinesh1606/flaskwiederholungspruefung.git && cd flaskwiederholungspruefung

# Virtuelle Umgebung erstellen und aktivieren (Windows)
$ python -m venv venv && .\venv\Scripts\activate

# Virtuelle Umgebung erstellen und aktivieren (Linux/Mac)
$ python -m venv venv && source venv/bin/activate

# Erforderliche Pakete installieren
$ pip install -r requirements.txt

# Quiz-Anwendung starten 
$ python app.py
