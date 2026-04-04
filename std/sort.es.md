# std/sort

El módulo `std/sort` proporciona algoritmos de ordenación altamente optimizados. Implementa de forma nativa el algoritmo `QuickSort` utilizando un motor de macros polimórfico de sobrecarga cero.

## Uso

```zc
import "std/sort.zc"

fn main() {
    let arr: int[5] = [52, 13, 99, 4, 42];
    sort_int((int*)arr, 5); // Pasa a ser [4, 13, 42, 52, 99]
}
```

## Funciones

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **sort_int** | `sort_int(arr: int*, len: usize)` | Ordena una matriz de enteros estándar `[i32]`. |
| **sort_long** | `sort_long(arr: long*, len: usize)` | Ordena una matriz de enteros largos `[i64]`. |
| **sort_float** | `sort_float(arr: float*, len: usize)` | Ordena una matriz de reales `[f32]`. |
| **sort_double** | `sort_double(arr: double*, len: usize)` | Ordena una matriz de reales de doble precisión `[f64]`. |

## Ordenación Personalizada

Si crea una `struct` personalizada con sobrecarga del operador `<`, puede generar un ordenador personalizado:

```zc
// Emite `sort_MiEstructura(MiEstructura* arr, usize len)`
raw { ZC_IMPL_SORT(MiEstructura) } 
```
