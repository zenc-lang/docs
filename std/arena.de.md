# std/arena

Das Modul `std/arena` bietet einen schnellen "Bump"-Allokator für Massenspeicherzuweisungen. Der gesamte in einer Arena zugewiesene Speicher wird auf einmal freigegeben, wenn die Arena selbst zerstört oder zurückgesetzt wird.

## Überblick

- **Leistung**: Allokationen sind extrem schnell und beinhalten nur ein einziges Inkrementieren des Zeigers.
- **Massenfreigabe**: Ideal für aufgabenlokale oder anfrage-lokale Allokationen, bei denen alles zur gleichen Zeit freigegeben werden kann.
- **Speichern/Wiederherstellen**: Unterstützung für "Checkpoints", um Speicher innerhalb der Arena teilweise freizugeben.
- **RAII**: Implementiert das `Drop`-Trait, um sicherzustellen, dass der zugrunde liegende Puffer automatisch freigegeben wird.

## Verwendung

```zc
import "std/arena.zc"

struct Node {
    val: int;
}

fn main() {
    // Arena mit 1KB Kapazität erstellen
    let a = Arena::new(1024);
    
    // Schnelle Allokationen
    let n1 = a.alloc<Node>();
    let n2 = a.alloc<Node>();
    
    // String in den Arena-Speicher duplizieren
    let s = a.dup_str("Hello World");
    
    println "Arena genutzt: {a.bytes_used()} Bytes";
    
    // Alles wird automatisch freigegeben, wenn 'a' den Gültigkeitsbereich verlässt
}
```

## Struktur-Definition

```zc
struct Arena {
    data: void*;
    capacity: usize;
    used: usize;
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Arena::new(cap: usize) -> Arena` | Erstellt eine neue Arena mit der angegebenen Kapazität. |

### Allokation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **alloc\<T>** | `alloc<T>(self) -> T*` | Allokiert und initialisiert Speicher für einen Typ `T` mit Null. |
| **alloc_n\<T>**| `alloc_n<T>(self, count: usize) -> T*` | Allokiert Speicher für ein Array von `count` Elementen des Typs `T`. |
| **alloc_bytes**| `alloc_bytes(self, size: usize) -> void*` | Rohe Byte-Allokation (ausgerichtet auf 8 Bytes). |
| **dup_str** | `dup_str(self, src: char*) -> char*` | Dupliziert einen C-String in die Arena. |

### Abfrage & Steuerung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **bytes_used** | `bytes_used(self) -> usize` | Gibt die Gesamtzahl der aktuell allokierten Bytes zurück. |
| **bytes_free** | `bytes_free(self) -> usize` | Gibt die verbleibende Kapazität zurück. |
| **save** | `save(self) -> usize` | Gibt einen "Checkpoint" zurück, der die aktuelle Nutzung darstellt. |
| **restore** | `restore(self, mark: usize)` | Gibt Speicher teilweise bis zu einem vorherigen Checkpoint frei. |
| **reset** | `reset(self)` | Gibt alle Allokationen frei, indem die Nutzung auf Null zurückgesetzt wird (Puffer bleibt erhalten). |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **free** | `free(self)` | Gibt den zugrunde liegenden Arena-Puffer explizit frei. |
| **Trait** | `impl Drop for Arena` | Ruft automatisch `free()` auf, wenn die Arena den Gültigkeitsbereich verlässt. |
