# std/slice

`Slice<T>` è una "vista" (view) leggera, che non possiede i dati (non-owning), in una sequenza contigua di elementi. È utilizzata principalmente per fornire un'interfaccia sicura e pratica per lavorare con array a dimensione fissa.

## Panoramica

- **Senza Proprietà (Non-owning)**: Le slice non copiano né possiedono i dati sottostanti; si limitano a puntare ad essi.
- **Supporto all'Iterazione**: Implementa il metodo `iterator()`, consentendo alle slice di essere utilizzate direttamente nei cicli `for-in`.
- **Conversione Automatica**: Il compilatore Zen-C converte automaticamente gli array a dimensione fissa in slice quando si esegue un'iterazione o si passano a funzioni che si aspettano una slice.
- **Accesso Sicuro**: Fornisce i metodi `get()` e `at()` con controllo dei limiti che restituiscono un `Option<T>`.

## Utilizzo

```zc
import "std/slice.zc"

fn main() {
    let arr: int[5] = [10, 20, 30, 40, 50];
    
    // Creazione esplicita di una slice
    let s = Slice<int>::from_array(arr, 5);
    
    // Iterazione diretta sulla slice
    for val in s {
        println "{val}";
    }
    
    // Iterazione diretta sull'array (importa automaticamente std/slice.zc)
    for val in arr {
        println "{val}";
    }
}
```

## Definizione della Struttura

```zc
struct Slice<T> {
    data: T*;
    len: usize;
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **from_array** | `Slice<T>::from_array(ptr: T*, len: usize) -> Slice<T>` | Crea una vista slice su un puntatore di array. |
| **new** | `Slice<T>::new(data: T*, len: usize) -> Slice<T>` | Alias per `from_array`. |

### Iterazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> SliceIter<T>` | Restituisce un iteratore per l'uso nei cicli `for-in`. |

### Accesso e Interrogazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Restituisce il numero di elementi nella slice. |
| **is_empty** | `is_empty(self) -> bool` | Restituisce `true` se la slice non contiene elementi. |
| **get** | `get(self, idx: usize) -> Option<T>` | Restituisce l'elemento all'indice `idx`, o `None` se fuori dai limiti. |
| **at** | `at(self, idx: usize) -> Option<T>` | Alias per `get`. |

## Note

- **Auto-import**: `std/slice.zc` viene importato automaticamente dal compilatore quando si esegue un'iterazione `for-in` su array a dimensione fissa.
- **Sicurezza**: Sebbene `data` sia un puntatore grezzo, la struttura `Slice` incoraggia l'uso del metodo `get()`, consapevole della lunghezza, per un accesso sicuro.
走
