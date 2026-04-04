# std/random

El módulo `std/random` proporciona un envoltorio de generador de números pseudoaleatorios (PRNG) orientado a objetos e idiomático alrededor de las funciones de `<stdlib.h>` de POSIX.

## Uso

```zc
import "std/random.zc"

fn main() {
    // Siembra automáticamente el generador con la hora actual del sistema
    let rng = Random::new();

    // Generar números enteros aleatorios
    let acotado = rng.next_int_range(1, 100); // de 1 a 100 inclusive
    
    println "Lanzamiento: {acotado}";
}
```

## Definición de Estructura

```zc
struct Random {
    seed: U32;
}
```

## Métodos

### Inicialización

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Random::new() -> Random` | Crea un nuevo generador aleatorio sembrado con la hora actual del sistema. |
| **from_seed** | `Random::from_seed(seed: U32) -> Random` | Crea un nuevo generador aleatorio utilizando una semilla específica. |

### Generación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **next_int** | `next_int(self) -> int` | Devuelve un número entero aleatorio en el rango bruto `[0, RAND_MAX]`. |
| **next_int_range** | `next_int_range(self, min: int, max: int) -> int` | Devuelve un número entero aleatorio en el rango `[min, max]` inclusive. |
| **next_double** | `next_double(self) -> double` | Devuelve un número de coma flotante aleatorio en el rango `[0.0, 1.0)`. |
| **next_bool** | `next_bool(self) -> bool` | Devuelve un booleano aleatorio. |
