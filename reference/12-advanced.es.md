+++
title = "12. Avanzado y Metaprogramación"
weight = 12
+++

# 12. Avanzado y Metaprogramación


### Metaprogramación

#### Comptime
Ejecuta código en tiempo de compilación para generar código fuente o imprimir mensajes.
```zc
comptime {
    // Genera código en tiempo de compilación (escrito en stdout)
    println "let fecha_compilacion = \"2024-01-01\";";
}

println "Fecha de compilación: {fecha_compilacion}";
```

<details>
<summary><b>Funciones Auxiliares</b></summary>

Funciones especiales disponibles dentro de bloques `comptime`:

<table>
<tr>
<th>Función</th>
<th>Descripción</th>
</tr>
<tr>
<td><code>yield(str)</code></td>
<td>Emite código generado explícitamente (alternativa a <code>printf</code>)</td>
</tr>
<tr>
<td><code>code(str)</code></td>
<td>Alias de <code>yield()</code> - intención más clara para generación de código</td>
</tr>
<tr>
<td><code>compile_error(msg)</code></td>
<td>Detiene la compilación con un mensaje de error fatal</td>
</tr>
<tr>
<td><code>compile_warn(msg)</code></td>
<td>Emite una advertencia en tiempo de compilación (permite continuar)</td>
</tr>
</table>

**Ejemplo:**
```zc
comptime {
    compile_warn("Generando código optimizado...");
    
    let ENABLE_FEATURE = 1;
    if (ENABLE_FEATURE == 0) {
        compile_error("¡La función debe estar habilitada!");
    }
    
    // Usa code() con raw strings para generación limpia
    code(r"let FEATURE_ENABLED = 1;");
}
```
</details>

<details>
<summary><b>Metadatos de Construcción</b></summary>

Accede a información de construcción del compilador en tiempo de compilación:

<table>
<tr>
<th>Constante</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
<tr>
<td><code>__COMPTIME_TARGET__</code></td>
<td>string</td>
<td>Plataforma: <code>"linux"</code>, <code>"windows"</code> o <code>"macos"</code></td>
</tr>
<tr>
<td><code>__COMPTIME_FILE__</code></td>
<td>string</td>
<td>Nombre del archivo fuente actual siendo compilado</td>
</tr>
</table>

**Ejemplo:**
```zc
comptime {
    // Generación de código específica de plataforma
    println "let PLATFORM = \"{__COMPTIME_TARGET__}\";";
}

println "Ejecutando en: {PLATFORM}";
```
</details>

{% alert(type="tip") %}
Usa raw strings (`r"..."`) en comptime para evitar escapar llaves: `code(r"fn test() { return 42; }")`. De lo contrario, usa `{{` y `}}` para escapar llaves en strings regulares.
{% end %}


#### Embed
Embebe archivos como los tipos especificados.
```zc
// Por defecto (Slice_char)
let datos = embed "assets/logo.png";

// Embed tipado
let texto = embed "shader.glsl" as string;    // Embebe como C-string
let rom   = embed "bios.bin" as u8[1024];     // Embebe como array fijo
let wav   = embed "sound.wav" as u8[];        // Embebe como Slice_u8
```

#### Plugins
Importa plugins del compilador para extender la sintaxis.
```zc
import plugin "regex"
let re = regex! { ^[a-z]+$ };
```

#### Macros de C Genéricas
Pasa macros del preprocesador directamente a C.

{% alert(type="tip") %}
Para constantes simples, usa `def` en su lugar. Usa `#define` cuando necesites macros del preprocesador de C o flags de compilación condicional.
{% end %}

```zc
#define MAX_BUFFER 1024
```

#### Compilación Condicional
Usa `@cfg()` para incluir o excluir condicionalmente cualquier declaración de nivel superior basándote en flags `-D`.

```zc
// Compilar con: zc build app.zc -DUSE_OPENGL

@cfg(USE_OPENGL)
import "opengl_backend.zc";

@cfg(USE_VULKAN)
import "vulkan_backend.zc";

@cfg(not(USE_OPENGL))
@cfg(not(USE_VULKAN))
fn fallback_init() { println "No se seleccionó backend"; }
```

| Forma | Significado |
|:---|:---|
| `@cfg(NAME)` | Incluir si `-DNAME` está definido |
| `@cfg(not(NAME))` | Incluir si `-DNAME` NO está definido |
| `@cfg(any(A, B, ...))` | Incluir si ALGUNA condición es verdadera (OR) |
| `@cfg(all(A, B, ...))` | Incluir si TODAS las condiciones son verdaderas (AND) |

