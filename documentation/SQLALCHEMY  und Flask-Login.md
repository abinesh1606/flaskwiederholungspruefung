# SQLAlchemy und Flask-Login
## SQLite Database Access -  SQL vs SQLAlchemy
### Hintergrund
Bei der Entwicklung von Anwendungen, die Datenbankfunktionalität erfordern, insbesondere solche, die leichte, eingebettete Datenbanklösungen benötigen, ist SQLite aufgrund seiner Einfachheit, Portabilität und geringen Installationsanforderungen oft die bevorzugte Wahl. Allerdings stehen Entwickler vor der Entscheidung, wie sie mit SQLite-Datenbanken interagieren sollen: indem sie Roh-SQL-Abfragen direkt verwenden oder eine Bibliothek wie SQLAlchemy einsetzen, die ein objekt-relationales Mapping (ORM) Framework sowie eine SQL-Ausdruckssprache bereitstellt.
### Mögliche Optionen
 - SQL direkt verwenden: Fortfahren mit der Interaktion mit SQLite-Datenbanken unter Verwendung von Roh-SQL-Abfragen.

- SQLAlchemy verwenden: Übergang zu SQLAlchemy zur Interaktion mit SQLite-Datenbanken.
### Vorteile von SQLAlchemy
- ORM-Funktionen: SQLAlchemy macht die Interaktion mit der Datenbank einfacher, indem es Low-Level-SQL-Operationen versteckt und es erlaubt, direkt mit Python-Objekten zu arbeiten.
- Abstraktion: SQLAlchemy versteckt die Unterschiede zwischen verschiedenen Datenbanken, was eine spätere Umstellung auf andere Datenbanken mit minimalen Änderungen am Code ermöglicht.
- Code-Wartbarkeit: SQLAlchemy fördert sauberen Code und einfache Wartung, indem es die Datenbanklogik in Python-Klassen und Methoden verpackt.
- Sicherheit: SQLAlchemy hilft, Sicherheitsrisiken wie SQL-Injection-Angriffe zu reduzieren, indem es Abfragen automatisch parametrisiert.
- Abfrage-Erstellung: SQLAlchemy bietet eine intuitive Möglichkeit, Abfragen dynamisch zu erstellen, was die Arbeit mit komplexen Abfrage-Szenarien erleichtert.

 ### Nachteile

- Einarbeitungszeit: Die Umstellung auf SQLAlchemy erfordert möglicherweise, dass Entwickler neue Konzepte und APIs erlernen, insbesondere wenn sie mit ORM-Prinzipien nicht vertraut sind.
- Performance-Overhead: Obwohl SQLAlchemy Abstraktionsvorteile bietet, kann es im Vergleich zur direkten Ausführung von Roh-SQL-Abfragen einen leichten Leistungsüberhang geben, insbesondere bei einfachen Operationen.
### Auswirkungen 
- Verbesserte Code-Wartbarkeit: Der Übergang zu SQLAlchemy verbessert die Code-Wartbarkeit, indem die Datenbanklogik innerhalb von Python-Klassen und -Methoden gekapselt wird.
- Erhöhte Sicherheit: Die ORM-Funktionen von SQLAlchemy helfen, Sicherheitsrisiken im Zusammenhang mit direkten SQL-Abfragen zu mindern, wie z. B. SQL-Injektionsangriffe.
- Mögliche Leistungseinbußen: Die Verwendung von SQLAlchemy kann mit geringfügigen Leistungseinbußen verbunden sein im Vergleich zur direkten Ausführung von SQL-Abfragen.

