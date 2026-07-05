+++
title = "2. Primitive Types"
weight = 2
+++

# 2. Primitive Types {#2-primitive-types}


| Type | C Equivalent | Description |
|:---|:---|:---|
| `int`, `uint` | `int32_t`, `uint32_t` | 32-bit signed/unsigned integer |
| `c_char`, `c_uchar` | `char`, `unsigned char` | C char / unsigned char (Interop) |
| `c_short`, `c_ushort` | `short`, `unsigned short` | C short / unsigned short (Interop) |
| `c_int`, `c_uint` | `int`, `unsigned int` | C int / unsigned int (Interop) |
| `c_long`, `c_ulong` | `long`, `unsigned long` | C long / unsigned long (Interop) |
| `c_longlong`, `c_ulonglong` | `long long`, `unsigned long long` | C long long / unsigned long long (Interop) |
| `I8` .. `I128` or `i8` .. `i128` | `int8_t` .. `__int128_t` | Signed fixed-width integers |
| `U8` .. `U128` or `u8` .. `u128` | `uint8_t` .. `__uint128_t` | Unsigned fixed-width integers |
| `isize`, `usize` | `ptrdiff_t`, `size_t` | Pointer-sized integers |
| `byte` | `uint8_t` | Alias for U8 |
| `F32`, `F64` or `f32`, `f64`  | `float`, `double` | Floating point numbers |
| `bool` | `bool` | `true` or `false` |
| `char` | `char` | Single character |
| `string` | `char*` | C-string (null-terminated) |
| `U0`, `u0`, `void` | `void` | Empty type |
| `iN` (for example, `i256`) | `_BitInt(N)` | Arbitrary bit-width signed integer (C23) |
| `uN` (for example, `u42`) | `unsigned _BitInt(N)` | Arbitrary bit-width unsigned integer (C23) |
| `rune` | `uint32_t` | Unicode scalar value (UTF-32 code point) |

#### Literals
- **Integers**: Decimal (`123`), Hex (`0xFF`), Octal (`0o755`), Binary (`0b1011`).
  - *Note*: Numbers with leading zeros are treated as decimal (`0123` is `123`), unlike C.
  - *Note*: Numbers can contain underscores for readability (`1_000_000`, `0b_1111_0000`).
- **Floats**: Standard (`3.14`), Scientific (`1e-5`, `1.2E3`). Floating point numbers also support underscores (`3_14.15_92`).

#### Unicode and Runes

Zen C provides first-class support for Unicode scalar values via the `rune` type. A `rune` represents a single Unicode code point (encoded as a 32-bit unsigned integer).

| Literal | Description |
|:---|:---|
| `'a'` | Standard ASCII character |
| `'🚀'` | Multi-byte Unicode character |
| `'\u{2764}'` | Unicode escape sequence (Hex) |

```zc
import "std.zc"

fn main() {
    let c = 'a';
    println "The character '{c}' has a code of {(int)c} in ASCII/Unicode";

    let code = 97;
    println "The code {code} corresponds to the character {(char)code}";

    let r: rune = '🚀';
    println "The rune '{r}' has a code of {(uint)r} in Unicode";
    
    let r_code: uint = 128640;
    println "The code {r_code} corresponds to the rune '{(rune)r_code}'";

    let r_esc: rune = '\u{2764}';
    println "The rune '{r_esc}' has code {(uint)r_esc} (0x{(uint)r_esc:X})";
}
```

{% alert(type="important") %}
**Best Practices for Portable Code**
- Use **Portable Types** (`int`, `uint`, `i64`, `u8`, etc.) for all pure Zen C logic. `int` is guaranteed to be 32-bit signed on all architectures.
- Use **C Interop Types** (`c_int`, `c_char`, `c_long`, ``c_ulong``, ``c_longlong``, ``c_ulonglong``) **only** when interacting with C libraries (FFI). Their size varies by platform and C compiler (e.g. `c_long` size differs between Windows and Linux).
- Use `isize` and `usize` for array indexing and memory pointer arithmetic.
{% end %}
