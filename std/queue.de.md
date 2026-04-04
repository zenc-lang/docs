# std/queue

`Queue<T>` ist eine generische First-In-First-Out (FIFO) Warteschlange, die als **Ringpuffer (Circular Buffer)** implementiert ist.

## Verwendung

```zc
import "std/queue.zc"

fn main() {
    let q = Queue<int>::new();
    
    q.push(1);
    q.push(2);
    q.push(3);
    
    // Pop gibt eine Option<T> zurück
    if (q.pop().is_some()) {
        println "Gepoppt: {q.pop().unwrap()}"; // 1
    }
}
```

## Implementierungsdetails

- **Ringpuffer**: Verwendet einen zirkulären Puffer mit `head`- und `tail`-Indizes.
- **Leistung**:
    - `push`: **Amortisiert O(1)** (passt die Größe an, wenn voll).
    - `pop`: **O(1)** (rückt den Head-Index vor).
    - `clone`: **O(N)**.
- **Sicherheit**: Sicherer Umgang mit Speicherumbruch und Größenänderung.

## Struktur-Definition

```zc
struct Queue<T> {
    data: T*;
    cap: usize;
    head: usize;
    tail: usize;
    count: usize;
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Queue<T>::new() -> Queue<T>` | Erstellt eine neue, leere Warteschlange. |
| **clone** | `clone(self) -> Queue<T>` | Erstellt eine tiefe Kopie der Warteschlange. |

### Modifikation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **push** | `push(self, value: T)` | Fügt ein Element am Ende der Warteschlange hinzu. |
| **pop** | `pop(self) -> Option<T>` | Entfernt und gibt das Element an der Vorderseite zurück. Gibt `None` zurück, wenn leer. |
| **clear** | `clear(self)` | Entfernt alle Elemente aus der Warteschlange. |

### Zugriff & Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Gibt die Anzahl der Elemente zurück. |
| **is_empty** | `is_empty(self) -> bool` | Gibt `true` zurück, wenn die Warteschlange leer ist. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **free** | `free(self)` | Gibt den internen Puffer frei. |
| **Trait** | `impl Drop for Queue` | Ruft beim Verlassen des Gültigkeitsbereichs automatisch `free()` auf. |
