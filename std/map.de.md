# std/map

`Map<V>` ist eine generische Hash-Map-Implementierung, die String-Schlüssel auf Werte vom Typ `V` abbildet.

## Verwendung

```zc
import "std/map.zc"

fn main() {
    let m = Map<int>::new();
    
    m.put("one", 1);
    m.put("two", 2);
    
    if (m.contains("one")) {
        let val = m.get("one");
        println "{val.unwrap()}";
    }
    
    m.remove("two");
} // m wird hier automatisch freigegeben
```

## Struktur-Definition

```zc
struct Map<V> {
    keys: char**;
    vals: V*;
    // ... interne Felder
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Map<V>::new() -> Map<V>` | Erstellt eine neue, leere Map. |

### Iteration

Sie können über die Schlüssel-Wert-Paare der Map mit einer `for`-Schleife iterieren.

```zc
let m = Map<int>::new();
m.put("a", 1);

for entry in m {
    println "Schlüssel: {entry.key}, Wert: {entry.val}";
}
```

Der Iterator liefert eine `MapEntry<V>`-Struktur:
```zc
struct MapEntry<V> {
    key: char*;
    val: V;
}
```

### Modifikation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **put** | `put(self, key: char*, val: V)` | Fügt ein Schlüssel-Wert-Paar ein oder aktualisiert dieses. |
| **remove** | `remove(self, key: char*)` | Entfernt einen Schlüssel und seinen Wert aus der Map. |

### Zugriff & Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **get** | `get(self, key: char*) -> Option<V>` | Ruft den mit dem Schlüssel verbundenen Wert ab. |
| **contains** | `contains(self, key: char*) -> bool` | Gibt wahr zurück, wenn der Schlüssel existiert. |
| **length** | `length(self) -> usize` | Gibt die Anzahl der Elemente in der Map zurück. |
| **is_empty** | `is_empty(self) -> bool` | Gibt wahr zurück, wenn die Map leer ist. |
| **capacity** | `capacity(self) -> usize` | Gibt die aktuelle Kapazität der Map zurück. |

### Iterations-Hilfsprogramme

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **is_slot_occupied** | `is_slot_occupied(self, idx: usize) -> bool` | Prüft, ob ein roher Slot-Index belegt ist. |
| **key_at** | `key_at(self, idx: usize) -> char*` | Ruft den Schlüssel am rohen Slot-Index ab. |
| **val_at** | `val_at(self, idx: usize) -> V` | Ruft den Wert am rohen Slot-Index ab. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **free** | `free(self)` | Gibt den internen Speicher der Map frei. **Hinweis**: Dies gibt die Werte nicht frei, wenn es sich um Zeiger/Objekte handelt. |
| **Trait** | `impl Drop for Map` | Ruft beim Verlassen des Gültigkeitsbereichs automatisch `free()` auf. |
