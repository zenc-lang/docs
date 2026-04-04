# std/random

Das Modul `std/random` bietet einen idiomatischen, objektorientierten Pseudozufallszahlengenerator (PRNG) als Wrapper um die POSIX `<stdlib.h>` Funktionen.

## Verwendung

```zc
import "std/random.zc"

fn main() {
    // Initialisiert den Generator automatisch mit der aktuellen Zeit
    let rng = Random::new();

    // Zufällige Ganzzahlen generieren
    let bounded = rng.next_int_range(1, 100); // 1 bis 100 einschließlich
    
    println "Gewürfelt: {bounded}";
}
```

## Struktur-Definition

```zc
struct Random {
    seed: U32;
}
```

## Methoden

### Initialisierung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Random::new() -> Random` | Erstellt einen neuen Zufallgenerator, der mit der aktuellen Systemzeit initialisiert wurde. |
| **from_seed** | `Random::from_seed(seed: U32) -> Random` | Erstellt einen neuen Zufallgenerator unter Verwendung eines spezifischen Seeds. |

### Generierung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **next_int** | `next_int(self) -> int` | Gibt eine zufällige Ganzzahl im rohen Bereich `[0, RAND_MAX]` zurück. |
| **next_int_range** | `next_int_range(self, min: int, max: int) -> int` | Gibt eine zufällige Ganzzahl im Bereich `[min, max]` einschließlich zurück. |
| **next_double** | `next_double(self) -> double` | Gibt eine zufällige Gleitkommazahl im Bereich `[0.0, 1.0)` zurück. |
| **next_bool** | `next_bool(self) -> bool` | Gibt einen zufälligen booleschen Wert zurück. |
