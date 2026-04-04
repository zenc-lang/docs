# std/sync

El módulo `std/sync` proporciona un conjunto completo de primitivas de sincronización para gestionar el acceso concurrente a datos compartidos y coordinar la ejecución de hilos.

## Resumen

- **Primitivas Estándar**: Incluye `Mutex`, `CondVar`, `RwLock`, `Once`, `Semaphore` y `Barrier`.
- **Integración con RAII**: Todas las primitivas implementan el rasgo `Drop`, lo que garantiza que los recursos del sistema (como los handles de pthread) se liberen automáticamente.
- **Multiplataforma**: Abstrae de forma segura las peculiaridades de cada plataforma (por ejemplo, implementando `Barrier` y `Semaphore` mediante mutexes/condvars en macOS).
- **Eficiencia**: Envoltorios ligeros alrededor de bibliotecas de sincronización de nivel de sistema optimizadas.

## Uso

```zc
import "std/sync.zc"

fn main() {
    let m = Mutex::new();
    
    // Bloqueo con alcance (RAII)
    {
        m.lock();
        // Sección crítica
        m.unlock();
    } // m se libera automáticamente si era el último propietario
    
    // Inicialización de una sola vez
    let once = Once::new();
    once.call(|| {
        println "¡Inicializado!";
    });
}
```

## Definiciones de Estructura

### `Mutex`
Un bloqueo de exclusión mutua para proteger datos compartidos.

### `CondVar`
Una variable de condición para la señalización entre hilos basada en cambios de estado.

### `RwLock`
Un bloqueo de lector-escritor que permite múltiples lectores concurrentes pero solo un escritor.

### `Once`
Garantiza que una pieza específica de código de inicialización se ejecute exactamente una vez.

### `Semaphore`
Un semáforo de conteo para controlar el acceso a un grupo de recursos.

### `Barrier`
Un punto de sincronización donde múltiples hilos deben esperar hasta que haya llegado un número específico de ellos.

## Métodos

### Métodos de `Mutex`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Mutex::new() -> Mutex` | Crea un nuevo mutex. |
| **lock** | `lock(self)` | Adquiere el bloqueo (bloqueante). |
| **try_lock** | `try_lock(self) -> bool` | Intenta adquirir el bloqueo sin bloquearse. |
| **unlock** | `unlock(self)` | Libera el bloqueo. |

### Métodos de `CondVar`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `CondVar::new() -> CondVar` | Crea una nueva variable de condición. |
| **wait** | `wait(self, mutex: Mutex*)` | Bloquea el hilo hasta que reciba una señal, liberando temporalmente el mutex. |
| **signal** | `signal(self)` | Despierta un hilo que esté esperando en esta condición. |
| **broadcast**| `broadcast(self)` | Despierta a todos los hilos que estén esperando en esta condición. |

### Métodos de `RwLock`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `RwLock::new() -> RwLock` | Crea un nuevo bloqueo de lector-escritor. |
| **rdlock** | `rdlock(self)` | Adquiere un bloqueo de lectura compartido. |
| **wrlock** | `wrlock(self)` | Adquiere un bloqueo de escritura exclusivo. |
| **unlock** | `unlock(self)` | Libera cualquier bloqueo que se posea. |

### Métodos de `Semaphore`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Semaphore::new(value: int) -> Semaphore` | Crea un nuevo semáforo con un `value` inicial. |
| **wait** | `wait(self)` | Decrementa el semáforo (bloqueante si es 0). |
| **post** | `post(self)` | Incrementa el semáforo. |
| **value** | `value(self) -> int` | Devuelve el valor actual. |

### Métodos de `Barrier`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Barrier::new(count: int) -> Barrier` | Crea una nueva barrera para `count` hilos. |
| **wait** | `wait(self) -> bool` | Espera en la barrera. Devuelve `true` para el líder designado. |

## Gestión de Memoria

Todas las primitivas implementan `impl Drop` y llamarán automáticamente a su método `free()` interno para liberar los recursos del sistema cuando salgan del alcance.
