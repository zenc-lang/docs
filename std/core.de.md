# std/core

Das Modul `std/core` bietet die grundlegendsten Definitionen und Fehlerbehandlungs-Primitiven für Zen-C-Programme. Es wird implizit von den meisten anderen Standardbibliotheken benötigt.

## Überblick

- **Standard-Header**: Enthält kritische C-Header wie `stdlib.h`, `stdio.h` und `stdbool.h`.
- **Panic-Mechanismus**: Bietet das `panic`-Makro für nicht behebbare Fehlermeldungen.
- **Prozesssteuerung**: Enthält grundlegende Funktionen zur Prozesssteuerung wie `exit`.

## Methoden

### Fehlerbehandlung

| Methode/Makro | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **panic** | `panic(msg: char*)` | Gibt eine formatierte Fehlermeldung aus, einschließlich Datei, Zeile und Funktion, und beendet dann den Prozess. |

### Prozesssteuerung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **exit** | `exit(code: int)` | Beendet den Prozess sofort mit dem angegebenen Rückgabecode. |
