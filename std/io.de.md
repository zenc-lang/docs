# std/io

Das Modul `std/io` bietet Standard-Eingabe/Ausgabe-Funktionen, einschließlich formatierter Ausgabe nach stdout und robustem Lesen von stdin.

## Überblick

- **Formatierte Ausgabe**: Bietet `print` und `println` mit Unterstützung für C-Style Format-Spezifizierer (`%s`, `%d`, etc.).
- **String-Formatierung**: Mehrere Optionen zum Formatieren in statische, benutzerdefinierte oder auf dem Heap allokierte Puffer.
- **Unicode-Unterstützung**: Enthält `read_rune` zum Lesen einzelner UTF-8-Zeichen von stdin.
- **Konvertierungs-Hilfsprogramme**: Einfache Methoden zum Konvertieren von Ganzzahlen und Runen in Strings.

## Verwendung

```zc
import "std/io.zc"

fn main() {
    // Grundlegendes Drucken
    println("Hallo, %s!", "Zen-C");
    
    // Lesen einer Zeile der Eingabe
    print("Geben Sie Ihren Namen ein: ");
    autofree let name = readln();
    
    if name != NULL {
        println("Begrüßung, %s", name);
    }
}
```

## Methoden

### Ausgabe

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **print** | `print(fmt: char*, ...) -> int` | Gibt formatierte Ausgabe nach stdout aus. |
| **println** | `println(fmt: char*, ...) -> int` | Gibt formatierte Ausgabe nach stdout aus, gefolgt von einem Zeilenumbruch. |

### Eingabe

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **readln** | `readln() -> char*` | Liest eine Zeile von stdin. Gibt einen auf dem Heap allokierten String zurück (Aufrufer muss diesen freigeben). |
| **read_rune** | `read_rune() -> rune` | Liest ein einzelnes UTF-8-Zeichen (Rune) von stdin. |

### Formatierung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **format** | `format(fmt: char*, ...) -> char*` | Formatiert in einen internen statischen Puffer. **Warnung**: Nicht threadsicher. |
| **format_into** | `format_into(buf: char*, size: usize, fmt: char*, ...) -> int` | Formatiert in einen vom Benutzer bereitgestellten Puffer spezifischer Größe. |
| **format_new** | `format_new(fmt: char*, ...) -> char*` | Formatiert in einen neuen auf dem Heap allokierten Puffer. Aufrufer muss diesen freigeben. |

### Konvertierung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **itos** | `itos(n: int) -> char*` | Konvertiert `n` in einen String in einem statischen Puffer. |
| **itos_new** | `itos_new(n: int) -> char*` | Konvertiert `n` in einen auf dem Heap allokierten String. |
| **utos** | `utos(n: uint) -> char*` | Konvertiert vorzeichenloses `n` in einen String in einem statischen Puffer. |