Múltiples `@cfg` en una declaración se combinan con AND. `not()` se puede usar dentro de `any()` y `all()`. Funciona con cualquier declaración de nivel superior: `fn`, `struct`, `import`, `impl`, `raw`, `def`, `test`, etc.

### Atributos

Decora funciones y structs para modificar el comportamiento del compilador.

| Atributo | Ámbito | Descripción |
|:---|:---|:---|
| `@required` | Fn | Advierte si el valor de retorno es ignorado. |
| `@deprecated("msg")` | Fn/Struct | Advierte sobre el uso con un mensaje. |
| `@inline` | Fn | Sugiere al compilador hacer inlininig. |
| `@noinline` | Fn | Previene el inlining. |
| `@packed` | Struct | Elimina el padding entre campos. |
| `@align(N)` | Struct | Fuerza el alineamiento a N bytes. |
| `@constructor` | Fn | Se ejecuta antes de main. |
| `@destructor` | Fn | Se ejecuta después de que main termine. |
| `@unused` | Fn/Var | Suprime advertencias de variables no usadas. |
| `@weak` | Fn | Enlace de símbolo débil (weak symbol linkage). |
| `@section("nombre")` | Fn | Coloca el código en una sección específica. |
| `@noreturn` | Fn | La función no retorna (ej. exit). |
| `@pure` | Fn | La función no tiene efectos secundarios (sugestión de optimización). |
| `@cold` | Fn | Es poco probable que la función se ejecute (sugestión de predicción de saltos). |
| `@hot` | Fn | La función se ejecuta frecuentemente (sugestión de optimización). |
| `@export` | Fn/Struct | Exporta el símbolo (visibilidad por defecto). |
| `@global` | Fn | CUDA: Punto de entrada del kernel (`__global__`). |
| `@device` | Fn | CUDA: Función de dispositivo (`__device__`). |
| `@host` | Fn | CUDA: Función de host (`__host__`). |
| `@comptime` | Fn | Función auxiliar disponible para ejecución en tiempo de compilación. |
| `@cfg(NAME)` | Cualquiera | Compilación condicional: incluye solo si se pasa `-DNAME`. Soporta `not()`, `any()`, `all()`. |
| `@derive(...)` | Struct | Implementa traits automáticamente. Soporta `Debug`, `Eq` (Derivación Inteligente), `Copy`, `Clone`. |
| `@ctype("tipo")` | Parámetro Fn | Sobrescribe el tipo C generado para un parámetro. |
| `@<custom>` | Cualquier | Pasa atributos genéricos a C (ej. `@flatten`, `@alias("nombre")`). |

#### Atributos Personalizados

Zen C soporta un potente sistema de **Atributos Personalizados** que te permite usar cualquier `__attribute__` de GCC/Clang directamente en tu código. Cualquier atributo que no sea reconocido explícitamente por el compilador de Zen C es tratado como un atributo genérico y se pasa al código C generado.

Esto proporciona acceso a características avanzadas del compilador, optimizaciones y directivas del enlazador sin necesidad de soporte explícito en el núcleo del lenguaje.

#### Mapeo de Sintaxis
Los atributos de Zen C se mapean directamente a atributos de C:
- `@nombre` → `__attribute__((nombre))`
- `@nombre(args)` → `__attribute__((nombre(args)))`
- `@nombre("string")` → `__attribute__((nombre("string")))`

#### Derivaciones Inteligentes

Zen C proporciona "Derivaciones Inteligentes" que respetan la Semántica de Movimiento:

- **`@derive(Eq)`**: Genera un método de igualdad que recibe los argumentos por referencia (`fn eq(self, other: T*)`).
    - Al comparar dos structs que no son Copy (`a == b`), el compilador pasa automáticamente `b` por referencia (`&b`) para evitar moverlo.
    - Las comprobaciones de igualdad recursivas en los campos también prefieren el acceso por puntero para prevenir la transferencia de posesión.

### Ensamblador Inline

Zen C proporciona soporte de primera clase para ensamblador inline, transpilando directamente a `asm` extendido de estilo GCC.

#### Uso Básico
Escribe ensamblador crudo dentro de bloques `asm`. Las cadenas se concatenan automáticamente.
```zc
asm {
    "nop"
    "mfence"
}
```

#### Volatile
Previene que el compilador optimice y elimine el ensamblador que tiene efectos secundarios.
```zc
asm volatile {
    "rdtsc"
}
```

