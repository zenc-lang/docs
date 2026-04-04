# std/iter

Il modulo `std/iter` fornisce i tratti (traits) per definire iteratori personalizzati compatibili con la sintassi del ciclo `for-in` di Zen C.

## Utilizzo

```zc
import "std/iter.zc"

fn main() {
    // Supponendo che la mia_collezione implementi Iterable<T>
    for item in mia_collezione {
        // ...
    }
}
```

## Tratti (Traits)

### `Iterator<T>`

Un'interfaccia per avanzare attraverso una sequenza.

```zc
trait Iterator<T> {
    fn next(self) -> Option<T>;
}
```

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **next** | `next(self) -> Option<T>` | Restituisce `Some(item)` se c'è un elemento successivo, o `None` se l'iterazione è completa. |

### `Iterable<T>`

Un'interfaccia per i tipi che possono produrre un `Iterator`.

```zc
trait Iterable<T> {
    fn iterator(self) -> Iterator<T>;
}
```

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> Iterator<T>` | Crea e restituisce un iteratore per la collezione. |
