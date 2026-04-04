# std/vec

`Vec<T>` è un tipo di array contiguo e ridimensionabile. È l'array dinamico standard utilizzato in Zen-C.

## Panoramica

- **Generico**: Funziona con qualsiasi tipo `T`.
- **Dinamico**: Si ridimensiona automaticamente man mano che vengono aggiunti elementi.
- **Sicuro**: Controllo dei limiti sull'accesso (va in panico in caso di errore).
- **RAII**: Libera automaticamente la memoria quando esce dall'ambito (implementa `Drop`).

## Utilizzo

```zc
import "std/vec.zc"

fn main() {
    let v = Vec<int>::new();
    v.push(10);
    v.push(20);
    
    // Iterazione
    for x in &v {
        println "{(*x)}";
    }
} // v viene liberato automaticamente qui
```

## Definizione della Struttura

```zc
struct Vec<T> {
    data: T*;
    len: usize;
    cap: usize;
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Vec<T>::new() -> Vec<T>` | Crea un nuovo vettore vuoto. Non alloca memoria fino al primo inserimento (push). |
| **with_capacity** | `Vec<T>::with_capacity(cap: usize) -> Vec<T>` | Crea un nuovo vettore con una capacità iniziale di `cap`. Utile per l'ottimizzazione se conosci in anticipo il numero di elementi. |

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **push** | `push(self, item: T)` | Aggiunge un elemento in coda. Va in panico se l'allocazione fallisce. |
| **pop** | `pop(self) -> T` | Rimuove l'ultimo elemento e lo restituisce. Va in panico se è vuoto. |
| **pop_opt** | `pop_opt(self) -> Option<T>` | Rimuove l'ultimo elemento e restituisce `Some(val)`. Restituisce `None` se è vuoto. Utilizzo sicuro. |
| **insert** | `insert(self, idx: usize, item: T)` | Inserisce un elemento all'indice `idx`. Sposta gli elementi a destra. Va in panico se `idx > len`. |
| **remove** | `remove(self, idx: usize) -> T` | Rimuove e restituisce l'elemento all'indice `idx`. Sposta gli elementi a sinistra. Va in panico se `idx >= len`. |
| **append** | `append(self, other: Vec<T>)` | Aggiunge tutti gli elementi di `other` a `self`. Consuma `other` (semantica di spostamento). |
| **clear** | `clear(self)` | Rimuove tutti i valori. Non ha effetto sulla capacità allocata. |
| **reverse** | `reverse(self)` | Inverte l'ordine degli elementi sul posto. |

### Accesso

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **get** | `get(self, idx: usize) -> T` | Restituisce una copia dell'elemento all'indice `idx`. Va in panico se fuori dai limiti. |
| **get_ref** | `get_ref(self, idx: usize) -> T*` | Restituisce un puntatore all'elemento all'indice `idx`. Va in panico se fuori dai limiti. Utile per evitare copie. |
| **set** | `set(self, idx: usize, item: T)` | Sovrascrive l'elemento all'indice `idx`. Va in panico se fuori dai limiti. |
| **first** | `first(self) -> T` | Restituisce una copia del primo elemento. Va in panico se è vuoto. |
| **last** | `last(self) -> T` | Restituisce una copia dell'ultimo elemento. Va in panico se è vuoto. |

### Utilità

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Restituisce il numero di elementi. |
| **is_empty** | `is_empty(self) -> bool` | Restituisce `true` se il vettore non contiene elementi. |
| **contains** | `contains(self, item: T) -> bool` | Restituisce `true` se il vettore contiene un elemento uguale a `item` (confronto byte a byte). |
| **clone** | `clone(self) -> Vec<T>` | Restituisce un nuovo vettore con una copia profonda dei dati. |
| **eq** | `eq(self, other: Vec<T>*) -> bool` | Restituisce `true` se due vettori sono uguali byte a byte. Accetta un puntatore per evitare lo spostamento di `other`. |

### Operatori

Zen-C supporta l'overloading degli operatori. `Vec<T>` implementa i seguenti:

| Operatore | Metodo | Descrizione |
| :--- | :--- | :--- |
| `+` | **add** | `v1 + &v2`. Restituisce un nuovo vettore (concatenazione). |
| `+=` | **add_assign** | `v1 += &v2`. Aggiunge `v2` a `v1`. |
| `==` | **eq** | `v1 == &v2`. Controllo di uguaglianza strutturale. |
| `!=` | **neq** | `v1 != &v2`. Controllo di disuguaglianza strutturale. |
| `<<` | **shl** | `v << item`. Aggiunge `item` in coda. |
| `>>` | **shr** | `v >> &item`. Estrae l'ultimo elemento in `item`. |
| `*` | **mul** | `v * n`. Restituisce un nuovo vettore con gli elementi ripetuti `n` volte. |
| `*=` | **mul_assign** | `v *= n`. Ripete gli elementi sul posto `n` volte. |
| `[]` | **get** / **set** | `v[i]` e `v[i] = x`. Indicizzazione standard. |

### Iterazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> VecIter<T>` | Restituisce un iteratore che produce copie. Usato da `for x in v`. |
| **iter_ref** | `iter_ref(self) -> VecIterRef<T>` | Restituisce un iteratore che produce puntatori. Usato da `for x in &v` o `for x in v.iter_ref()`. Consente modifiche sul posto. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **Free** | `free(self)` | Libera manualmente la memoria. Sicuro da chiamare più volte. |
| **Forget** | `forget(self)` | Distacca il buffer di memoria dal vettore (imposta i campi a 0). Impedisce a `Drop` di liberare la memoria. Utile per implementare la semantica di spostamento o il trasferimento di proprietà. |
| **Tratto**| `impl Drop for Vec` | Chiama automaticamente `free()` quando `Vec` esce dall'ambito. |
走
