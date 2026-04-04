# std/vec

`Vec<T>` ist ein zusammenhängender, wachsender Array-Typ. Es ist das standardmäßige dynamische Array in Zen-C.

## Überblick

- **Generisch**: Funktioniert mit jedem Typ `T`.
- **Dynamisch**: Passt die Größe automatisch an, wenn Elemente hinzugefügt werden.
- **Sicher**: Grenzprüfungen beim Zugriff (löst Panic im Fehlerfall aus).
- **RAII**: Gibt Speicher automatisch frei, wenn der Gültigkeitsbereich verlassen wird (implementiert `Drop`).

## Verwendung

```zc
import "std/vec.zc"

fn main() {
    let v = Vec<int>::new();
    v.push(10);
    v.push(20);
    
    // Iteration
    for x in &v {
        println "{(*x)}";
    }
} // v wird hier automatisch freiggeben
```

## Struktur-Definition

```zc
struct Vec<T> {
    data: T*;
    len: usize;
    cap: usize;
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Vec<T>::new() -> Vec<T>` | Erstellt einen neuen, leeren Vektor. Allokiert erst beim ersten Push Speicher. |
| **with_capacity** | `Vec<T>::with_capacity(cap: usize) -> Vec<T>` | Erstellt einen neuen Vektor mit einer Anfangskapazität von `cap`. Nützlich zur Optimierung, wenn die Anzahl der Elemente vorab bekannt ist. |

### Modifikation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **push** | `push(self, item: T)` | Fügt ein Element am Ende hinzu. Löst Panic aus, wenn die Allokation fehlschlägt. |
| **pop** | `pop(self) -> T` | Entfernt das letzte Element und gibt es zurück. Löst Panic aus, wenn leer. |
| **pop_opt** | `pop_opt(self) -> Option<T>` | Entfernt das letzte Element und gibt `Some(val)` zurück. Gibt `None` zurück, wenn leer. Sicherer Gebrauch. |
| **insert** | `insert(self, idx: usize, item: T)` | Fügt ein Element bei `idx` ein. Verschiebt Elemente nach rechts. Löst Panic aus, wenn `idx > len`. |
| **remove** | `remove(self, idx: usize) -> T` | Entfernt das Element bei `idx` und gibt es zurück. Verschiebt Elemente nach links. Löst Panic aus, wenn `idx >= len`. |
| **append** | `append(self, other: Vec<T>)` | Hängt alle Elemente von `other` an `self` an. Konsumiert `other` (Move-Semantik). |
| **clear** | `clear(self)` | Entfernt alle Werte. Hat keinen Einfluss auf die allokierte Kapazität. |
| **reverse** | `reverse(self)` | Kehrt die Reihenfolge der Elemente in-place um. |

### Zugriff

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **get** | `get(self, idx: usize) -> T` | Gibt eine Kopie des Elements bei `idx` zurück. Löst Panic aus, wenn außerhalb der Grenzen. |
| **get_ref** | `get_ref(self, idx: usize) -> T*` | Gibt einen Zeiger auf das Element bei `idx` zurück. Löst Panic aus, wenn außerhalb der Grenzen. Nützlich zur Vermeidung von Kopien. |
| **set** | `set(self, idx: usize, item: T)` | Überschreibt das Element bei `idx`. Löst Panic aus, wenn außerhalb der Grenzen. |
| **first** | `first(self) -> T` | Gibt eine Kopie des ersten Elements zurück. Löst Panic aus, wenn leer. |
| **last** | `last(self) -> T` | Gibt eine Kopie des letzten Elements zurück. Löst Panic aus, wenn leer. |

### Hilfsmittel

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Gibt die Anzahl der Elemente zurück. |
| **is_empty** | `is_empty(self) -> bool` | Gibt `true` zurück, wenn der Vektor keine Elemente enthält. |
| **contains** | `contains(self, item: T) -> bool` | Gibt `true` zurück, wenn der Vektor ein Element gleich `item` enthält (byteweise). |
| **clone** | `clone(self) -> Vec<T>` | Gibt einen neuen Vektor mit einer tiefen Kopie der Daten zurück. |
| **eq** | `eq(self, other: Vec<T>*) -> bool` | Gibt `true` zurück, wenn zwei Vektoren byteweise gleich sind. Nimmt einen Zeiger, um das Verschieben von `other` zu vermeiden. |

### Operatoren

Zen-C unterstützt Operatorüberladung. `Vec<T>` implementiert folgendes:

| Operator | Methode | Beschreibung |
| :--- | :--- | :--- |
| `+` | **add** | `v1 + &v2`. Gibt einen neuen Vektor zurück (Konkatenation). |
| `+=` | **add_assign** | `v1 += &v2`. Hängt `v2` an `v1` an. |
| `==` | **eq** | `v1 == &v2`. Strukturelle Gleichheitsprüfung. |
| `!=` | **neq** | `v1 != &v2`. Strukturelle Ungleichheitsprüfung. |
| `<<` | **shl** | `v << item`. Schiebt `item` ans Ende. |
| `>>` | **shr** | `v >> &item`. Poppt das letzte Element in `item`. |
| `*` | **mul** | `v * n`. Gibt einen neuen Vektor zurück, dessen Elemente `n`-mal wiederholt werden. |
| `*=` | **mul_assign** | `v *= n`. Wiederholt Elemente in-place `n`-mal. |
| `[]` | **get** / **set** | `v[i]` und `v[i] = x`. Standard-Indizierung. |

### Iteration

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> VecIter<T>` | Gibt einen Iterator zurück, der Kopien liefert. Wird von `for x in v` verwendet. |
| **iter_ref** | `iter_ref(self) -> VecIterRef<T>` | Gibt einen Iterator zurück, der Zeiger liefert. Wird von `for x in &v` oder `for x in v.iter_ref()` verwendet. Ermöglicht In-place-Modifikationen. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **Free** | `free(self)` | Gibt Speicher manuell frei. Sicher, mehrmals aufgerufen zu werden. |
| **Forget** | `forget(self)` | Trennt den Speicherpuffer vom Vektor (setzt Felder auf 0). Verhindert, dass `Drop` den Speicher freigibt. Nützlich für die Implementierung von Move-Semantik oder Besitzübertragung. |
| **Trait** | `impl Drop for Vec` | Ruft beim Verlassen des Gültigkeitsbereichs automatisch `free()` auf. |
