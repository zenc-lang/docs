# std/stack

Il modulo `std/stack` fornisce una struttura dati stack LIFO (Last-In, First-Out).

## Utilizzo

```zc
import "std/stack.zc"

fn main() {
    let s = Stack<int>::new();
    s.push(10);
    s.push(20);
    
    let cima = s.pop(); // Some(20)
} // s viene liberato automaticamente qui
```

## Definizione della Struttura

```zc
struct Stack<T> {
    // Dettagli di implementazione interna
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Stack<T>::new() -> Stack<T>` | Crea un nuovo stack vuoto. |
| **clone** | `clone(self) -> Stack<T>` | Crea una copia profonda dello stack. |

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **push** | `push(self, value: T)` | Inserisce un valore in cima allo stack. |
| **pop** | `pop(self) -> Option<T>` | Rimuove e restituisce l'elemento in cima allo stack. Restituisce `None` se è vuoto. |
| **clear** | `clear(self)` | Rimuove tutti gli elementi dallo stack. |

### Accesso e Interrogazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Restituisce il numero di elementi nello stack. |
| **is_empty** | `is_empty(self) -> bool` | Restituisce `true` se lo stack non contiene elementi. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera manualmente la memoria dello stack. |
| **Tratto** | `impl Drop for Stack` | Chiama automaticamente `free()` quando lo stack esce dall'ambito. |
走
