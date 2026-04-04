# std/bigfloat

Das Modul `std/bigfloat` bietet Gleitkomma-Arithmetik mit beliebiger Präzision. Es ermöglicht Berechnungen mit einer wesentlich höheren Genauigkeit als die Standardtypen `float` oder `double`.

## Überblick

- **Beliebige Präzision**: Legen Sie die Anzahl der Bits für die Mantisse fest.
- **Rundungsmodi**: Unterstützung für verschiedene Rundungsstrategien (Auf die nächste Stelle, Richtung Null, etc.).
- **Mathematische Funktionen**: Hochpräzise Implementierungen von `sin`, `cos`, `exp`, `log`, etc.
- **Interoperabilität**: Einfache Konvertierung von und in Standard-Numeriktypen.

## Verwendung

```zc
import "std/bigfloat.zc"

fn main() {
    // BigFloat mit 256-Bit Präzision erstellen
    let pi = BigFloat::from_str("3.1415926535897932384626433832795028841971", 256);
    
    let radius = BigFloat::from_f64(10.5);
    let area = pi * (radius * radius);
    
    println "Fläche mit hoher Präzision: {area.to_string(20)}";
}
```

## Struktur-Definition

```zc
struct BigFloat {
    // Interne Darstellung
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **from_f64** | `BigFloat::from_f64(val: f64) -> BigFloat` | Erstellt ein BigFloat aus einem 64-Bit-Float. |
| **from_str** | `BigFloat::from_str(s: char*, prec: usize) -> BigFloat` | Analysiert ein BigFloat aus einem String mit der angegebenen Präzision. |

### Arithmetik

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **add** | `add(self, other: BigFloat) -> BigFloat` | Addiert zwei BigFloats. |
| **sub** | `sub(self, other: BigFloat) -> BigFloat` | Subtrahiert zwei BigFloats. |
| **mul** | `mul(self, other: BigFloat) -> BigFloat` | Multipliziert zwei BigFloats. |
| **div** | `div(self, other: BigFloat) -> BigFloat` | Dividiert zwei BigFloats. |

### Hilfsmittel

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **to_string** | `to_string(self, digits: usize) -> String` | Konvertiert das BigFloat in einen String mit `digits` Präzision. |
| **to_f64** | `to_f64(self) -> f64` | Konvertiert in einen Standard-64-Bit-Float (Präzisionsverlust möglich). |
