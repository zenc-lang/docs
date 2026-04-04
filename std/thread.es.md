# std/thread

El módulo `std/thread` proporciona primitivas de alto nivel para crear y gestionar hilos de ejecución concurrentes.

## Resumen

- **Hilos Nativos**: Utiliza la gestión de hilos a nivel de sistema subyacente (por ejemplo, hilos POSIX).
- **Soporte de Clausuras**: `Thread::spawn` puede aceptar clausuras de Zen-C, lo que permite compartir datos fácilmente entre hilos.
- **Ciclo de Vida Explícito**: Los hilos deben unirse (join) o separarse (detach) explícitamente para garantizar una limpieza adecuada de los recursos.
- **Seguridad**: Los errores durante la creación o manipulación de hilos se informan a través de `Result<bool>`.

## Uso

```zc
import "std/thread.zc"

fn trabajador(id: int) {
    println "Hola desde el trabajador {id}";
}

fn main() {
    // Generación con una clausura
    let t = Thread::spawn(|| {
        trabajador(42);
    }).unwrap();
    
    // Espera explícita a la finalización
    t.join();
}
```

## Definiciones de Estructura

### `Thread`
Representa un handle a un hilo generado.
```zc
struct Thread {
    handle: void*;
}
```

## Métodos

### Ciclo de vida de `Thread`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **spawn** | `Thread::spawn(func: fn()) -> Result<Thread>` | Genera un nuevo hilo que ejecuta la clausura o función proporcionada. |
| **join** | `join(self) -> Result<bool>` | Bloquea el hilo actual hasta que el hilo generado termine. |
| **detach** | `detach(self) -> Result<bool>` | Separa el hilo, permitiéndole ejecutarse de forma independiente. Los recursos se liberan automáticamente al salir. |
| **cancel** | `cancel(self) -> Result<bool>` | Envía una solicitud de cancelación al hilo. |

### Funciones de Utilidad

| Función | Firma | Descripción |
| :--- | :--- | :--- |
| **sleep_ms** | `sleep_ms(ms: int)` | Suspende la ejecución del hilo actual durante aproximadamente `ms` milisegundos. |
