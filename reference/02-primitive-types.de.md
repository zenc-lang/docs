+++
title = "2. Primitive Typen"
weight = 2
+++

# 2. Primitive Typen {#2-primitive-typen}


| Typ | C-Äquivalent | Beschreibung |
|:---|:---|:---|
| `int`, `uint` | `int32_t`, `uint32_t` | 32-Bit vorzeichenbehaftete/vorzeichenlose Ganzzahl |
| `c_char`, `c_uchar` | `char`, `unsigned char` | C-`char` / `unsigned char` (Interoperabilität) |
| `c_short`, `c_ushort` | `short`, `unsigned short` | C-`short` / `unsigned short` (Interoperabilität) |
| `c_int`, `c_uint` | `int`, `unsigned int` | C-`int` / `unsigned int` (Interoperabilität) |
| `c_long`, `c_ulong` | `long`, `unsigned long` | C-`long` / `unsigned long` (Interoperabilität) |
| `c_longlong`, `c_ulonglong` | `long long`, `unsigned long long` | C-`long long` / `unsigned long long` (Interoperabilität) |
| `I8` .. `I128` oder `i8` .. `i128` | `int8_t` .. `__int128_t` | Vorzeichenbehaftete Ganzzahlen mit fester Bitbreite |
| `U8` .. `U128` oder `u8` .. `u128` | `uint8_t` .. `__uint128_t` | Vorzeichenlose Ganzzahlen mit fester Bitbreite |
| `isize`, `usize` | `ptrdiff_t`, `size_t` | Ganzzahlen mit Zeigergröße |
| `byte` | `uint8_t` | Alias für `U8` |
| `F32`, `F64` oder `f32`, `f64` | `float`, `double` | Gleitkommazahlen |
| `bool` | `bool` | `true` oder `false` |
| `char` | `char` | Einzelnes Zeichen |
| `string` | `char*` | C-String (nullterminiert) |
| `U0`, `u0`, `void` | `void` | Leerer Typ |
| `iN` (z. B. `i256`) | `_BitInt(N)` | Ganzzahl mit beliebiger Bitbreite (vorzeichenbehaftet, C23) |
| `uN` (z. B. `u42`) | `unsigned _BitInt(N)` | Ganzzahl mit beliebiger Bitbreite (vorzeichenlos, C23) |
| `rune` | `uint32_t` | Unicode-Skalarwert (UTF-32-Codepunkt) |

#### Literale
- **Ganzzahlen**: Dezimal (`123`), Hexadezimal (`0xFF`), Oktal (`0o755`), Binär (`0b1011`).
- *Hinweis*: Zahlen mit führenden Nullen werden als Dezimalzahlen behandelt (`0123` ist `123`), anders als in C.
- *Hinweis*: Zahlen können zur besseren Lesbarkeit Unterstriche enthalten (`1_000_000`, `0b_1111_0000`).
- **Gleitkommazahlen**: Standard (`3.14`), Wissenschaftlich (`1e-5`, `1.2E3`). Gleitkommazahlen unterstützen auch Unterstriche (`3_14.15_92`).

#### Unicode und Runen

Zen C bietet erstklassige Unterstützung für Unicode-Skalarwerte über den Typ `rune`. Eine `rune` repräsentiert einen einzelnen Unicode-Codepunkt (kodiert als 32-Bit-Ganzzahl ohne Vorzeichen).

| Literal | Beschreibung |
|:---|:---|
| `'a'` | Standard-ASCII-Zeichen |
| `'🚀'` | Mehrbyte-Unicode-Zeichen |
| `'\u{2764}'` | Unicode-Escape-Sequenz (Hex) |

```zc
import "std.zc"

fn main() {
    let c = 'a';
    println "Das Zeichen '{c}' hat den Code {(int)c} in ASCII/Unicode";

    let code = 97;
    println "Der Code {code} entspricht dem Zeichen {(char)code}";

    let r: rune = '🚀';
    println "Die Rune '{r}' hat den Unicode-Code {(uint)r}";
    
    let r_code: uint = 128640;
    println "Der Code {r_code} entspricht der Rune '{(rune)r_code}'";

    let r_esc: rune = '\u{2764}';
    println "Die Rune '{r_esc}' hat den Code {(uint)r_esc} (0x{(uint)r_esc:X})";
}
```

{% alert(type="important") %}
**Bewährte Vorgehensweisen für portablen Code**

- Verwende **portable Datentypen** (`int`, `uint`, `i64`, `u8` usw.) für die gesamte reine Zen-C-Logik. `int` ist auf allen Architekturen garantiert 32-Bit-Datentypen mit Vorzeichen.
- Verwende **C-Interop-Datentypen** (`c_int`, `c_char`, `c_long`, `c_ulong`, `c_longlong`, `c_ulonglong`) **nur** bei der Interaktion mit C-Bibliotheken (FFI). Deren Größe variiert je nach Plattform und C-Compiler (z. B. unterscheidet sich die Größe von `c_long` zwischen Windows und Linux).
- Verwende `isize` und `usize` für Array-Indizierung und Speicherzeigerarithmetik.
{% end %}