### Entschluss
Ich habe beschlossen, von der Verwendung direkter SQL-Abfragen auf SQLAlchemy umzusteigen, um mit SQLite-Datenbanken zu interagieren. Zu dieser Entscheidung bin ich gekommen nachdem ich mich mit den Vorteilen und Nachteilen von SQLAlchemy auseinadergesetzt habe.
![mermaidchart_flasklogin](https://github.com/abinesh1606/flaskwiederholungspruefung/assets/149621097/1f2e5f5e-70de-4c0f-9cd0-740a56566c0a)


## Flask-Login

### Hintergrund
Authentifizierung ist ein entscheidender Aspekt von Webanwendungen, der sicherstellt, dass Benutzer sicher auf Ressourcen zugreifen und mit der Anwendung interagieren können. Im Kontext einer Flask-basierten Webanwendung besteht die Notwendigkeit, eine authentifizierte Sitzungsbasierte Authentifizierung zu implementieren, um Benutzeranmeldesitzungen und Zugriffskontrolle zu verwalten. Flask-Login ist eine beliebte Erweiterung für Flask, die Sitzungsverwaltung und Benutzerauthentifizierungsfunktionen von Haus aus bietet.

### Mögliche Optionen

- Benutzerdefinierte Authentifizierungsimplementation: Entwicklung einer benutzerdefinierten Authentifizierungslösung von Grund auf.
- Verwendung von Flask-Login: Nutzung der Flask-Login-Erweiterung für die Sitzungsverwaltung und Benutzerauthentifizierung.

### Vorteile

- Einfachheit: Flask-Login vereinfacht die Implementierung der sitzungsbasierten Authentifizierung, indem es sofort einsatzbereite Funktionen für die Verwaltung von Benutzersitzungen und den Authentifizierungszustand bereitstellt.
- Integration mit Flask: Flask-Login integriert nahtlos in Flask-Anwendungen und nutzt die vorhandenen Funktionen und Konventionen von Flask.
- Sitzungsverwaltung: Flask-Login übernimmt die Sitzungsverwaltung, einschließlich der Funktionen zum Ein- und Ausloggen und der Verfolgung von Benutzersitzungen, wodurch der Bedarf an manuellem Code zur Sitzungsverwaltung verringert wird.
- Benutzerverwaltung: Flask-Login bietet Hilfsprogramme zur Verwaltung der Benutzerauthentifizierung, wie z. B. Hashen von Passwörtern, Laden von Benutzern und Authentifizierungsrückrufe.
- Flexibilität: Flask-Login bietet Flexibilität bei der Anpassung des Authentifizierungsverhaltens und ermöglicht benutzerdefinierte Ansichten für Ein- und Ausloggen, Authentifizierungsmethoden und Strategien zur Verwaltung von Benutzersitzungen.

  ### Nachteile

 - Einarbeitungszeit: Mit Flask-Login ist möglicherweise eine Lernphase verbunden, insbesondere für Entwickler, die mit Flask-Erweiterungen oder der API von Flask-Login nicht vertraut sind.
- Abhängigkeit: Die Integration von Flask-Login fügt dem Projekt eine Abhängigkeit hinzu, was die Komplexität und den Wartungsaufwand erhöhen kann.

  ### Auswirkungen
-  Effiziente Authentifizierungsimplementierung: Flask-Login vereinfacht die Implementierung der authentifizierungsbasierten Sitzungsverwaltung und reduziert dadurch die Entwicklungszeit und den Aufwand.
- Verbesserte Sicherheit: Flask-Login hilft, gängige Sicherheitsrisiken im Zusammenhang mit der Sitzungsverwaltung zu minimieren, wie etwa Session-Fixierung und Session-Hijacking, indem bewährte Verfahren für die Sitzungsverwaltung und Benutzerauthentifizierung implementiert werden.
- Abhängigkeitsmanagement: Die Integration von Flask-Login fügt dem Projekt eine Abhängigkeit hinzu, die zusammen mit anderen Abhängigkeiten verwaltet und aktualisiert werden muss.

  ### Entschluss

  Ich habe beschlossen, die authentifizierungsbasierte Sitzungsverwaltung für die Webanwendung mit Flask-Login umzusetzen, nachdem ich die obengenannten Vorteile und Nachteile gegeneinander abgewägt habe.


![mermaidchart_flasklogin](https://github.com/abinesh1606/flaskwiederholungspruefung/assets/149621097/5a9f2a31-c614-43f9-aad9-28b34f8b2a4f)




