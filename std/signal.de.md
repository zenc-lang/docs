# std/sys/signal

Das Modul `std/sys/signal` bietet Primitiven zur Handhabung von Systemsignalen und kapselt die POSIX `signal.h` Funktionalität ein.

## Überblick

- **Signal-Abfangen**: Definition benutzerdefinierter Handler für Signale wie `SIGINT` (Strg+C).
- **Graceful Termination**: Verwendung von Signal-Handlern zur Durchführung von Bereinigungsarbeiten vor dem Beenden.
- **Gängige Konstanten**: Bietet plattformübergreifende Definitionen für Standardsignale.

## Verwendung

```zc
import "std/sys/signal.zc"
import "std/io.zc"

fn on_interrupt(sig: int) {
    println "SIGINT empfangen ({sig}). Bereinigen...";
    exit(0);
}

fn main() {
    Signal::set_handler(Z_SIGINT, on_interrupt);
    println "Warten auf Strg+C...";
    while(true) {}
}
```

## Struktur-Definition

```zc
struct Signal {}
```

## Methoden

### `Signal` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **set_handler** | `Signal::set_handler(sig: int, handler: fn*(int)) -> fn*(int)` | Registriert einen Handler für das angegebene Signal und gibt den vorherigen Handler zurück. |

## Konstanten

### Standardsignale
- `Z_SIGINT`: Unterbrechung durch Tastatur (Strg+C).
- `Z_SIGILL`: Ungültige Instruktion.
- `Z_SIGABRT`: Abort-Signal.
- `Z_SIGFPE`: Gleitkomma-Ausnahme.
- `Z_SIGSEGV`: Segmentierungsfehler (ungültiger Speicherzugriff).
- `Z_SIGTERM`: Beendigungssignal.
