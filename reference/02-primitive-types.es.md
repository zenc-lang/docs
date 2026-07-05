+++
title = "2. Tipos Primitivos"
weight = 2
+++

# 2. Tipos Primitivos {#2-tipos-primitivos}


| Tipo | Equivalente en C | Descripción |
|:---|:---|:---|
| `int`, `uint` | `int32_t`, `uint32_t` | Entero de 32 bits con signo/sin signo |
| `c_char`, `c_uchar` | `char`, `unsigned char` | C char (Interoperabilidad) |
| `c_short`, `c_ushort` | `short`, `unsigned short` | C short (Interoperabilidad) |
| `c_int`, `c_uint` | `int`, `unsigned int` | C int (Interoperabilidad) |
| `c_long`, `c_ulong` | `long`, `unsigned long` | C long (Interoperabilidad) |
| `c_longlong`, `c_ulonglong` | `long long`, `unsigned long long` | C long long / unsigned long long (Interoperabilidad) |
| `I8` .. `I128` o `i8` .. `i128` | `int8_t` .. `__int128_t` | Enteros con signo de ancho fijo |
| `U8` .. `U128` o `u8` .. `u128` | `uint8_t` .. `__uint128_t` | Enteros sin signo de ancho fijo |
| `isize`, `usize` | `ptrdiff_t`, `size_t` | Enteros del tamaño de un puntero |
| `byte` | `uint8_t` | Alias para U8 |
| `F32`, `F64` o `f32`, `f64`  | `float`, `double` | Números de coma flotante |
| `bool` | `bool` | `true` o `false` |
| `char` | `char` | Carácter único |
| `string` | `char*` | Cadena de C (terminada en null) |
| `U0`, `u0`, `void` | `void` | Tipo vacío |
| `iN` (ej. `i256`) | `_BitInt(N)` | Entero con signo de ancho arbitrario (C23) |
| `uN` (ej. `u42`) | `unsigned _BitInt(N)` | Entero sin signo de ancho arbitrario (C23) |
| `rune` | `uint32_t` | Valor escalar Unicode (punto de código UTF-32) |

#### Literales
- **Enteros**: Decimal (`123`), Hex (`0xFF`), Octal (`0o755`), Binario (`0b1011`).
  - *Nota*: Los números con ceros a la izquierda se tratan como decimales (`0123` es `123`), a diferencia de C.
  - *Nota*: Los números pueden contener guiones bajos para mejorar la legibilidad (`1_000_000`, `0b_1111_0000`).
- **Flotantes**: Estándar (`3.14`), Científico (`1e-5`, `1.2E3`). Los números de punto flotante también soportan guiones bajos (`3_14.15_92`).

#### Unicode y Runas

Zen C proporciona soporte de primera clase para valores escalares Unicode a través del tipo `rune`. Una `rune` representa un único punto de código Unicode (codificado como un entero sin signo de 32 bits).

| Literal | Descripción |
|:---|:---|
| `'a'` | Carácter ASCII estándar |
| `'🚀'` | Carácter Unicode multi-byte |
| `'\u{2764}'` | Secuencia de escape Unicode (Hex) |

```zc
import "std.zc"

fn main() {
    let c = 'a';
    println "El carácter '{c}' tiene un código de {(int)c} en ASCII/Unicode";

    let codigo = 97;
    println "El código {codigo} corresponde al carácter {(char)codigo}";

    let r: rune = '🚀';
    println "La runa '{r}' tiene un código de {(uint)r} en Unicode";
    
    let r_codigo: uint = 128640;
    println "El código {r_codigo} corresponde a la runa '{(rune)r_codigo}'";

    let r_esc: rune = '\u{2764}';
    println "La runa '{r_esc}' tiene el código {(uint)r_esc} (0x{(uint)r_esc:X})";
}
```

{% alert(type="important") %}
**Mejores Prácticas para Código Portable**
- Usa **Tipos Portables** (`int`, `uint`, `i64`, `u8`, etc.) para toda la lógica pura de Zen C. `int` garantiza ser 32-bits con signo en todas las arquitecturas.
- Usa **Tipos de Interoperabilidad C** (`c_int`, `c_char`, `c_long`, ``c_ulong``, ``c_longlong``, ``c_ulonglong``) **sólo** al interactuar con bibliotecas C (FFI). Su tamaño varía según la plataforma y el compilador C.
- Usa `isize` y `usize` para indexado de arrays y aritmética de punteros.
{% end %}
