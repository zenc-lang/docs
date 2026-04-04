# std/option

`Option<T>` representa un valor opcional: cada `Option` es o bien `Some` y contiene un valor, o bien `None`. Se utiliza comúnmente para manejar la ausencia de un valor sin recurrir a punteros nulos.

## Resumen

- **Seguro**: Fomenta el manejo explícito del caso `None`.
- **Genérico**: Puede envolver cualquier tipo `T`.
- **Cero coste**: Se compila en una estructura simple con una bandera booleana.
- **Conveniente**: Proporciona muchos métodos de utilidad para extraer y transformar valores.

## Uso

```zc
import "std/option.zc"

fn main() {
    let val = Option<int>::Some(10);
    
    if (val.is_some()) {
        println "El valor es {val.unwrap()}";
    }
    
    let vacio = Option<int>::None();
    let x = vacio.unwrap_or(0);
}
```

## Definición de Estructura

```zc
struct Option<T> {
    is_some: bool;
    val: T;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **Some** | `Option<T>::Some(v: T) -> Option<T>` | Crea una opción `Some` que contiene `v`. |
| **None** | `Option<T>::None() -> Option<T>` | Crea una opción `None`. |

### Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **is_some** | `is_some(self) -> bool` | Devuelve `true` si la opción es `Some`. |
| **is_none** | `is_none(self) -> bool` | Devuelve `true` si la opción es `None`. |

### Extracción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **unwrap** | `unwrap(self) -> T` | Devuelve el valor contenido. Lanza un pánico si es `None`. |
| **unwrap_ref** | `unwrap_ref(self) -> T*` | Devuelve un puntero al valor contenido. Lanza un pánico si es `None`. |
| **unwrap_or** | `unwrap_or(self, def: T) -> T` | Devuelve el valor contenido o `def`. |
| **expect** | `expect(self, msg: char*) -> T` | Devuelve el valor o lanza un pánico con `msg`. |
| **or_else** | `or_else(self, other: Option<T>) -> Option<T>` | Devuelve la opción si es `Some`, de lo contrario devuelve `other`. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **forget** | `forget(self)` | Pone a cero el valor interno sin llamar a destructores ni liberar memoria. |
