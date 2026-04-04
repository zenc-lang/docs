# std/complex

Die `std/complex`-Bibliothek bietet die `Complex`-Struktur und wesentliche mathematische Operationen für die Arbeit mit komplexen Zahlen in Zen-C.

## Überblick

- **Werttyp**: Einfache Struktur mit `real`- und `imag`-Komponenten.
- **Operator-Unterstützung**: Unterstützt `+`, `-`, `*`, `/`, `==` und `!=` durch Operatorüberladung.
- **Eigenschaften**: Bietet Methoden zur Berechnung von Betrag und Phase.
- **Interpolation**: Kann direkt in f-Strings und Print-Anweisungen verwendet werden.

## Verwendung

```zc
import "std/complex.zc"

fn main() {
    let c1 = Complex::new(3.0, 4.0);
    let c2 = Complex::new(1.0, 2.0);
    
    let sum = c1 + c2;
    let prod = c1 * c2;
    
    println "Summe: {sum}";       // Summe: 4.000000 + 6.000000i
    println "Betrag: {c1.magnitude()}";
}
```

## Struktur-Definition

```zc
struct Complex {
    real: double;
    imag: double;
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Complex::new(r: double, i: double) -> Complex` | Erstellt eine neue komplexe Zahl mit der Realteil-Komponente `r` und der Imaginärteil-Komponente `i`. |

### Zugriff & Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **magnitude** | `magnitude(self) -> double` | Gibt den Betrag (Absolutwert) der komplexen Zahl zurück. |
| **phase** | `phase(self) -> double` | Gibt die Phase (Winkel) in Radiant zurück. |

## Operatoren

| Operator | Methode | Beschreibung |
| :--- | :--- | :--- |
| `+` | **add** | Addiert zwei komplexe Zahlen. |
| `-` | **sub** | Subtrahiert eine komplexe Zahl von einer anderen. |
| `*` | **mul** | Multipliziert zwei komplexe Zahlen. |
| `/` | **div** | Dividiert eine komplexe Zahl durch eine andere. |
| `==` | **eq** | Prüft, ob zwei komplexe Zahlen strikt gleich sind. |
| `!=` | **neq** | Prüft, ob zwei komplexe Zahlen nicht gleich sind. |
| `{}` | **to_string** | Ermöglicht direkte String-Interpolation. |
