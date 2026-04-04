# std/iter

El módulo `std/iter` proporciona rasgos para definir iteradores personalizados compatibles con la sintaxis del bucle `for-in` de Zen C.

## Uso

```zc
import "std/iter.zc"

fn main() {
    // Asumiendo que mi_coleccion implementa Iterable<T>
    for item in mi_coleccion {
        // ...
    }
}
```

## Rasgos

### `Iterator<T>`

Una interfaz para avanzar a través de una secuencia.

```zc
trait Iterator<T> {
    fn next(self) -> Option<T>;
}
```

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **next** | `next(self) -> Option<T>` | Devuelve `Some(item)` si hay un siguiente elemento, o `None` si la iteración ha terminado. |

### `Iterable<T>`

Una interfaz para tipos que pueden producir un `Iterator`.

```zc
trait Iterable<T> {
    fn iterator(self) -> Iterator<T>;
}
```

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> Iterator<T>` | Crea y devuelve un iterador para la colección. |
