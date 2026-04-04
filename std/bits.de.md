# std/bits

Das Modul `std/bits` bietet Low-Level-Bitmanipulationsfunktionen, die oft direkt in effiziente CPU-Instruktionen kompiliert werden.

## Überblick

- **Rotation**: Links- und Rechtsrotation von Bits.
- **Zählen**: Führende Nullen, gesetzte Bits (Popcount).
- **Endianness**: Konvertierung zwischen Little-Endian und Big-Endian.
- **Portabilität**: Abstrahiert Compiler-Intrinsics für verschiedene Architekturen.

## Verwendung

```zc
import "std/bits.zc"

fn main() {
    let x: u32 = 0x12345678;
    
    // Bits rotieren
    let y = Bits::rotl32(x, 8);
    println "Rotiert: 0x{y:x}";
    
    // Gesetzte Bits zählen (Popcount)
    println "Gesetzte Bits: {Bits::popcount32(x)}";
}
```

## Funktionen

### Rotation

| Funktion | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **rotl32** | `rotl32(val: u32, shift: u32) -> u32` | Rotiert Bits in einem 32-Bit-Wert nach links. |
| **rotr32** | `rotr32(val: u32, shift: u32) -> u32` | Rotiert Bits in einem 32-Bit-Wert nach rechts. |
| **rotl64** | `rotl64(val: u64, shift: u32) -> u64` | Rotiert Bits in einem 64-Bit-Wert nach links. |
| **rotr64** | `rotr64(val: u64, shift: u32) -> u64` | Rotiert Bits in einem 64-Bit-Wert nach rechts. |

### Bit-Analyse

| Funktion | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **clz32** | `clz32(val: u32) -> u32` | Zählt führende Nullen in einem 32-Bit-Wert. |
| **ctz32** | `ctz32(val: u32) -> u32` | Zählt abschließende Nullen in einem 32-Bit-Wert. |
| **popcount32** | `popcount32(val: u32) -> u32` | Zählt die Anzahl der gesetzten Bits (1-Bits). |

### Endianness

| Funktion | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **bswap32** | `bswap32(val: u32) -> u32` | Vertauscht die Byte-Reihenfolge eines 32-Bit-Werts. |
| **bswap64** | `bswap64(val: u64) -> u64` | Vertauscht die Byte-Reihenfolge eines 64-Bit-Werts. |
