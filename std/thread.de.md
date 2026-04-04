# std/thread

Das Modul `std/thread` bietet High-Level-Primitiven zur Erstellung und Verwaltung gleichzeitiger Ausführungs-Threads.

## Überblick

- **Native Threads**: Verwendet zugrunde liegende Threading-Mechanismen des Systems (z. B. POSIX-Threads).
- **Closure-Unterstützung**: `Thread::spawn` kann Zen-C-Closures aufnehmen, was einen einfachen Datenaustausch zwischen Threads ermöglicht.
- **Expliziter Lebenszyklus**: Threads müssen explizit mit `join` oder `detach` behandelt werden, um eine ordnungsgemäße Ressourcenbereinigung sicherzustellen.
- **Sicherheit**: Fehler bei der Thread-Erstellung oder -Manipulation werden über `Result<bool>` gemeldet.

## Verwendung

```zc
import "std/thread.zc"

fn worker(id: int) {
    println "Hallo vom Worker {id}";
}

fn main() {
    // Starten mit einer Closure
    let t = Thread::spawn(|| {
        worker(42);
    }).unwrap();
    
    // Explizit auf Abschluss warten
    t.join();
}
```

## Struktur-Definitionen

### `Thread`
Repräsentiert ein Handle für einen gestarteten Thread.
```zc
struct Thread {
    handle: void*;
}
```

## Methoden

### `Thread` Lebenszyklus

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **spawn** | `Thread::spawn(func: fn()) -> Result<Thread>` | Startet einen neuen Thread, der die bereitgestellte Closure oder Funktion ausführt. |
| **join** | `join(self) -> Result<bool>` | Blockiert den aktuellen Thread, bis der gestartete Thread beendet ist. |
| **detach** | `detach(self) -> Result<bool>` | Trennt den Thread ab, sodass er unabhängig laufen kann. Ressourcen werden beim Beenden automatisch freigegeben. |
| **cancel** | `cancel(self) -> Result<bool>` | Sendet eine Abbruch-Anfrage an den Thread. |

### Hilfsfunktionen

| Funktion | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **sleep_ms** | `sleep_ms(ms: int)` | Unterbricht die Ausführung des aktuellen Threads für ca. `ms` Millisekunden. |
