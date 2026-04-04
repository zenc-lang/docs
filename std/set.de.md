# std/set

`Set<T>` ist eine generische Hash-Set-Implementierung zum Speichern eindeutiger Werte vom Typ `T`. Es verwendet eine Hash-Tabelle mit offener Adressierung und linearer Sondierung.

## Überblick

- **Generisch**: Speichert jeden Typ `T`.
- **Eindeutig**: Behandelt Duplikate automatisch; das Hinzufügen eines vorhandenen Elements gibt `false` zurück.
- **Schnell**: Durchschnittliche Zeitkomplexität von O(1) für Hinzufügungen, Entfernungen und Abfragen.
- **RAII**: Implementiert das `Drop`-Trait für eine automatische Speicherverwaltung.

## Verwendung

```zc
import "std/set.zc"

fn main() {
    let s = Set<int>::new();
    
    s.add(10);
    s.add(20);
    s.add(10); // Duplikat, gibt false zurück
    
    if (s.contains(10)) {
        println "Set enthält 10";
    }
    
    s.remove(20);
    println "Länge: {s.length()}";
} // s wird hier automatisch freigegeben
```

## Struktur-Definition

```zc
struct Set<T> {
    data: T*;
    len: usize;
    cap: usize;
    // ... interne Felder
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Set<T>::new() -> Set<T>` | Erstellt ein neues, leeres Set. |

### Modifikation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **add** | `add(self, val: T) -> bool` | Fügt einen Wert zum Set hinzu. Gibt `true` zurück, wenn hinzugefügt, `false`, wenn bereits vorhanden. |
| **remove** | `remove(self, val: T) -> bool` | Entfernt einen Wert aus dem Set. Gibt `true` zurück, wenn vorhanden und entfernt. |
| **clear** | `clear(self)` | Entfernt alle Elemente aus dem Set, ohne den allokierten Speicher freizugeben. |

### Zugriff & Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **contains** | `contains(self, val: T) -> bool` | Gibt `true` zurück, wenn der Wert im Set existiert. |
| **length** | `length(self) -> usize` | Gibt die Anzahl der eindeutigen Elemente zurück. |
| **is_empty** | `is_empty(self) -> bool` | Gibt `true` zurück, wenn das Set keine Elemente hat. |
| **capacity** | `capacity(self) -> usize` | Gibt die aktuelle interne Kapazität zurück. |

### Hilfsmittel

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **is_slot_occupied** | `is_slot_occupied(self, idx: usize) -> bool` | Prüft, ob ein spezifischer interner Hash-Slot belegt ist. |
| **val_at** | `val_at(self, idx: usize) -> Option<T>` | Gibt den Wert an einem spezifischen internen Slot zurück, falls vorhanden. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **free** | `free(self)` | Gibt die internen Puffer des Sets manuell frei. |
| **Trait** | `impl Drop for Set` | Ruft beim Verlassen des Gültigkeitsbereichs automatisch `free()` auf. |
