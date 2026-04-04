# std/time

Das Modul `std/time` bietet Hilfsmittel für hochpräzise Zeitmessung und das Unterbrechen von Threads.

## Überblick

- **Millisekunden-Präzision**: `Time::now()` gibt die aktuelle Systemzeit in Millisekunden zurück.
- **Duration-Typ**: Die Struktur `Duration` ermöglicht intuitive Berechnungen von Zeitspannen.
- **Einfaches Schlafen**: Leicht zu bedienende Funktionen zum Aussetzen der Ausführung.
- **Leichtgewichtig**: Minimaler Overhead, kapselt Standard-Zeitfunktionen auf Systemebene ein.

## Verwendung

```zc
import "std/time.zc"

fn main() {
    let start = Time::now();
    
    // 1,5 Sekunden schlafen
    Time::sleep(Duration::from_ms(1500));
    
    let end = Time::now();
    println "Vergangen: {end - start} ms";
}
```

## Struktur-Definitionen

### `Duration`
Repräsentiert eine Zeitspanne.
```zc
struct Duration {
    millis: U64;
}
```

### `Time`
Statische Hilfsstruktur für Systemzeit-Operationen.
```zc
struct Time {}
```

## Methoden

### `Duration` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **from_ms** | `Duration::from_ms(ms: U64) -> Duration` | Erstellt eine `Duration` aus einer Anzahl von Millisekunden. |
| **from_secs** | `Duration::from_secs(s: U64) -> Duration` | Erstellt eine `Duration` aus einer Anzahl von Sekunden. |

### `Time` Statische Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **now** | `Time::now() -> U64` | Gibt die aktuelle Systemzeit in Millisekunden seit der Epoche zurück. |
| **sleep** | `Time::sleep(d: Duration)` | Unterbricht den aktuellen Thread für die angegebene `Duration`. |
| **sleep_ms** | `Time::sleep_ms(ms: U64)` | Unterbricht den aktuellen Thread für die angegebene Anzahl von Millisekunden. |
