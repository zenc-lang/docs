# std/stack

El módulo `std/stack` proporciona una estructura de datos de pila LIFO (Último en Entrar, Primero en Salir).

## Uso

```zc
import "std/stack.zc"

fn main() {
    let s = Stack<int>::new();
    s.push(10);
    s.push(20);
    
    let superior = s.pop(); // Some(20)
} // s se libera automáticamente aquí
```

## Definición de Estructura

```zc
struct Stack<T> {
    // Detalles de la implementación interna
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Stack<T>::new() -> Stack<T>` | Crea una nueva pila vacía. |
| **clone** | `clone(self) -> Stack<T>` | Crea una copia profunda de la pila. |

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **push** | `push(self, value: T)` | Inserta un valor en la parte superior de la pila. |
| **pop** | `pop(self) -> Option<T>` | Elimina y devuelve el elemento superior de la pila. Devuelve `None` si está vacía. |
| **clear** | `clear(self)` | Elimina todos los elementos de la pila. |

### Acceso y Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Devuelve el número de elementos en la pila. |
| **is_empty** | `is_empty(self) -> bool` | Devuelve `true` si la pila no contiene elementos. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera manualmente la memoria de la pila. |
| **Trait** | `impl Drop for Stack` | Llama automáticamente a `free()` cuando la pila sale del alcance. |
