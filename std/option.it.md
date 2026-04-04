# std/option

`Option<T>` rappresenta un valore opzionale: ogni `Option` è o `Some` e contiene un valore, oppure `None`. È comunemente usato per gestire l'assenza di un valore senza ricorrere ai puntatori nulli.

## Panoramica

- **Sicuro**: Incoraggia la gestione esplicita del caso `None`.
- **Generico**: Può avvolgere qualsiasi tipo `T`.
- **Zero-cost**: Viene compilato in una semplice struttura con un flag booleano.
- **Pratico**: Fornisce molti metodi di utilità per estrarre e trasformare i valori.

## Utilizzo

```zc
import "std/option.zc"

fn main() {
    let val = Option<int>::Some(10);
    
    if (val.is_some()) {
        println "Il valore è {val.unwrap()}";
    }
    
    let vuoto = Option<int>::None();
    let x = vuoto.unwrap_or(0);
}
```

## Definizione della Struttura

```zc
struct Option<T> {
    is_some: bool;
    val: T;
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **Some** | `Option<T>::Some(v: T) -> Option<T>` | Crea un'opzione `Some` contenente `v`. |
| **None** | `Option<T>::None() -> Option<T>` | Crea un'opzione `None`. |

### Interrogazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **is_some** | `is_some(self) -> bool` | Restituisce `true` se l'opzione è `Some`. |
| **is_none** | `is_none(self) -> bool` | Restituisce `true` se l'opzione è `None`. |

### Estrazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **unwrap** | `unwrap(self) -> T` | Restituisce il valore contenuto. Va in panico se è `None`. |
| **unwrap_ref** | `unwrap_ref(self) -> T*` | Restituisce un puntatore al valore contenuto. Va in panico se è `None`. |
| **unwrap_or** | `unwrap_or(self, def: T) -> T` | Restituisce il valore contenuto o `def`. |
| **expect** | `expect(self, msg: char*) -> T` | Restituisce il valore o va in panico con `msg`. |
| **or_else** | `or_else(self, other: Option<T>) -> Option<T>` | Restituisce l'opzione se è `Some`, altrimenti restituisce `other`. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **forget** | `forget(self)` | Azzera il valore interno senza chiamare i distruttori o liberare memoria. |
