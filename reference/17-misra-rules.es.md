+++
title = "17. Reglas MISRA"
weight = 17
+++

# 17. Reglas MISRA

Zen C incluye un **modo de conformidad MISRA C:2012** activado con el flag `--misra`.
Ademas de las comprobaciones MISRA estandar, el compilador aplica varias **reglas especificas de Zen**
que promueven un codigo mas seguro y mantenible.

#### Activar el modo MISRA

```bash
zc build app.zc --misra
```

Las violaciones se informan como errores del compilador en tiempo de compilacion:

```
error: MISRA Rule Zen 2.2: tuple with 3 or more fields shall be replaced
       with a named struct (use 'struct' instead of positional tuple)
  --> app.zc:5:1
   |
 5 | fn get_stats() -> (int, int, int) { ... }
```

{% alert(type="note") %}
El texto del estandar MISRA es propiedad intelectual de MISRA Consortium Ltd. La
implementacion de Zen C verifica la conformidad pero no reproduce el estandar.
Para las definiciones oficiales de las reglas, consulte la documentacion de
[MISRA C:2012](https://www.misra.org.uk/).
{% end %}

#### Reglas Especificas de Zen

Estas reglas son exclusivas de Zen C. Cada regla se verifica cuando `--misra` esta activo.

#### Zen 1.1 -- Sin bloques raw

Prohibe los bloques `raw { }` que eluden el transpilador.

```zc
// Bad:
fn main() {
    raw { int x = 10; }
}

// Good:
fn main() {
    let x = 10;
}
```

#### Zen 1.2 -- Sin bloques plugin

Prohibe los bloques `plugin ... end`, que ejecutan codigo arbitrario en tiempo de compilacion.

```zc
// Bad:
plugin my_plugin

// Good:
import "std/some_module.zc"
```

#### Zen 1.3 -- Match exhaustivo de enums

Prohibe el comodin `_` en `match` sobre tipos enum -- todas las variantes deben manejarse explicitamente.

```zc
enum Color { Red; Green; Blue; }

// Bad -- missing Blue:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
    }
}

// Good:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
        Color::Blue => { println "blue"; }
    }
}
```

#### Zen 1.4 -- Sin directivas de preprocesador

Prohibe las directivas de preprocesador de C (`#define`, `#include`, `#if`, etc.).
Utilice `import` y `def` de Zen en su lugar.

```zc
// Bad:
#define BUFFER_SIZE 256
#include <stdio.h>

// Good:
def BUFFER_SIZE = 256;
import "std/io.zc"
```

#### Zen 1.5 -- Sin `var` / `const` para declaraciones

Las palabras clave `var` y `const` estan obsoletas para declaraciones de variables/constantes.
Utilice `let` para variables y `def` para constantes de tiempo de compilacion.

```zc
// Bad:
var x = 10;
const MAX = 100;

// Good:
let x = 10;
def MAX = 100;
```

> `const` sigue siendo valido como **calificador de tipo** para interoperabilidad con C
> (por ejemplo, `const int` en declaraciones FFI).

#### Zen 1.8 -- Sin ocultacion de identificadores

Prohibe declarar un nombre que oculte uno de un ambito externo.

```zc
let x = 10;
if true {
    // Bad -- shadows outer x:
    let x = 20;
}

// Good:
if true {
    let inner_x = 20;
}
```

#### Zen 2.1 -- Sin identificadores reservados

Prohibe los identificadores que comienzan con `__`, `_[A-Z]` o `_z_`, los cuales estan reservados
para el compilador y la implementacion de C.

```zc
// Bad:
let __my_var = 10;
let _Reserved = 20;
let _z_internal = 30;

// Good:
let my_var = 10;
let reserved = 20;
let internal = 30;
```

#### Zen 2.2 -- Limite de tamano de tuplas

Las tuplas con **3 o mas campos** no deben usarse como tipos de retorno o parametros de funcion.
Utilice una estructura con nombre en su lugar. Las tuplas de 2 elementos estan exentas.

```zc
// Bad -- 3-tuple as return type:
fn get_stats() -> (int, int, int) { ... }
fn process(p: (int, string, bool)) { ... }

// Good -- use a struct:
struct Stats { sum: int; avg: int; max: int; }
fn get_stats() -> Stats { ... }

// OK -- 2-tuples are exempt:
fn get_pair() -> (int, int) { ... }
```

#### Zen 2.3 -- Comparacion de strings

`string == string` no debe usarse. Utilice `strcmp()` en su lugar.

```zc
// Bad (when a, b are string):
if a == b { ... }

// Good:
if strcmp(a, b) == 0 { ... }

// OK -- int, bool, pointer comparisons are safe:
if x == y { ... }
```

## Cobertura Estandar MISRA C:2012

El compilador verifica las siguientes reglas estandar de MISRA C:2012.
Haga clic en un capitulo para expandir la lista de reglas.

{% misra_table() %}

Para el texto completo de las reglas, consulte la documentacion oficial de
[MISRA C:2012](https://www.misra.org.uk/).
