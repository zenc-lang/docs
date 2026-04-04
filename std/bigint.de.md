# std/bigint

Das Modul `std/bigint` bietet Ganzzahl-Arithmetik mit beliebiger Präzision. Es ermöglicht das Arbeiten mit Ganzzahlen, die den Bereich von 64-Bit-Ganzzahlen überschreiten.

## Überblick

- **Beliebige Größe**: Begrenzt nur durch den verfügbaren Speicher.
- **Effiziente Algorithmen**: Implementiert schnelle Multiplikations- und Divisionsalgorithmen.
- **Kryptographisch sicher**: Kann für kryptographische Anwendungen verwendet werden, die große Primzahlen erfordern.
- **Bitweise Operationen**: Volle Unterstützung für bitweise Logik auf großen Ganzzahlen.

## Verwendung

```zc
import "std/bigint.zc"

fn main() {
    // Erstelle BigInt aus einem String
    let a = BigInt::from_str("123456789012345678901234567890");
    let b = BigInt::from_int(1000);
    
    let result = a * b;
    println "Ergebnis: {result.to_string()}";
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **from_int** | `BigInt::from_int(val: i64) -> BigInt` | Erstellt ein BigInt aus einem 64-Bit-Integer. |
| **from_str** | `BigInt::from_str(s: char*) -> BigInt` | Erstellt ein BigInt aus einem String. |

### Arithmetik

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **add**| `add(self, other: BigInt) -> BigInt` | Addiert zwei BigInts. |
| **sub**| `sub(self, other: BigInt) -> BigInt` | Subtrahiert zwei BigInts. |
| **mul**| `mul(self, other: BigInt) -> BigInt` | Multipliert zwei BigInts. |
| **div**| `div(self, other: BigInt) -> BigInt` | Dividiert zwei BigInts. |
| **mod**| `mod(self, other: BigInt) -> BigInt` | Berechnet den Rest der Division. |
| **pow**| `pow(self, exp: u32) -> BigInt` | Berechnet die Potenz. |

### Utilities

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **to_string** | `to_string(self) -> String` | Konvertiert BigInt in einen String (Basis 10). |
| **to_hex** | `to_hex(self) -> String` | Konvertiert BigInt in einen Hexadezimal-String. |
| **is_prime** | `is_prime(self) -> bool` | Führt einen probabilistischen Primzahltest durch. |
