# std/mem

Das Modul `std/mem` bietet Kernfunktionen zur Speicherverwaltung, einschließlich manueller Allokationsfunktionen, Standard-Lebenszyklus-Traits und Smart-Pointer-Implementierungen.

## Überblick

- **Manuelle Allokation**: Wrapper um `malloc`, `calloc` und `free` mit typsicheren Signaturen.
- **Traits**: Definiert die primären Lebenszyklus-Traits: `Drop` (Destruktoren), `Clone` (Tiefe Kopien) und `Copy` (Implizite Kopien).
- **Smart Pointer**: Enthält `Box<T>` für Heap-allokierte Daten mit automatischer Bereinigung (RAII).
- **Puffer-Hilfsprogramme**: Hochsprachenfunktionen zum Vertauschen, Nullen und Kopieren von Speicher.

## Verwendung

```zc
import "std/mem.zc"

fn main() {
    // Manuelle Allokation
    let ptr = alloc<int>();
    *ptr = 42;
    free(ptr);
    
    // Automatische Bereinigung mit Box (RAII)
    {
        let b = Box<int>::new();
        *b.get() = 100;
        // Speicher wird hier automatisch freigegeben
    }
}
```

## Methoden

### Allokation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **alloc\<T>**| `alloc<T>()    -> T*` | Allokiert Speicher für eine einzelne Instanz von `T`. |
| **zalloc\<T>**| `zalloc<T>()   -> T*` | Allokiert mit Null initialisierten Speicher für eine einzelne Instanz von `T`. |
| **alloc_n\<T>**| `alloc_n<T>(n: usize) -> T*` | Allokiert Speicher für ein Array von `n` Instanzen von `T`. |

### Operationen

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **mem_zero\<T>**| `mem_zero<T>(ptr: T*, count: usize)` | Setzt den Speicher für `count` Instanzen von `T` auf Null. |
| **mem_copy\<T>**| `mem_copy<T>(dst: T*, src: T*, count: usize)`| Kopiert `count` Instanzen von `T` von `src` nach `dst`. |
| **swap\<T>** | `swap<T>(a: T*, b: T*)` | Vertauscht die Werte zwischen zwei Speicherstellen. |

## Traits

| Trait | Methode | Signatur | Beschreibung |
| :--- | :--- | :--- | :--- |
| **Drop** | **drop** | `drop(self)` | Destruktor, der aufgerufen wird, wenn das Objekt den Gültigkeitsbereich verlässt. |
| **Clone** | **clone** | `clone(self) -> Self` | Erstellt eine tiefe Kopie des Objekts. |
| **Copy** | *(Marker)* | N/A | Zeigt an, dass der Typ implizite Kopien anstelle von Verschiebungen verwenden sollte. |

## Struktur-Definition: `Box<T>`

Ein einfacher RAII Smart Pointer zur Verwaltung von Heap-Speicher.

```zc
struct Box<T> {
    ptr: T*;
}
```

### `Box` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Box::new() -> Box<T>` | Allokiert eine neue vom Heap verwaltete Instanz. |
| **from_ptr** | `Box::from_ptr(p: T*) -> Box<T>` | Erstellt eine `Box`, die den Besitz eines vorhandenen Zeigers übernimmt. |
| **get** | `get(self) -> T*` | Gibt den rohen internen Zeiger zurück. |
| **free** | `free(self)` | Gibt den zugrunde liegenden Speicher manuell frei. |
| **Trait** | `impl Drop for Box<T>` | Ruft beim Verlassen des Gültigkeitsbereichs automatisch `free()` auf. |
