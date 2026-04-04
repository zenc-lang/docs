# std/queue

`Queue<T>` è una coda generica First-In-First-Out (FIFO) implementata come un **Ring Buffer (Buffer Circolare)**.

## Utilizzo

```zc
import "std/queue.zc"

fn main() {
    let q = Queue<int>::new();
    
    q.push(1);
    q.push(2);
    q.push(3);
    
    // Pop restituisce un Option<T>
    if (q.pop().is_some()) {
        println "Estratto: {q.pop().unwrap()}"; // 1
    }
}
```

## Dettagli di Implementazione

- **Ring Buffer**: Utilizza un buffer circolare con indici `head` e `tail`.
- **Prestazioni**:
    - `push`: **O(1) ammortizzato** (ridimensiona quando è pieno).
    - `pop`: **O(1)** (avanza l'indice di testa).
    - `clone`: **O(N)**.
- **Sicurezza**: Gestione sicura del wrapping della memoria e del ridimensionamento.

## Definizione della Struttura

```zc
struct Queue<T> {
    data: T*;
    cap: usize;
    head: usize;
    tail: usize;
    count: usize;
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Queue<T>::new() -> Queue<T>` | Crea una nuova coda vuota. |
| **clone** | `clone(self) -> Queue<T>` | Crea una copia profonda della coda. |

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **push** | `push(self, value: T)` | Aggiunge un elemento in fondo alla coda. |
| **pop** | `pop(self) -> Option<T>` | Rimuove e restituisce l'elemento in testa. Restituisce `None` se è vuota. |
| **clear** | `clear(self)` | Rimuove tutti gli elementi dalla coda. |

### Accesso e Interrogazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Restituisce il numero di elementi. |
| **is_empty** | `is_empty(self) -> bool` | Restituisce `true` se la coda è vuota. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera il buffer interno. |
| **Tratto** | `impl Drop for Queue` | Chiama automaticamente `free()` quando esce dall'ambito. |
