# std/slice

`Slice<T>` ist eine leichtgewichtige "Sicht" (View) ohne Besitzanspruch auf eine zusammenhängende Sequenz von Elementen. Es wird primär verwendet, um eine sichere und bequeme Schnittstelle für die Arbeit mit Arrays fester Größe zu bieten.

## Überblick

- **Kein Besitz**: Slices kopieren oder besitzen die zugrunde liegenden Daten nicht; sie zeigen lediglich darauf.
- **Iterationsunterstützung**: Implementiert die Methode `iterator()`, wodurch Slices direkt in `for-in`-Schleifen verwendet werden können.
- **Automatische Konvertierung**: Der Zen-C-Compiler konvertiert Arrays fester Größe automatisch in Slices bei Iterationen oder wenn sie an Funktionen übergeben werden, die Slices erwarten.
- **Sicherer Zugriff**: Bietet grenzgeprüfte `get()`- und `at()`-Methoden, die `Option<T>` zurückgeben.

## Verwendung

```zc
import "std/slice.zc"

fn main() {
    let arr: int[5] = [10, 20, 30, 40, 50];
    
    // Explizite Erstellung eines Slices
    let s = Slice<int>::from_array(arr, 5);
    
    // Direkte Iteration über den Slice
    for val in s {
        println "{val}";
    }
    
    // Direktes Iterieren über das Array (auto-importiert std/slice.zc)
    for val in arr {
        println "{val}";
    }
}
```

## Struktur-Definition

```zc
struct Slice<T> {
    data: T*;
    len: usize;
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **from_array** | `Slice<T>::from_array(ptr: T*, len: usize) -> Slice<T>` | Erstellt eine Slice-Sicht über einen Array-Zeiger. |
| **new** | `Slice<T>::new(data: T*, len: usize) -> Slice<T>` | Alias für `from_array`. |

### Iteration

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> SliceIter<T>` | Gibt einen Iterator zur Verwendung in `for-in`-Schleifen zurück. |

### Zugriff & Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Gibt die Anzahl der Elemente im Slice zurück. |
| **is_empty** | `is_empty(self) -> bool` | Gibt `true` zurück, wenn der Slice keine Elemente enthält. |
| **get** | `get(self, idx: usize) -> Option<T>` | Gibt das Element bei `idx` zurück, oder `None`, wenn außerhalb der Grenzen. |
| **at** | `at(self, idx: usize) -> Option<T>` | Alias für `get`. |

## Hinweise

- **Auto-Import**: `std/slice.zc` wird vom Compiler automatisch importiert, wenn eine `for-in`-Iteration auf Arrays fester Größe durchgeführt wird.
- **Sicherheit**: Obwohl `data` ein roher Zeiger ist, ermutigt die `Slice`-Struktur zur Verwendung der längenbewussten `get()`-Methode für einen sicheren Zugriff.
