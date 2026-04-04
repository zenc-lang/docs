# std/utf8

Das Modul `std/utf8` bietet Hilfsmittel für die Arbeit mit Unicode-Codepunkten (`rune`-Typ) und UTF-8-Kodierung.

## Verwendung

```zc
import "std/utf8.zc"

fn main() {
    let r = 'ñ';
    
    if (Utf8::is_alpha(r)) {
        println "{r} ist ein Buchstabe";
    }
}
```

## Methoden

### Abfrage & Identifikation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **is_digit** | `is_digit(r: rune) -> bool` | Gibt wahr zurück, wenn die Rune eine Dezimalziffer ist (0-9). |
| **is_alpha** | `is_alpha(r: rune) -> bool` | Gibt wahr zurück, wenn die Rune ein Buchstabe ist. |
| **is_whitespace** | `is_whitespace(r: rune) -> bool` | Gibt wahr zurück, wenn die Rune ein Leerzeichen ist. |
| **is_upper** | `is_upper(r: rune) -> bool` | Gibt wahr zurück, wenn die Rune ein Großbuchstabe ist. |
| **is_lower** | `is_lower(r: rune) -> bool` | Gibt wahr zurück, wenn die Rune ein Kleinbuchstabe ist. |
| **is_valid** | `is_valid(data: char*, len: usize) -> bool` | Gibt wahr zurück, wenn der Puffer gültige UTF-8-Daten enthält. |

### Transformation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **to_upper** | `to_upper(r: rune) -> rune` | Gibt die Großbuchstaben-Version der Rune zurück. |
| **to_lower** | `to_lower(r: rune) -> rune` | Gibt die Kleinbuchstaben-Version der Rune zurück. |

### Kodierung & Dekodierung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **encode** | `encode(r: rune, buf: char*) -> usize` | Kodiert eine Rune in UTF-8. Gibt die geschriebenen Bytes zurück (1-4). |
| **rune_len** | `rune_len(r: rune) -> usize` | Gibt die Anzahl der für die Kodierung der Rune benötigten Bytes zurück. |
| **decode** | `decode(data: char*, len: usize, consumed: usize*) -> rune` | Dekodiert die erste UTF-8-Sequenz aus den Daten. |
