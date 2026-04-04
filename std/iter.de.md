# std/iter

Das Modul `std/iter` bietet Traits zur Definition benutzerdefinierter Iteratoren, die mit der `for-in`-Schleifensyntax von Zen C kompatibel sind.

## Verwendung

```zc
import "std/iter.zc"

fn main() {
    // Angenommen, my_collection implementiert Iterable<T>
    for item in my_collection {
        // ...
    }
}
```

## Traits

### `Iterator<T>`

Eine Schnittstelle zum Fortschreiten durch eine Sequenz.

```zc
trait Iterator<T> {
    fn next(self) -> Option<T>;
}
```

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **next** | `next(self) -> Option<T>` | Gibt `Some(item)` zurück, wenn ein nächstes Element vorhanden ist, oder `None`, wenn die Iteration abgeschlossen ist. |

### `Iterable<T>`

Eine Schnittstelle für Typen, die einen `Iterator` erzeugen können.

```zc
trait Iterable<T> {
    fn iterator(self) -> Iterator<T>;
}
```

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> Iterator<T>` | Erstellt und gibt einen Iterator für die Sammlung zurück. |
