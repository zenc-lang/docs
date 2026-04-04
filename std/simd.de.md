# std/simd

Zen-C bietet native SIMD (Single Instruction, Multiple Data) Vektortypen, die direkt in hardwareoptimierte Vektorinstruktionen (SSE, AVX, NEON, etc.) kompiliert werden, welche vom Target-Backend unterstützt werden.

## Überblick

- **Native Leistung**: Nutzt LLVM/GCC Vektorerweiterungen für maximale Effizienz.
- **Implizit Portabel**: Typen wie `f32x4` werden auf die beste verfügbare 128-Bit-Hardware der jeweiligen Architektur abgebildet.
- **Elementweise Arithmetik**: Standardoperatoren (`+`, `-`, `*`, `/`) werden gleichzeitig auf alle Lanes angewendet.
- **Broadcasting**: Die Initialisierung mit einem einzelnen Wert überträgt diesen auf alle Lanes.

## Verwendung

```zc
import "std/simd.zc"

fn main() {
    // Initialisierung (Explizite Lanes)
    let a = f32x4 { 1.0, 2.0, 3.0, 4.0 };
    
    // Broadcasting (Einzelner Wert für alle Lanes)
    let b = f32x4 { v: 2.0 };
    
    // Elementweise Addition
    let c = a + b;   // Ergebnis: { 3.0, 4.0, 5.0, 6.0 }
    
    // Lane-Zugriff
    let first = c[0];
}
```

## Vektortypen

Die Standardbibliothek definiert mehrere 128-Bit- und 256-Bit-Vektortypen. Sie können auch benutzerdefinierte Typen mit dem Attribut `@vector(N)` definieren.

### 128-Bit Vektoren (SSE / NEON)

| Typ | Elementtyp | Lanes | Byte-Größe |
| :--- | :--- | :--- | :--- |
| `f32x4` | `f32` | 4 | 16 |
| `f64x2` | `f64` | 2 | 16 |
| `i32x4` | `i32` | 4 | 16 |
| `u32x4` | `u32` | 4 | 16 |
| `i64x2` | `i64` | 2 | 16 |
| `u64x2` | `u64` | 2 | 16 |
| `i16x8` | `i16` | 8 | 16 |
| `u16x8` | `u16` | 8 | 16 |
| `i8x16` | `i8` | 16 | 16 |
| `u8x16` | `u8` | 16 | 16 |

### 256-Bit Vektoren (AVX / AVX2)

| Typ | Elementtyp | Lanes | Byte-Größe |
| :--- | :--- | :--- | :--- |
| `f32x8` | `f32` | 8 | 32 |
| `f64x4` | `f64` | 4 | 32 |
| `i32x8` | `i32` | 8 | 32 |
| `u32x8` | `u32` | 8 | 32 |
| `i64x4` | `i64` | 4 | 32 |
| `u64x4` | `u64` | 4 | 32 |
| `i16x16` | `i16` | 16 | 32 |
| `u16x16` | `u16` | 16 | 32 |
| `i8x32` | `i8` | 32 | 32 |
| `u8x32` | `u8` | 32 | 32 |

## Operationen

| Kategorie | Operator | Beschreibung |
| :--- | :--- | :--- |
| **Arithmetik** | `+`, `-`, `*`, `/` | Standardmäßige elementweise Addition, Subtraktion, Multiplikation und Division. |
| **Bitweise** | `&`, `\|`, `^`, `~` | Bitweises AND, OR, XOR und NOT über alle Lanes. |
| **Indizierung** | `[i]` | Zugriff auf oder Modifikation einzelner Lanes per Index. |
| **Vergleich** | `==`, `!=`, `<`, `>` | Gibt einen booleschen Maskenvektor zurück (Ergebnisse variieren je nach Backend). |
