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

 ## Nachteile

- Einarbeitungszeit: Die Umstellung auf SQLAlchemy erfordert möglicherweise, dass Entwickler neue Konzepte und APIs erlernen, insbesondere wenn sie mit ORM-Prinzipien nicht vertraut sind.
- Performance-Overhead: Obwohl SQLAlchemy Abstraktionsvorteile bietet, kann es im Vergleich zur direkten Ausführung von Roh-SQL-Abfragen einen leichten Leistungsüberhang geben, insbesondere bei einfachen Operationen.
## Auswirkungen 
- Verbesserte Code-Wartbarkeit: Der Übergang zu SQLAlchemy verbessert die Code-Wartbarkeit, indem die Datenbanklogik innerhalb von Python-Klassen und -Methoden gekapselt wird.
- Erhöhte Sicherheit: Die ORM-Funktionen von SQLAlchemy helfen, Sicherheitsrisiken im Zusammenhang mit direkten SQL-Abfragen zu mindern, wie z. B. SQL-Injektionsangriffe.
- Mögliche Leistungseinbußen: Die Verwendung von SQLAlchemy kann mit geringfügigen Leistungseinbußen verbunden sein im Vergleich zur direkten Ausführung von SQL-Abfragen.

## Entschluss
Ich habe beschlossen, von der Verwendung direkter SQL-Abfragen auf SQLAlchemy umzusteigen, um mit SQLite-Datenbanken zu interagieren.
![Screenshot 2024-04-05 092647](https://github.com/abinesh1606/flaskwiederholungspruefung/assets/149621097/ce31ae81-8983-46ee-aa6e-ae121c65e516)



