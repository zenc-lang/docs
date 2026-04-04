# std/slice

`Slice<T>` es una "vista" ligera y sin propiedad sobre una secuencia contigua de elementos. Se utiliza principalmente para proporcionar una interfaz segura y conveniente para trabajar con matrices de tamaño fijo.

## Resumen

- **Sin Propiedad**: Las rodajas (slices) no copian ni poseen los datos subyacentes; simplemente apuntan a ellos.
- **Soporte de Iteración**: Implementa el método `iterator()`, lo que permite usar rodajas directamente en bucles `for-in`.
- **Conversión Automática**: El compilador de Zen-C convierte automáticamente las matrices de tamaño fijo en rodajas al realizar una iteración o al pasarlas a funciones que esperan rodajas.
- **Acceso Seguro**: Proporciona los métodos `get()` y `at()` con comprobación de límites que devuelven `Option<T>`.

## Uso

```zc
import "std/slice.zc"

fn main() {
    let arr: int[5] = [10, 20, 30, 40, 50];
    
    // Creación explícita de una rodaja
    let s = Slice<int>::from_array(arr, 5);
    
    // Iteración directa sobre la rodaja
    for val in s {
        println "{val}";
    }
    
    // Iteración directa sobre la matriz (importa automáticamente std/slice.zc)
    for val in arr {
        println "{val}";
    }
}
```

## Definición de Estructura

```zc
struct Slice<T> {
    data: T*;
    len: usize;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **from_array** | `Slice<T>::from_array(ptr: T*, len: usize) -> Slice<T>` | Crea una vista de rodaja sobre un puntero de matriz. |
| **new** | `Slice<T>::new(data: T*, len: usize) -> Slice<T>` | Alias de `from_array`. |

### Iteración

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> SliceIter<T>` | Devuelve un iterador para su uso en bucles `for-in`. |

### Acceso y Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Devuelve el número de elementos en la rodaja. |
| **is_empty** | `is_empty(self) -> bool` | Devuelve `true` si la rodaja no contiene elementos. |
| **get** | `get(self, idx: usize) -> Option<T>` | Devuelve el elemento en `idx`, o `None` si está fuera de los límites. |
| **at** | `at(self, idx: usize) -> Option<T>` | Alias de `get`. |

## Notas

- **Auto-importación**: El compilador importa automáticamente `std/slice.zc` al realizar una iteración `for-in` sobre matrices de tamaño fijo.
- **Seguridad**: Aunque `data` es un puntero directo, la estructura `Slice` fomenta el uso del método `get()`, que tiene en cuenta la longitud, para un acceso seguro.
