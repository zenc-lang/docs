# std/sys/signal

El módulo `std/sys/signal` proporciona primitivas para manejar señales del sistema, envolviendo la funcionalidad de `signal.h` de POSIX.

## Resumen

- **Intercepción de Señales**: Define controladores personalizados para señales como `SIGINT` (Ctrl+C).
- **Terminación Controlada**: Utiliza controladores de señales para realizar una limpieza antes de salir del programa.
- **Constantes Comunes**: Proporciona definiciones multiplataforma para señales estándar.

## Uso

```zc
import "std/sys/signal.zc"
import "std/io.zc"

fn al_interrumpir(sig: int) {
    println "Recibida SIGINT ({sig}). Limpiando...";
    exit(0);
}

fn main() {
    Signal::set_handler(Z_SIGINT, al_interrumpir);
    println "Esperando Ctrl+C...";
    while(true) {}
}
```

## Definición de Estructura

```zc
struct Signal {}
```

## Métodos

### Métodos de `Signal`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **set_handler** | `Signal::set_handler(sig: int, handler: fn*(int)) -> fn*(int)` | Registra un controlador para la señal dada y devuelve el controlador anterior. |

## Constantes

### Señales Estándar
- `Z_SIGINT`: Interrupción desde el teclado (Ctrl+C).
- `Z_SIGILL`: Instrucción ilegal.
- `Z_SIGABRT`: Señal de aborto.
- `Z_SIGFPE`: Excepción de coma flotante.
- `Z_SIGSEGV`: Violación de segmentación (acceso a memoria no válido).
- `Z_SIGTERM`: Señal de terminación.
