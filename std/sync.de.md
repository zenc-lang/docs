# std/sync

Das Modul `std/sync` bietet eine umfassende Suite von Synchronisationsprimitiven zur Verwaltung des gleichzeitigen Zugriffs auf gemeinsam genutzte Daten und zur Koordination der Thread-Ausführung.

## Überblick

- **Standard-Primitiven**: Enthält `Mutex`, `CondVar`, `RwLock`, `Once`, `Semaphore` und `Barrier`.
- **RAII-Integration**: Alle Primitiven implementieren das `Drop`-Trait, wodurch sichergestellt wird, dass Systemressourcen (wie pthread-Handles) automatisch freigegeben werden.
- **Plattformübergreifend**: Abstrahiert sicher plattformspezifische Eigenheiten (z. B. die Implementierung von `Barrier` und `Semaphore` über Mutexe/Condvars auf macOS).
- **Effizienz**: Schlanke Wrapper um optimierte Synchronisationsbibliotheken auf Systemebene.

## Verwendung

```zc
import "std/sync.zc"

fn main() {
    let m = Mutex::new();
    
    // Scoped Lock (RAII)
    {
        m.lock();
        // Kritischer Abschnitt
        m.unlock();
    } // m wird automatisch freigegeben, wenn es der letzte Besitzer war
    
    // Einmalige Initialisierung
    let once = Once::new();
    once.call(|| {
        println "Initialisiert!";
    });
}
```

## Struktur-Definitionen

### `Mutex`
Ein Mutex (gegenseitiger Ausschluss) zum Schutz gemeinsam genutzter Daten.

### `CondVar`
Eine Bedingungsvariable zur Signalisierung zwischen Threads basierend auf Zustandsänderungen.

### `RwLock`
Ein Reader-Writer-Lock, das mehrere gleichzeitige Leser, aber nur einen Schreiber zulässt.

### `Once`
Stellt sicher, dass ein spezifischer Teil des Initialisierungscodes genau einmal ausgeführt wird.

### `Semaphore`
Ein zählender Semaphor zur Steuerung des Zugriffs auf einen Ressourcen-Pool.

### `Barrier`
Ein Synchronisationspunkt, an dem mehrere Threads warten müssen, bis eine bestimmte Anzahl eingetroffen ist.

## Methoden

### `Mutex` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Mutex::new() -> Mutex` | Erstellt einen neuen Mutex. |
| **lock** | `lock(self)` | Erwirbt die Sperre (blockierend). |
| **try_lock** | `try_lock(self) -> bool` | Versucht, die Sperre zu erwerben, ohne zu blockieren. |
| **unlock** | `unlock(self)` | Gibt die Sperre frei. |

### `CondVar` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `CondVar::new() -> CondVar` | Erstellt eine neue Bedingungsvariable. |
| **wait** | `wait(self, mutex: Mutex*)` | Blockiert den Thread bis zur Signalisierung und gibt den Mutex vorübergehend frei. |
| **signal** | `signal(self)` | Weckt einen Thread auf, der auf diese Bedingung wartet. |
| **broadcast**| `broadcast(self)` | Weckt alle Threads auf, die auf diese Bedingung warten. |

### `RwLock` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `RwLock::new() -> RwLock` | Erstellt ein neues Reader-Writer-Lock. |
| **rdlock** | `rdlock(self)` | Erwirbt eine gemeinsame Lese-Sperre. |
| **wrlock** | `wrlock(self)` | Erwirbt eine exklusive Schreib-Sperre. |
| **unlock** | `unlock(self)` | Gibt jede gehaltene Sperre frei. |

### `Semaphore` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Semaphore::new(value: int) -> Semaphore` | Erstellt einen neuen Semaphor mit dem Initialwert `value`. |
| **wait** | `wait(self)` | Dekrementiert den Semaphor (blockiert, wenn 0). |
| **post** | `post(self)` | Inkrementiert den Semaphor. |
| **value** | `value(self) -> int` | Gibt den aktuellen Wert zurück. |

### `Barrier` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Barrier::new(count: int) -> Barrier` | Erstellt eine neue Barriere für `count` Threads. |
| **wait** | `wait(self) -> bool` | Wartet an der Barriere. Gibt `true` für den designierten Leiter zurück. |

## Speicherverwaltung

Alle Primitiven implementieren `impl Drop` und rufen automatisch ihre interne `free()` Methode auf, um Systemressourcen freizugeben, wenn sie den Gültigkeitsbereich verlassen.
