+++
title = "2. Tipi Primitivi"
weight = 2
+++

# 2. Tipi Primitivi {#2-tipi-primitivi}


| Tipo | C Equivalent | Descrizione |
|:---|:---|:---|
| `int`, `uint` | `int32_t`, `uint32_t` | Intero a 32 bit con segno/senza segno |
| `c_char`, `c_uchar` | `char`, `unsigned char` | C char (Interop) |
| `c_short`, `c_ushort` | `short`, `unsigned short` | C short (Interop) |
| `c_int`, `c_uint` | `int`, `unsigned int` | C int (Interop) |
| `c_long`, `c_ulong` | `long`, `unsigned long` | C long (Interop) |
| `c_longlong`, `c_ulonglong` | `long long`, `unsigned long long` | C long long / unsigned long long (Interop) |
| `I8` .. `I128` or `i8` .. `i128` | `int8_t` .. `__int128_t` | Interi a grandezza fissa con segno |
| `U8` .. `U128` or `u8` .. `u128` | `uint8_t` .. `__uint128_t` | Interi a grandezza fissa senza segno |
| `isize`, `usize` | `ptrdiff_t`, `size_t` | Interi con grandezza di un puntatore |
| `byte` | `uint8_t` | Alias per U8 |
| `F32`, `F64` or `f32`, `f64`  | `float`, `double` | Numeri con parte decimale |
| `bool` | `bool` | `true` (lett. _vero_) o `false` (lett. _falso_) |
| `char` | `char` | Carattere singolo |
| `string` | `char*` | Stringhe C terminate da NULL |
| `U0`, `u0`, `void` | `void` | Tipo vuoto |
| `iN` (es. `i256`) | `_BitInt(N)` | Intero con segno di ampiezza arbitraria (C23) |
| `uN` (es. `u42`) | `unsigned _BitInt(N)` | Intero senza segno di ampiezza arbitraria (C23) |
| `rune` | `uint32_t` | Valore scalare Unicode (punto di codice UTF-32) |

#### Unicode e Rune

Zen C fornisce supporto di prima classe per i valori scalari Unicode tramite il tipo `rune`. Una `rune` rappresenta un singolo punto di codice Unicode (codificato come un intero non segnato a 32 bit).

| Letterale | Descrizione |
|:---|:---|
| `'a'` | Carattere ASCII standard |
| `'🚀'` | Carattere Unicode multi-byte |
| `\u{2764}'` | Sequenza di escape Unicode (Hex) |

```zc
import "std.zc"

fn main() {
    let c = 'a';
    println "Il carattere '{c}' ha un codice di {(int)c} in ASCII/Unicode";

    let codice = 97;
    println "Il codice {codice} corrisponde al carattere {(char)codice}";

    let r: rune = '🚀';
    println "La runa '{r}' ha un codice di {(uint)r} in Unicode";
    
    let r_code: uint = 128640;
    println "Il codice {r_code} corrisponde alla runa '{(rune)r_code}'";

    let r_esc: rune = '\u{2764}';
    println "La runa '{r_esc}' ha il codice {(uint)r_esc} (0x{(uint)r_esc:X})";
}
```

#### Letterali
- **Interi**: Decimali (`123`), Hex (`0xFF`), Ottali (`0o755`), Binari (`0b1011`).
  - *Nota*: I numeri con zeri iniziali sono trattati come decimali (`0123` è `123`), a differenza del C.
  - *Nota*: I numeri possono contenere trattini bassi per leggibilità (`1_000_000`, `0b_1111_0000`).
- **A virgola mobile**: Standard (`3.14`), Scientifico (`1e-5`, `1.2E3`). I numeri in virgola mobile supportano anche i trattini bassi (`3_14.15_92`).

{% alert(type="important") %}
**Best Practice per Codice Portabile**
- Usa **Tipi Portabili** (`int`, `uint`, `i64`, `u8`, ecc.) per tutta la logica Zen C pura. `int` è garantito essere a 32-bit con segno su tutte le architetture.
- Usa **Tipi di Interop C** (`c_int`, `c_char`, `c_long`, ``c_ulong``, ``c_longlong``, ``c_ulonglong``) **solo** quando interagisci con librerie C (FFI). La loro dimensione varia in base alla piattaforma e al compilatore C.
- Usa `isize` e `usize` per indicizzazione di array e aritmetica dei puntatori.
{% end %}
