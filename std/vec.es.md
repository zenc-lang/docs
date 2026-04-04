# std/vec

`Vec<T>` es un tipo de matriz contigua y ampliable. Es la matriz dinámica estándar utilizada en Zen-C.

## Resumen

- **Genérico**: Funciona con cualquier tipo `T`.
- **Dinámico**: Cambia de tamaño automáticamente a medida que se añaden elementos.
- **Seguro**: Comprobación de límites en el acceso (lanza un pánico si falla).
- **RAII**: Libera automáticamente la memoria cuando sale del alcance (implementa `Drop`).

## Uso

```zc
import "std/vec.zc"

fn main() {
    let v = Vec<int>::new();
    v.push(10);
    v.push(20);
    
    // Iteración
    for x in &v {
        println "{(*x)}";
    }
} // v se libera automáticamente aquí
```

## Definición de Estructura

```zc
struct Vec<T> {
    data: T*;
    len: usize;
    cap: usize;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Vec<T>::new() -> Vec<T>` | Crea un nuevo vector vacío. No asigna memoria hasta el primer push. |
| **with_capacity** | `Vec<T>::with_capacity(cap: usize) -> Vec<T>` | Crea un nuevo vector con una capacidad inicial de `cap`. Útil para optimización si conoce el número de elementos de antemano. |

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **push** | `push(self, item: T)` | Añade un elemento al final. Lanza un pánico si la asignación falla. |
| **pop** | `pop(self) -> T` | Elimina el último elemento y lo devuelve. Lanza un pánico si está vacío. |
| **pop_opt** | `pop_opt(self) -> Option<T>` | Elimina el último elemento y devuelve `Some(val)`. Devuelve `None` si está vacío. Uso seguro. |
| **insert** | `insert(self, idx: usize, item: T)` | Inserta un elemento en `idx`. Desplaza los elementos a la derecha. Lanza un pánico si `idx > len`. |
| **remove** | `remove(self, idx: usize) -> T` | Elimina y devuelve el elemento en `idx`. Desplaza los elementos a la izquierda. Lanza un pánico si `idx >= len`. |
| **append** | `append(self, other: Vec<T>)` | Añade todos los elementos de `other` a `self`. Consume `other` (semántica de movimiento). |
| **clear** | `clear(self)` | Elimina todos los valores. No tiene efecto sobre la capacidad asignada. |
| **reverse** | `reverse(self)` | Invierte el orden de los elementos in situ. |

### Acceso

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **get** | `get(self, idx: usize) -> T` | Devuelve una copia del elemento en `idx`. Lanza un pánico si está fuera de los límites. |
| **get_ref** | `get_ref(self, idx: usize) -> T*` | Devuelve un puntero al elemento en `idx`. Lanza un pánico si está fuera de los límites. Útil para evitar copias. |
| **set** | `set(self, idx: usize, item: T)` | Sobrescribe el elemento en `idx`. Lanza un pánico si está fuera de los límites. |
| **first** | `first(self) -> T` | Devuelve una copia del primer elemento. Lanza un pánico si está vacío. |
| **last** | `last(self) -> T` | Devuelve una copia del último elemento. Lanza un pánico si está vacío. |

### Utilidad

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Devuelve el número de elementos. |
| **is_empty** | `is_empty(self) -> bool` | Devuelve `true` si el vector no contiene elementos. |
| **contains** | `contains(self, item: T) -> bool` | Devuelve `true` si el vector contiene un elemento igual a `item` (comparación byte a byte). |
| **clone** | `clone(self) -> Vec<T>` | Devuelve un nuevo vector con una copia profunda de los datos. |
| **eq** | `eq(self, other: Vec<T>*) -> bool` | Devuelve `true` si dos vectores son iguales byte a byte. Toma un puntero para evitar mover `other`. |

### Operadores

Zen-C admite la sobrecarga de operadores. `Vec<T>` implementa los siguientes:

| Operador | Método | Descripción |
| :--- | :--- | :--- |
| `+` | **add** | `v1 + &v2`. Devuelve un nuevo vector (concatenación). |
| `+=` | **add_assign** | `v1 += &v2`. Añade `v2` a `v1`. |
| `==` | **eq** | `v1 == &v2`. Comprobación de igualdad estructural. |
| `!=` | **neq** | `v1 != &v2`. Comprobación de desigualdad estructural. |
| `<<` | **shl** | `v << item`. Añade `item` al final. |
| `>>` | **shr** | `v >> &item`. Extrae el último elemento en `item`. |
| `*` | **mul** | `v * n`. Devuelve un nuevo vector con los elementos repetidos `n` veces. |
| `*=` | **mul_assign** | `v *= n`. Repite los elementos in situ `n` veces. |
| `[]` | **get** / **set** | `v[i]` y `v[i] = x`. Indexación estándar. |

### Iteración

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> VecIter<T>` | Devuelve un iterador que produce copias. Usado por `for x in v`. |
| **iter_ref** | `iter_ref(self) -> VecIterRef<T>` | Devuelve un iterador que produce punteros. Usado por `for x in &v` o `for x in v.iter_ref()`. Permite la modificación in situ. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **Free** | `free(self)` | Libera manualmente la memoria. Es seguro llamarlo varias veces. |
| **Forget** | `forget(self)` | Desvincula el búfer de memoria del vector (pone los campos a 0). Evita que `Drop` libere la memoria. Útil para implementar la semántica de movimiento o transferir la propiedad. |
| **Trait** | `impl Drop for Vec` | Llama automáticamente a `free()` cuando `Vec` sale del alcance. |
