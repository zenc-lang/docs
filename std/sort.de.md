# std/sort

Das Modul `std/sort` bietet hochoptimierte Sortieralgorithmen. Es implementiert nativ den `QuickSort`-Algorithmus unter Verwendung einer polymorphen Makro-Engine ohne Overhead.

## Verwendung

```zc
import "std/sort.zc"

fn main() {
    let arr: int[5] = [52, 13, 99, 4, 42];
    sort_int((int*)arr, 5); // Wird zu [4, 13, 42, 52, 99]
}
```

## Funktionen

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **sort_int** | `sort_int(arr: int*, len: usize)` | Sortiert ein Array von Standard-Ganzzahlen `[i32]`. |
| **sort_long** | `sort_long(arr: long*, len: usize)` | Sortiert ein Array von long-Ganzzahlen `[i64]`. |
| **sort_float** | `sort_float(arr: float*, len: usize)` | Sortiert ein Array von Floats `[f32]`. |
| **sort_double** | `sort_double(arr: double*, len: usize)` | Sortiert ein Array von Doubles `[f64]`. |

## Benutzerdefiniertes Sortieren

Wenn Sie ein benutzerdefiniertes `struct` mit `<` Operatorüberladung erstellen, können Sie einen benutzerdefinierten Sorter generieren:

```zc
// Emittiert `sort_MyStruct(MyStruct* arr, usize len)`
raw { ZC_IMPL_SORT(MyStruct) } 
```
