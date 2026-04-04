# std/time

El módulo `std/time` proporciona utilidades para la medición del tiempo de alta precisión y la suspensión de hilos.

## Resumen

- **Precisión de Milisegundos**: `Time::now()` devuelve la hora actual del sistema en milisegundos.
- **Tipo Duration**: La estructura `Duration` permite cálculos de intervalos de tiempo intuitivos.
- **Suspensión Simple**: Funciones fáciles de usar para suspender la ejecución.
- **Ligero**: Sobrecarga mínima, envolviendo funciones de tiempo estándar a nivel de sistema.

## Uso

```zc
import "std/time.zc"

fn main() {
    let inicio = Time::now();
    
    // Dormir durante 1,5 segundos
    Time::sleep(Duration::from_ms(1500));
    
    let fin = Time::now();
    println "Transcurrido: {fin - inicio} ms";
}
```

## Definiciones de Estructura

### `Duration`
Representa un intervalo de tiempo.
```zc
struct Duration {
    millis: U64;
}
```

### `Time`
Estructura de utilidad estática para operaciones de tiempo del sistema.
```zc
struct Time {}
```

## Métodos

### Métodos de `Duration`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **from_ms** | `Duration::from_ms(ms: U64) -> Duration` | Crea una `Duration` a partir de un conteo de milisegundos. |
| **from_secs** | `Duration::from_secs(s: U64) -> Duration` | Crea una `Duration` a partir de un conteo de segundos. |

### Métodos Estáticos de `Time`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **now** | `Time::now() -> U64` | Devuelve la hora actual del sistema en milisegundos desde la época (epoch). |
| **sleep** | `Time::sleep(d: Duration)` | Suspende el hilo actual durante la `Duration` especificada. |
| **sleep_ms** | `Time::sleep_ms(ms: U64)` | Suspende el hilo actual durante el conteo especificado de milisegundos. |
