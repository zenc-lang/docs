# std/simd

Zen-C fornisce tipi vettoriali SIMD (Single Instruction, Multiple Data) nativi che vengono compilati direttamente in istruzioni vettoriali ottimizzate per l'hardware (SSE, AVX, NEON, ecc.) supportate dal backend di destinazione.

## Panoramica

- **Prestazioni Native**: Sfrutta le estensioni vettoriali di LLVM/GCC per la massima efficienza.
- **Implicitamente Portabile**: Tipi come `f32x4` si mappano sul miglior hardware a 128 bit disponibile specifico per l'architettura.
- **Aritmetica Elemento per Elemento**: Gli operatori standard (`+`, `-`, `*`, `/`) si applicano a tutte le corsie (lane) simultaneamente.
- **Broadcasting**: L'inizializzazione con un singolo valore lo trasmette a tutte le corsie.

## Utilizzo

```zc
import "std/simd.zc"

fn main() {
    // Inizializzazione (Corsie esplicite)
    let a = f32x4 { 1.0, 2.0, 3.0, 4.0 };
    
    // Broadcasting (Singolo valore a tutte le corsie)
    let b = f32x4 { v: 2.0 };
    
    // Addizione elemento per elemento
    let c = a + b;   // Risultato: { 3.0, 4.0, 5.0, 6.0 }
    
    // Accesso alla corsia
    let primo = c[0];
}
```

## Tipi Vettoriali

La libreria standard definisce diversi tipi vettoriali a 128 bit e 256 bit. Puoi anche definirne di personalizzati usando l'attributo `@vector(N)`.

### Vettori a 128 bit (SSE / NEON)

| Tipo | Tipo Elemento | Corsie | Dimensione in Byte |
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

### Vettori a 256 bit (AVX / AVX2)

| Tipo | Tipo Elemento | Corsie | Dimensione in Byte |
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

## Operazioni

| Categoria | Operatore | Descrizione |
| :--- | :--- | :--- |
| **Aritmetica** | `+`, `-`, `*`, `/` | Addizione, sottrazione, moltiplicazione e divisione standard elemento per elemento. |
| **Bit a Bit** | `&`, `\|`, `^`, `~` | AND, OR, XOR e NOT bit a bit su tutte le corsie. |
| **Indicizzazione**| `[i]` | Accedi o modifica le singole corsie tramite indice. |
| **Confronto** | `==`, `!=`, `<`, `>` | Restituisce un vettore maschera booleano (i risultati variano in base al backend). |
