# std/set

`Set<T>` es una implementación genérica de conjunto hash para almacenar valores únicos de tipo `T`. Utiliza una tabla hash de direccionamiento abierto con sondeo lineal.

## Resumen

- **Genérico**: Almacena cualquier tipo `T`.
- **Único**: Maneja automáticamente los duplicados; añadir un elemento que ya existe devuelve `false`.
- **Rápido**: Complejidad de tiempo promedio O(1) para adiciones, eliminaciones y búsquedas.
- **RAII**: Implementa el rasgo `Drop` para la gestión automática de la memoria.

## Uso

```zc
import "std/set.zc"

fn main() {
    let s = Set<int>::new();
    
    s.add(10);
    s.add(20);
    s.add(10); // Duplicado, devuelve false
    
    if (s.contains(10)) {
        println "El conjunto contiene 10";
    }
    
    s.remove(20);
    println "Longitud: {s.length()}";
} // s se libera automáticamente aquí
```

## Definición de Estructura

```zc
struct Set<T> {
    data: T*;
    len: usize;
    cap: usize;
    // ... campos internos
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Set<T>::new() -> Set<T>` | Crea un nuevo conjunto vacío. |

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **add** | `add(self, val: T) -> bool` | Añade un valor al conjunto. Devuelve `true` si se añade, `false` si ya está presente. |
| **remove** | `remove(self, val: T) -> bool` | Elimina un valor del conjunto. Devuelve `true` si estaba presente y se eliminó. |
| **clear** | `clear(self)` | Elimina todos los elementos del conjunto sin liberar la memoria asignada. |

### Acceso y Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **contains** | `contains(self, val: T) -> bool` | Devuelve `true` si el valor existe en el conjunto. |
| **length** | `length(self) -> usize` | Devuelve el número de elementos únicos. |
| **is_empty** | `is_empty(self) -> bool` | Devuelve `true` si el conjunto no tiene elementos. |
| **capacity** | `capacity(self) -> usize` | Devuelve la capacidad interna actual. |

### Utilidad

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **is_slot_occupied** | `is_slot_occupied(self, idx: usize) -> bool` | Comprueba si una ranura hash interna específica está ocupada. |
| **val_at** | `val_at(self, idx: usize) -> Option<T>` | Devuelve el valor en una ranura interna específica, si lo hay. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera manualmente los búferes internos del conjunto. |
| **Trait** | `impl Drop for Set` | Llama automáticamente a `free()` cuando el conjunto sale del alcance. |
