# RESTful API
### Hintergrund
Laut Aufgabenstellung sollte ich folgende Flask-Erweiterungen mittels Decisions Record abwägen:

- Flask-RESTful,https://flask-restful.readthedocs.io/en/latest/

- Flask-Restless-NG, https://flask-restless-ng.readthedocs.io/en/latest/

- Flask-RESTX,https://flask-restx.readthedocs.io/en/latest/

- Flask-smorest,https://flask-smorest.readthedocs.io/en/latest/index.html
### Entscheidung
Nachdem ich zahlreiche Websites und YouTube Videos gesehen habe, habe ich mich dazu entschlossen Flask-RESTX zuverwenden. Im folgenden Teil werden die wesentlichen Argumente aufgelistet, die mich überzeugt haben:
### Vorteile
- Einfache API-Erstellung: Flask-RestX erleichtert die Erstellung von RESTful-APIs in Flask. Es bietet Werkzeuge, um schnell und einfach API-Endpunkte zu definieren.

- Datenvalidierung: Die Erweiterung ermöglicht die Validierung von Daten, die über die API gesendet werden, um sicherzustellen, dass sie den erwarteten Formaten entsprechen.

- Dokumentationserstellung: Flask-RestX unterstützt die automatische Generierung von API-Dokumentationen, was die Entwicklung und den Einsatz der API erleichtert.

- Flexibilität und Anpassbarkeit: Entwickler haben die Möglichkeit, die Erweiterung nach ihren Anforderungen anzupassen und anzupassen. Sie bietet verschiedene Optionen für die Authentifizierung und Autorisierung.

- Sicherheit: Flask-RestX bietet Mechanismen zur Authentifizierung und Autorisierung, um sicherzustellen, dass die API geschützt ist und nur autorisierten Benutzern zugänglich ist.


## Referenz
**Benutzer:**

- `id`(int): Identifikationsnummer des Nutzers .
- `username`(str):  Benutzername .
- `password`(str):  Passwort .
- `posts`(relationship): Eine Sammlung von Beiträgen, die vom Benutzer erstellt wurden.
- `likes`(relationship): Eine Sammlung von Likes, die vom Benutzer gegeben wurden .

**Beitrag:**

- `id`(int):Identifikationsnummer des Beitrags .
- `title`(str): Der Titel des Beitrags (string).
- `body`:(txt) Der Inhalt des Beitrags .
- `created`(datetime): Der Zeitstempel, wann der Beitrag erstellt wurde .
- `author_id`(int): Die ID des Benutzers, der den Beitrag erstellt hat .
- `likes`: Eine Sammlung von Likes, die der Beitrag erhalten hat .

**Like:**

- `id`(int):  Identifikationsnummer von dem Likes.
- `created`(datetime): Zeit an dem das Like ergeben wurde.
- `author_id`(int): Die ID des Benutzers, der das Like gegeben hat.
- `post_id`(int): Die ID des Beitrags mit dem erhaltenen Like.

  ## Hier kann man mit dem Link auf die API zugreifen um interaktiv zu testen :
   http://127.0.0.1:5000/api/docs/
