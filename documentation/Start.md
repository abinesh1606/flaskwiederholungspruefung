# Flaskwiederholungsprüfung von Abinesh Gulasingam
**Im folgenden werden erneut die jeweligen Aufgabenstellungen aufgelistet**
## SQLAlchemyund Flask-Login


1. **Führen Sie SQLAlchemy in die Applikation ein:**
   -
   Erstellen Sie das Datenmodell (User und Post) unter Nutzung der SQLAlchemy-Klasse „Model“. Verwenden Sie dazu den folgenden [Link](LINK).
   
   Ersetzen Sie alle CRUD-Operationen durch geeignete SQLAlchemy-Methoden. Weitere Informationen finden Sie [hier](LINK).
   
   Entfernen Sie jeglichen Code, der durch den Wechsel von direkter sqlite3-Nutzung zu SQLAlchemy überflüssig wurde.

2. **Erstellen Sie ein Decision Record:**
   
   Nutzen Sie ein Decision Record, mit dem Sie die beiden Lösungen (vorher / nachher) gegeneinander abwägen.
   
   Schenken Sie dem Abschnitt „regarded options“ besondere Aufmerksamkeit.

3. **Führen Sie Flask-Login in die Applikation ein:**
   
   Verwenden Sie Flask-Login für die Login- und Logout-Prozesse.
   
   Nutzen Sie Flask-Login um sicherzustellen, dass nur eingeloggte Benutzer Blogposts erstellen, bearbeiten und löschen können.
   
   Implementieren Sie eine „Remember me“-Funktionalität. Nutzen Sie dafür den folgenden [Link](LINK).
   
   Entfernen Sie jeglichen Code, der durch die Einführung von Flask-Login überflüssig wurde.

4. **Erstellen Sie ein Decision Record zur Abwägung der beiden Lösungen (vorher / nachher):**
   
   Dokumentieren Sie die Vor- und Nachteile der beiden Lösungen in einem Decision Record.


2. ## Like-Button

5. **Implementieren Sie einen Like-Button für einzelne Blog-Posts:**
   
   Mit dem Like-Button soll die Leserin anzeigen können, dass ihr ein bestimmter Blog-Post gefällt.
   
   Ein gegebener Like kann wieder zurückgenommen werden (ggf. nur unter bestimmten Voraussetzungen).
   
   Neben dem Like-Button wird die Gesamtzahl aller bisher hinterlassenen „Likes“ angezeigt.

6. **Erstellen Sie ein Decision Record zur Implementierung des Like-Buttons:**
   
   Erklären Sie mehrere Lösungsansätze zur Implementierung des Like-Buttons und wägen Sie diese gegeneinander ab.
   
   Falls Sie mehrere Aspekte diskutieren möchten, erstellen Sie zur besseren Übersicht mehrere Decision Records.
   
   Um die Anschaulichkeit zu erhöhen, dürfen Sie auf Modellierungswerkzeuge wie Mermaid zurückgreifen.
   
   Tipp: Sie können Mermaid-Diagramme nativ in Ihre Dokumentation einbinden. Weitere Informationen finden Sie [hier](LINK).

## RESTful API
7. **Erstellen Sie ein RESTful API:**
   
   Nutzen Sie zur Code-Organisation das Blueprint-Feature von Flask; exponierte Funktionalitäten:
   
   - POST Request zum Anlegen eines neuen Blog-Posts in der Datenbank
   - Zwei GET Requests um (1) alle Blog-Posts auszulesen, sowie (2) den Blog-Post mit einer bestimmten ID auszulesen
   - PATCH Request zum Aktualisieren folgender Datenfelder eines bestimmten Blog-Posts: title, body, author_id
   - DELETE Request um den Blog-Post mit einer bestimmten ID aus der Datenbank zu löschen
   -
   Payloads werden im JSON-Format ausgetauscht. [Hier](LINK) finden Sie Inspiration.
   -
   Beispiel (von dem Sie abweichen können): Ein GET Request auf `api/posts/11` retourniert `{“id”: 11, “title”: “Hello, world!”, …}`
   -
   Tipp: Verwenden Sie Tools wie Talend API Tester oder cURL um Ihr API zu testen.

8. **Zur Implementierungs-Unterstützung wägen Sie diese Flask-Erweiterungen mittels Decision Record ab:**
   
   - Flask-RESTful: [Dokumentation](https://flask-restful.readthedocs.io/en/latest/)
   - Flask-Restless-NG: [Dokumentation](https://flask-restless-ng.readthedocs.io/en/latest/)
   - Flask-RESTX: [Dokumentation](https://flask-restx.readthedocs.io/en/latest/)
   - Flask-smorest: [Dokumentation](https://flask-smorest.readthedocs.io/en/latest/index.html)

9. **Erstellen Sie eine API-Referenz-Dokumentation:**
   -
   Folgen Sie dem Beispiel der Uber API Reference, um Ihre eigene Dokumentation geeignet zu strukturieren.

