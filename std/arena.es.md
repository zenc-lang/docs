# std/arena

El módulo `std/arena` proporciona un asignador "bump" rápido para asignaciones de memoria masivas. Toda la memoria asignada dentro de una arena se libera a la vez cuando la arena misma se destruye o se reinicia.

## Resumen

- **Rendimiento**: Las asignaciones son extremadamente rápidas, implicando solo un incremento de puntero.
- **Liberación Masiva**: Ideal para asignaciones locales de tareas o peticiones donde todo puede liberarse al mismo tiempo.
- **Guardar/Restaurar**: Soporte para "puntos de control" para liberar parcialmente la memoria dentro de la arena.
- **RAII**: Implementa el rasgo `Drop` para asegurar que el búfer subyacente se libere automáticamente.

## Uso

```zc
import "std/arena.zc"

struct Node {
    val: int;
}

fn main() {
    // Crear arena con capacidad de 1KB
    let a = Arena::new(1024);
    
    // Asignaciones rápidas
    let n1 = a.alloc<Node>();
    let n2 = a.alloc<Node>();
    
    // Duplicar cadena en la memoria de la arena
    let s = a.dup_str("Hola Mundo");
    
    println "Arena usada: {a.bytes_used()} bytes";
    
    // Todo se libera automáticamente cuando 'a' sale del alcance
}
```

## Definición de Estructura

```zc
struct Arena {
    data: void*;
    capacity: usize;
    used: usize;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Arena::new(cap: usize) -> Arena` | Crea una nueva arena con la capacidad especificada. |

### Asignación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **alloc\<T>** | `alloc<T>(self) -> T*` | Asigna e inicializa a cero la memoria para un tipo `T`. |
| **alloc_n\<T>**| `alloc_n<T>(self, count: usize) -> T*` | Asigna memoria para una matriz de `count` elementos de tipo `T`. |
| **alloc_bytes**| `alloc_bytes(self, size: usize) -> void*` | Asignación de bytes crudos (alineada a 8 bytes). |
| **dup_str** | `dup_str(self, src: char*) -> char*` | Duplica una cadena C en la arena. |

### Consulta y Control

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **bytes_used** | `bytes_used(self) -> usize` | Devuelve el total de bytes asignados actualmente. |
| **bytes_free** | `bytes_free(self) -> usize` | Devuelve la capacidad restante. |
| **save** | `save(self) -> usize` | Devuelve un "punto de control" que representa el uso actual. |
| **restore** | `restore(self, mark: usize)` | Libera parcialmente hasta un punto de control previo. |
| **reset** | `reset(self)` | Libera todas las asignaciones reiniciando el uso a cero (se mantiene el búfer). |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera explícitamente el búfer subyacente de la arena. |
| **Trait** | `impl Drop for Arena` | Llama automáticamente a `free()` cuando la arena sale del alcance. |
