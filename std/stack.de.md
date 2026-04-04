# std/stack

Das Modul `std/stack` bietet eine LIFO (Last-In, First-Out) Stapelspeicher-Datenstruktur (Stack).

## Verwendung

```zc
import "std/stack.zc"

fn main() {
    let s = Stack<int>::new();
    s.push(10);
    s.push(20);
    
    let top = s.pop(); // Some(20)
} // s wird hier automatisch freigegeben
```

## Struktur-Definition

```zc
struct Stack<T> {
    // Interne Implementierungsdetails
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Stack<T>::new() -> Stack<T>` | Erstellt einen neuen, leeren Stack. |
| **clone** | `clone(self) -> Stack<T>` | Erstellt eine tiefe Kopie des Stacks. |

### Modifikation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **push** | `push(self, value: T)` | Legt einen Wert oben auf den Stack. |
| **pop** | `pop(self) -> Option<T>` | Entfernt und gibt das oberste Element des Stacks zurück. Gibt `None` zurück, wenn leer. |
| **clear** | `clear(self)` | Entfernt alle Elemente aus dem Stack. |

### Zugriff & Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Gibt die Anzahl der Elemente im Stack zurück. |
| **is_empty** | `is_empty(self) -> bool` | Gibt `true` zurück, wenn der Stack keine Elemente enthält. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **free** | `free(self)` | Gibt den Speicher des Stacks manuell frei. |
| **Trait** | `impl Drop for Stack` | Ruft beim Verlassen des Gültigkeitsbereichs automatisch `free()` auf. |
