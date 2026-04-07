+++
title = "13. Interoperabilidad C"
weight = 13
+++

# 13. Interoperabilidad C

Zen C ofrece dos formas de interactuar con código C: **Importaciones de Confianza** (Conveniente) y **FFI Explícita** (Seguro/Preciso).

#### Método 1: Importaciones de Confianza (Conveniente)

Puedes importar una cabecera C directamente usando la palabra clave `import` con la extensión `.h`. Esto trata la cabecera como un módulo y asume que todos los símbolos accedidos existen.

```zc
//> link: -lm
import "math.h" as c_math;

fn main() {
    // El compilador confía en la corrección; emite 'cos(...)' directamente
    let x = c_math::cos(3.14159);
}
```

> **Pros**: Cero código repetitivo. Acceso a todo el contenido de la cabecera inmediato.
> **Cons**: Sin seguridad de tipos desde Zen C (errores capturados por el compilador C después).

#### Método 2: FFI Explícita (Seguro)

Para una comprobación estricta de tipos o cuando no quieres incluir el texto de una cabecera, usa `extern fn`.

```zc
include <stdio.h> // Emite #include <stdio.h> en el C generado

// Define firma estricta
extern fn printf(fmt: char*, ...) -> c_int;

fn main() {
    printf("Hola FFI: %d\n", 42); // Comprobado por tipos por Zen C
}
```

> **Pros**: Zen C asegura que los tipos coincidan.
> **Cons**: Requiere declaración manual de funciones.

#### `import` vs `include`

- **`import "file.h"`**: Registra la cabecera como un módulo con nombre. Habilita el acceso implícito a símbolos (ej. `file::function()`).
- **`include <file.h>`**: Simplemente emite `#include <file.h>` en el código C generado. No introduce ningún símbolo al compilador de Zen C; debe usar `extern fn` para acceder a ellos.

#### Diagnóstico y Fricción

Por defecto, Zen C suprime las advertencias de "Función no definida" para las funciones de la biblioteca estándar de C para proporcionar una experiencia de interoperabilidad sin fricciones. Puede controlar este comportamiento utilizando los indicadores `-Winterop` y `-Wno-interop`.

[Leer más sobre el Sistema de Diagnóstico](15-diagnostics.es.md)

---

## Biblioteca Estándar

Zen C incluye una biblioteca estándar (`std`) que cubre las funcionalidades esenciales.

[Explorar la Documentación de la Biblioteca Estándar](../docs/std/README.md)

### Módulos Clave

<details>
<summary>Click para ver todos los módulos de la Biblioteca Estándar</summary>

| Módulo | Descripción | Docs |
| :--- | :--- | :--- |
| **`std/bigfloat.zc`** | Aritmética de punto flotante de precisión arbitraria. | [Docs](../docs/std/bigfloat.md) |
| **`std/bigint.zc`** | Entero de precisión arbitraria `BigInt`. | [Docs](../docs/std/bigint.md) |
| **`std/bits.zc`** | Operaciones bit a bit de bajo nivel (`rotl`, `rotr`, etc). | [Docs](../docs/std/bits.md) |
| **`std/complex.zc`** | Aritmética de números complejos `Complex`. | [Docs](../docs/std/complex.md) |
| **`std/vec.zc`** | Array dinámico creíble `Vec<T>`. | [Docs](../docs/std/vec.md) |
| **`std/string.zc`** | Tipo `String` asignado en el heap con soporte UTF-8. | [Docs](../docs/std/string.md) |
| **`std/queue.zc`** | Cola FIFO (Ring Buffer). | [Docs](../docs/std/queue.md) |
| **`std/map.zc`** | Mapa Hash Genérico `Map<V>`. | [Docs](../docs/std/map.md) |
| **`std/fs.zc`** | Operaciones del sistema de archivos. | [Docs](../docs/std/fs.md) |
| **`std/io.zc`** | Entrada/Salida estándar (`print`/`println`). | [Docs](../docs/std/io.md) |
| **`std/option.zc`** | Valores opcionales (`Some`/`None`). | [Docs](../docs/std/option.md) |
| **`std/result.zc`** | Gestión de errores (`Ok`/`Err`). | [Docs](../docs/std/result.md) |
| **`std/path.zc`** | Manipulación de rutas multiplataforma. | [Docs](../docs/std/path.md) |
| **`std/env.zc`** | Variables de entorno del proceso. | [Docs](../docs/std/env.md) |
| **`std/net/`** | TCP, UDP, HTTP, DNS, URL. | [Docs](../docs/std/net.md) |
| **`std/thread.zc`** | Hilos y Sincronización. | [Docs](../docs/std/thread.md) |
| **`std/time.zc`** | Medición de tiempo y espera (sleep). | [Docs](../docs/std/time.md) |
| **`std/json.zc`** | Parseo y serialización de JSON. | [Docs](../docs/std/json.md) |
| **`std/stack.zc`** | Pila LIFO `Stack<T>`. | [Docs](../docs/std/stack.md) |
| **`std/set.zc`** | Conjunto Hash Genérico `Set<T>`. | [Docs](../docs/std/set.md) |
| **`std/process.zc`** | Ejecución y gestión de procesos. | [Docs](../docs/std/process.md) |
| **`std/regex.zc`** | Expresiones Regulares (basado en TRE). | [Docs](../docs/std/regex.md) |
| **`std/simd.zc`** | Tipos de vectores SIMD nativos. | [Docs](../docs/std/simd.md) |

</details>

---