#### Restricciones con Nombre
Zen C simplifica la compleja sintaxis de restricciones de GCC con vinculaciones con nombre.

```zc
// Sintaxis: : out(variable) : in(variable) : clobber(reg)
// Usa la sintaxis de marcador de posición {variable} para legibilidad

fn sumar(x: int) -> int {
    let resultado: int;
    asm {
        "mov {x}, {resultado}"
        "add $5, {resultado}"
        : out(resultado)
        : in(x)
        : clobber("cc")
    }
    return resultado;
}
```

| Tipo | Sintaxis | Equivalente GCC |
|:---|:---|:---|
| **Salida** | `: out(variable)` | `"=r"(variable)` |
| **Entrada** | `: in(variable)` | `"r"(variable)` |
| **Clobber** | `: clobber("rax")` | `"rax"` |
| **Memoria** | `: clobber("memory")` | `"memory"` |

> **Nota:** Cuando uses la sintaxis de Intel (mediante `-masm=intel`), debes asegurarte de que tu construcción esté configurada correctamente (por ejemplo, `//> cflags: -masm=intel`). TCC no soporta el ensamblador con sintaxis Intel.

### Directivas de Construcción

Zen C soporta comentarios especiales en la parte superior de tu archivo fuente para configurar el proceso de construcción sin necesidad de un complejo sistema de construcción o Makefile.

| Directiva | Argumentos | Descripción |
|:---|:---|:---|
| `//> link:` | `-lfoo` o `ruta/a/lib.a` | Enlaza contra una biblioteca o archivo objeto. |
| `//> lib:` | `ruta/a/libs` | Añade una ruta de búsqueda de biblioteca (`-L`). |
| `//> include:` | `ruta/a/headers` | Añade una ruta de búsqueda de cabeceras (`-I`). |
| `//> framework:` | `Cocoa` | Enlaza contra un framework de macOS. |
| `//> cflags:` | `-Wall -O3` | Pasa flags arbitrarios al compilador de C. |
| `//> define:` | `MACRO` o `LLAVE=VAL` | Define una macro del preprocesador (`-D`). |
| `//> pkg-config:` | `gtk+-3.0` | Ejecuta `pkg-config` y añade `--cflags` y `--libs`. |
| `//> shell:` | `comando` | Ejecuta un comando de shell durante la construcción. |
| `//> get:` | `http://url/archivo` | Descarga un archivo si el archivo específico no existe. |

#### Características

**1. Protección de SO (OS Guarding)**
Prefija las directivas con el nombre de un SO para aplicarlas solo en plataformas específicas.
Prefijos soportados: `linux:`, `windows:`, `macos:` (o `darwin:`).

```zc
//> linux: link: -lm
//> windows: link: -lws2_32
//> macos: framework: Cocoa
```

**2. Expansión de Variables de Entorno**
Usa la sintaxis `${VAR}` para expandir variables de entorno en tus directivas.

```zc
//> include: ${HOME}/mylib/include
//> lib: ${ZC_ROOT}/std
```

#### Ejemplos

```zc
//> include: ./include
//> lib: ./libs
//> link: -lraylib -lm
//> cflags: -Ofast
//> pkg-config: gtk+-3.0

import "raylib.h"

fn main() { ... }
```

### Palabras Clave

Las siguientes palabras clave están reservadas en Zen C.

#### Declaraciones
`alias`, `def`, `enum`, `fn`, `impl`, `import`, `let`, `module`, `opaque`, `struct`, `trait`, `union`, `use`

#### Flujo de Control
`async`, `await`, `break`, `catch`, `continue`, `defer`, `do`, `else`, `for`, `goto`, `guard`, `if`, `loop`, `match`, `return`, `try`, `unless`, `while`

#### Especiales
`asm`, `assert`, `autofree`, `comptime`, `const`, `embed`, `launch`, `ref`, `sizeof`, `static`, `test`, `volatile`

#### Constantes
`true`, `false`, `null`

#### Reservadas de C
Los siguientes identificadores están reservados porque son palabras clave en C11:
`auto`, `case`, `char`, `default`, `double`, `extern`, `float`, `inline`, `int`, `long`, `register`, `restrict`, `short`, `signed`, `switch`, `typedef`, `unsigned`, `void`, `_Atomic`, `_Bool`, `_Complex`, `_Generic`, `_Imaginary`, `_Noreturn`, `_Static_assert`, `_Thread_local`

#### Operadores
`and`, `or`
