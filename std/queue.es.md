# std/queue

`Queue<T>` es una cola genérica de tipo Primero en Entrar, Primero en Salir (FIFO) implementada como un **Búfer Circular (Ring Buffer)**.

## Uso

```zc
import "std/queue.zc"

fn main() {
    let q = Queue<int>::new();
    
    q.push(1);
    q.push(2);
    q.push(3);
    
    // Pop devuelve un Option<T>
    if (q.pop().is_some()) {
        println "Extraído: {q.pop().unwrap()}"; // 1
    }
}
```

## Detalles de Implementación

- **Búfer Circular**: Utiliza un búfer circular con índices `head` (cabeza) y `tail` (cola).
- **Rendimiento**:
    - `push`: **O(1) amortizado** (cambia de tamaño cuando está lleno).
    - `pop`: **O(1)** (avanza el índice de la cabeza).
    - `clone`: **O(N)**.
- **Seguridad**: Manejo seguro del ajuste de memoria y el cambio de tamaño.

## Definición de Estructura

```zc
struct Queue<T> {
    data: T*;
    cap: usize;
    head: usize;
    tail: usize;
    count: usize;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Queue<T>::new() -> Queue<T>` | Crea una nueva cola vacía. |
| **clone** | `clone(self) -> Queue<T>` | Crea una copia profunda de la cola. |

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **push** | `push(self, value: T)` | Añade un elemento a la parte trasera de la cola. |
| **pop** | `pop(self) -> Option<T>` | Elimina y devuelve el elemento en la parte delantera. Devuelve `None` si está vacía. |
| **clear** | `clear(self)` | Elimina todos los elementos de la cola. |

### Acceso y Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Devuelve el número de elementos. |
| **is_empty** | `is_empty(self) -> bool` | Devuelve `true` si la cola está vacía. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera el búfer interno. |
| **Trait** | `impl Drop for Queue` | Llama automáticamente a `free()` cuando sale del alcance. |
