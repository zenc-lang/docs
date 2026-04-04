# std/math

Das Modul `Math` bietet einen Kernsatz an mathematischen Standardkonstanten und -funktionen. Es fungiert als Zen-C-Wrapper um die standardmäßigen mathematischen Gleitkommaoperationen.

## Überblick

- **Statische Methoden**: Alle Methoden werden direkt auf der `Math`-Struktur aufgerufen.
- **Präzision**: Verwendet `double` für hochpräzise Gleitkommaarithmetik.
- **Umfassend**: Deckt Trigonometrie, Exponentialfunktionen, Logarithmen und Rundungen ab.
- **Effizient**: Kapselt direkt optimierte C-Bibliotheksfunktionen ein.

## Verwendung

```zc
import "std/math.zc"

fn main() {
    let radius = 5.0;
    let area = Math::PI() * Math::pow(radius, 2.0);
    println "Kreisfläche: {area}";
}
```

## Konstanten

Alle Konstanten sind statische Funktionen, die ein `double` zurückgeben.

| Konstante | Beschreibung |
| :--- | :--- |
| **Math::PI()** | Archimedes-Konstante (ca. 3,14159). |
| **Math::E()** | Eulersche Zahl (ca. 2,71828). |

## Methoden

### Arithmetik

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **abs** | `abs(x: double) -> double` | Gibt den Absolutwert von `x` zurück. |
| **sqrt** | `sqrt(x: double) -> double` | Gibt die Quadratwurzel von `x` zurück. |
| **pow** | `pow(base: double, exp: double) -> double` | Gibt `base` hoch `exp` zurück. |
| **exp** | `exp(x: double) -> double` | Gibt `e` hoch `x` zurück. |
| **log** | `log(x: double) -> double` | Gibt den natürlichen Logarithmus (Basis e) von `x` zurück. |
| **log10** | `log10(x: double) -> double` | Gibt den Logarithmus zur Basis 10 von `x` zurück. |

### Trigonometrie

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **sin** | `sin(x: double) -> double` | Gibt den Sinus von `x` (Radiant) zurück. |
| **cos** | `cos(x: double) -> double` | Gibt den Kosinus von `x` (Radiant) zurück. |
| **tan** | `tan(x: double) -> double` | Gibt den Tangens von `x` (Radiant) zurück. |
| **asin** | `asin(x: double) -> double` | Gibt den Arkussinus von `x` zurück. |
| **acos** | `acos(x: double) -> double` | Gibt den Arkuskosinus von `x` zurück. |
| **atan** | `atan(x: double) -> double` | Gibt den Arkustangens von `x` zurück. |
| **atan2** | `atan2(y: double, x: double) -> double` | Gibt den Arkustangens von `y/x` zurück. |

### Rundung & Rest

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **ceil** | `ceil(x: double) -> double` | Rundet auf die nächste Ganzzahl auf. |
| **floor** | `floor(x: double) -> double` | Rundet auf die nächste Ganzzahl ab. |
| **round** | `round(x: double) -> double` | Rundet auf die nächstgelegene Ganzzahl. |
| **mod** | `mod(x: double, y: double) -> double` | Berechnet den Gleitkomma-Rest von `x / y`. |

### Min / Max

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **max** | `max(a: double, b: double) -> double` | Gibt den größeren von zwei Werten zurück. |
| **min** | `min(a: double, b: double) -> double` | Gibt den kleineren von zwei Werten zurück. |
