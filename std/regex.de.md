# std/regex

Das Modul `std/regex` bietet Unterstützung für reguläre Ausdrücke basierend auf POSIX `regex.h`.

## Verwendung

```zc
import "std/regex.zc"

fn main() {
    if regex_match("^[a-z]+$", "hello") {
        println "Passt!";
    }
    
    let re = Regex::compile("\\d+");
    let count = re.count("123 abc 456");
    re.destroy();
}
```

## Struktur-Definitionen

### `Regex`

Repräsentiert einen kompilierten regulären Ausdruck.

```zc
struct Regex {
    // Interne Handles
}
```

### `Match`

Repräsentiert eine erfolgreiche Übereinstimmung (Match).

```zc
struct Match {
    text: char*;
    start: int;
    len: int;
}
```

## Methoden

### Regex-Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **compile** | `Regex::compile(pattern: char*) -> Regex` | Kompiliert ein Regex-Muster mit Standard-Flags. |
| **compile_with_flags** | `Regex::compile_with_flags(pattern: char*, flags: int) -> Regex` | Kompiliert mit benutzerdefinierten POSIX-Flags. |
| **destroy** | `destroy(self)` | Gibt den kompilierten Regex frei. |

### Übereinstimmung & Suche

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **match** | `match(self, text: char*) -> bool` | Gibt wahr zurück, wenn das Muster irgendwo in `text` übereinstimmt. |
| **find** | `find(self, text: char*) -> Option<Match>` | Gibt die erste Übereinstimmung einschließlich Position und Länge zurück. |
| **count** | `count(self, text: char*) -> int` | Gibt die Anzahl der nicht überlappenden Übereinstimmungen zurück. |
| **split** | `split(self, text: char*) -> Vec<String>` | Teilt den Text anhand des Musters auf. |

### Match-Zugriff

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **as_string** | `as_string(self) -> char*` | Gibt einen Zeiger auf den Anfang der Übereinstimmung zurück. |
| **end** | `end(self) -> int` | Gibt den Index nach dem letzten Zeichen der Übereinstimmung zurück. |

### Statische Hilfsfunktionen

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **regex_match** | `regex_match(pattern: char*, text: char*) -> bool` | Schnelle Prüfung auf Übereinstimmung. |
| **regex_find** | `regex_find(pattern: char*, text: char*) -> Option<Match>` | Findet die erste Übereinstimmung. |
| **regex_count** | `regex_count(pattern: char*, text: char*) -> int` | Zählt alle Übereinstimmungen. |
| **regex_split** | `regex_split(pattern: char*, text: char*) -> Vec<String>` | Teilt Text nach Muster auf. |
