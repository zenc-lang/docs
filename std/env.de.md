# std/env

Das Modul `std/env` bietet plattformübergreifenden Zugriff auf Prozess-Umgebungsvariablen.

## Überblick

- **Schlüssel-Wert-Zugriff**: Einfache API zum Abrufen, Setzen und Löschen von Umgebungsvariablen.
- **Geliehen oder Eigenhändig**: Wählen Sie zwischen `get` (gibt einen geliehenen C-String zurück) und `get_dup` (gibt einen eigenen, auf dem Heap allokierten `String` zurück).
- **Plattformübergreifend**: Abstrahiert sicher die zugrunde liegenden Systemaufrufe für die Umgebungsmanipulation.

## Verwendung

```zc
import "std/env.zc"

fn main() {
    // Setzen einer Umgebungsvariablen
    Env::set("MY_APP_MODE", "development");

    // Abrufen (Geliehen)
    match Env::get("MY_APP_MODE") {
        Some(val) => println "Modus: {val}",
        None => println "Modus nicht gesetzt"
    }

    // Abrufen (Eigener String für RAII)
    match Env::get_dup("HOME") {
        Some(home) => {
             println "Heimatverzeichnis: {home}";
             // home wird automatisch freigegeben
        }
        None => println "HOME nicht gefunden"
    }
}
```

## Enum-Definition

```zc
enum EnvRes {
    OK,
    ERR,
}
```

## Methoden

### Zugriff & Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **get** | `Env::get(name: char*) -> Option<char*>` | Ruft einen geliehenen Zeiger auf eine Umgebungsvariable ab. Nicht freigeben. |
| **get_dup** | `Env::get_dup(name: char*) -> Option<String>` | Ruft eine Umgebungsvariable als neues `String`-Objekt ab. |

### Modifikation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **set** | `Env::set(name: char*, value: char*) -> EnvRes` | Setzt oder aktualisiert eine Umgebungsvariable. |
| **unset** | `Env::unset(name: char*) -> EnvRes` | Entfernt eine Umgebungsvariable aus dem aktuellen Prozess. |
