# Like-Button
## Implementierung eines "Gefällt mir"-Buttons für einzelne Blog-Beiträge
### Hintergrund
In der Entwicklung der Blog-Anwendung soll eine Funktion eingebaut werden, die es den Lesern ermöglicht, ihre Zustimmung zu bestimmten Blog-Beiträgen auszudrücken - das Ganze über eine "Gefällt mir"-Schaltfläche. Diese Schaltfläche zeigt auch an, wie viele Personen den Beitrag mögen. Zusätzlich soll es möglich sein, ein Like wieder zurückzuziehen.
### Mögliche Optionen
- Serverseitige Implementierung mit Flask: Implementierung der Like-Schaltfläche unter Verwendung von Flask zur Verarbeitung von Datenbankinteraktionen.
- Clientseitige Implementierung mit JavaScript: Implementierung der Like-Schaltfläche unter Verwendung von JavaScript zum Senden von Backend-Anfragen.
### Entschluss
Ich habe beschlossen, die Like-Schaltflächen-Funktion mit JavaScript zu implementieren, um Backend-Anfragen für Datenbankinteraktionen zu senden.
### Begründung

Die Client-seitige Implementierung mit JavaScript bietet ein reaktionsschnelles und interaktives Benutzererlebnis und entlastet gleichzeitig die Verarbeitung auf dem Server. Dieser Ansatz stellt sicher, dass Datenbankinteraktionen sicher auf der Serverseite behandelt werden, wodurch das Risiko von Manipulationen oder Missbrauch minimiert wird. Darüber hinaus ermöglicht die Verwendung von JavaScript zum Senden von Backend-Anfragen eine effiziente Handhabung von Likes, ohne die gesamte Seite neu laden zu müssen, was das Benutzererlebnis verbessert.

### Ausiwkrungen
- Verbessertes Benutzererlebnis: Die mit JavaScript implementierte Like-Button-Funktion bietet ein nahtloses und reaktionsschnelles Benutzererlebnis.
- Sichere Datenbankinteraktionen: Backend-Anfragen, die von der Client-Seite gesendet werden, stellen sicher, dass Datenbankinteraktionen sicher auf dem Server behandelt werden, wodurch Sicherheitsrisiken minimiert werden.
- Erhöhte Komplexität auf der Frontend-Seite: Die Implementierung der Like-Button-Funktion mit JavaScript erhöht die Komplexität des Frontend-Codebasis.
- Potenzielle Leistungsauswirkungen: Die Verarbeitung auf der Client-Seite kann je nach Netzwerklatenz und Serverantwortzeiten zu leichten Verzögerungen bei der Handhabung von Likes führen.






