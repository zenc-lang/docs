# std/sort

Il modulo `std/sort` fornisce algoritmi di ordinamento altamente ottimizzati. Implementa nativamente l'algoritmo `QuickSort` utilizzando un motore di macro polimorfiche a zero overhead.

## Utilizzo

```zc
import "std/sort.zc"

fn main() {
    let arr: int[5] = [52, 13, 99, 4, 42];
    sort_int((int*)arr, 5); // Diventa [4, 13, 42, 52, 99]
}
```

## Funzioni

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **sort_int** | `sort_int(arr: int*, len: usize)` | Ordina un array di interi standard `[i32]`. |
| **sort_long** | `sort_long(arr: long*, len: usize)` | Ordina un array di interi lunghi `[i64]`. |
| **sort_float** | `sort_float(arr: float*, len: usize)` | Ordina un array di float `[f32]`. |
| **sort_double** | `sort_double(arr: double*, len: usize)` | Ordina un array di double `[f64]`. |

## Ordinamento Personalizzato

Se crei una `struct` personalizzata con l'overloading dell'operatore `<`, puoi generare un ordinatore personalizzato:

```zc
// Emette `sort_MyStruct(MyStruct* arr, usize len)`
raw { ZC_IMPL_SORT(MyStruct) } 
```
走
