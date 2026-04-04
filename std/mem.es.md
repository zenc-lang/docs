# std/mem

El módulo `std/mem` proporciona utilidades de gestión de memoria del núcleo, incluyendo funciones de asignación manual, rasgos de ciclo de vida estándar e implementaciones de punteros inteligentes.

## Resumen

- **Asignación Manual**: Envoltorios alrededor de `malloc`, `calloc` y `free` con firmas de tipo seguro.
- **Rasgos**: Define los rasgos de ciclo de vida primarios: `Drop` (destructores), `Clone` (copias profundas) y `Copy` (copias implícitas).
- **Punteros Inteligentes**: Incluye `Box<T>` para datos asignados en el montón con limpieza automática (RAII).
- **Utilidades de Búfer**: Funciones de alto nivel para intercambiar, poner a cero y copiar memoria.

## Uso

```zc
import "std/mem.zc"

fn main() {
    // Asignación manual
    let ptr = alloc<int>();
    *ptr = 42;
    free(ptr);
    
    // Limpieza automática con Box (RAII)
    {
        let b = Box<int>::new();
        *b.get() = 100;
        // la memoria se libera automáticamente aquí
    }
}
```

## Métodos

### Asignación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **alloc\<T>**| `alloc<T>() -> T*` | Asigna memoria para una sola instancia de `T`. |
| **zalloc\<T>**| `zalloc<T>() -> T*` | Asigna memoria inicializada a cero para una sola instancia de `T`. |
| **alloc_n\<T>**| `alloc_n<T>(n: usize) -> T*` | Asigna memoria para una matriz de `n` instancias de `T`. |

### Operaciones

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **mem_zero\<T>**| `mem_zero<T>(ptr: T*, count: usize)` | Establece a cero la memoria para `count` instancias de `T`. |
| **mem_copy\<T>**| `mem_copy<T>(dst: T*, src: T*, count: usize)`| Copia `count` instancias de `T` de `src` a `dst`. |
| **swap\<T>** | `swap<T>(a: T*, b: T*)` | Intercambia los valores entre dos ubicaciones de memoria. |

## Rasgos

| Rasgo | Método | Firma | Descripción |
| :--- | :--- | :--- | :--- |
| **Drop** | **drop** | `drop(self)` | Destructor llamado cuando el objeto sale del alcance. |
| **Clone** | **clone** | `clone(self) -> Self` | Crea una copia profunda del objeto. |
| **Copy** | *(Marcador)* | N/A | Indica que el tipo debe usar copias implícitas en lugar de movimientos. |

## Definición de Estructura: `Box<T>`

Un puntero inteligente RAII sencillo para gestionar la memoria del montón.

```zc
struct Box<T> {
    ptr: T*;
}
```

### Métodos de `Box`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Box::new() -> Box<T>` | Asigna una nueva instancia gestionada en el montón. |
| **from_ptr** | `Box::from_ptr(p: T*) -> Box<T>` | Crea un `Box` que toma la propiedad de un puntero existente. |
| **get** | `get(self) -> T*` | Devuelve el puntero interno crudo. |
| **free** | `free(self)` | Libera manualmente la memoria subyacente. |
| **Trait** | `impl Drop for Box<T>` | Llama automáticamente a `free()` cuando el box sale del alcance. |
