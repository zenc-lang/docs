# std/math

Il modulo `Math` fornisce un set principale di costanti e funzioni matematiche standard. Agisce come un wrapper Zen-C intorno alle operazioni matematiche standard in virgola mobile.

## Panoramica

- **Metodi Statici**: Tutti i metodi vengono chiamati direttamente sulla struttura `Math`.
- **Precisione**: Utilizza `double` per l'aritmetica in virgola mobile ad alta precisione.
- **Completo**: Copre trigonometria, esponenziali, logaritmi e arrotondamenti.
- **Efficiente**: Avvolge direttamente le funzioni ottimizzate della libreria C.

## Utilizzo

```zc
import "std/math.zc"

fn main() {
    let raggio = 5.0;
    let area = Math::PI() * Math::pow(raggio, 2.0);
    println "Area del cerchio: {area}";
}
```

## Costanti

Tutte le costanti sono funzioni statiche che restituiscono un `double`.

| Costante | Descrizione |
| :--- | :--- |
| **Math::PI()** | Costante di Archimede (circa 3.14159). |
| **Math::E()** | Numero di Eulero (circa 2.71828). |

## Metodi

### Aritmetica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **abs** | `abs(x: double) -> double` | Restituisce il valore assoluto di `x`. |
| **sqrt** | `sqrt(x: double) -> double` | Restituisce la radice quadrata di `x`. |
| **pow** | `pow(base: double, exp: double) -> double` | Restituisce `base` elevato alla potenza di `exp`. |
| **exp** | `exp(x: double) -> double` | Restituisce `e` elevato alla potenza di `x`. |
| **log** | `log(x: double) -> double` | Restituisce il logaritmo naturale (base-e) di `x`. |
| **log10** | `log10(x: double) -> double` | Restituisce il logaritmo in base 10 di `x`. |

### Trigonometria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **sin** | `sin(x: double) -> double` | Restituisce il seno di `x` (radianti). |
| **cos** | `cos(x: double) -> double` | Restituisce il coseno di `x` (radianti). |
| **tan** | `tan(x: double) -> double` | Restituisce la tangente di `x` (radianti). |
| **asin** | `asin(x: double) -> double` | Restituisce l'arcoseno di `x`. |
| **acos** | `acos(x: double) -> double` | Restituisce l'arcocoseno di `x`. |
| **atan** | `atan(x: double) -> double` | Restituisce l'arcotangente di `x`. |
| **atan2** | `atan2(y: double, x: double) -> double` | Restituisce l'arcotangente di `y/x`. |

### Arrotondamento e Resto

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **ceil** | `ceil(x: double) -> double` | Arrotonda per eccesso all'intero più vicino. |
| **floor** | `floor(x: double) -> double` | Arrotonda per difetto all'intero più vicino. |
| **round** | `round(x: double) -> double` | Arrotonda all'intero più vicino. |
| **mod** | `mod(x: double, y: double) -> double` | Calcola il resto in virgola mobile di `x / y`. |

### Min / Max

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **max** | `max(a: double, b: double) -> double` | Restituisce il maggiore tra due valori. |
| **min** | `min(a: double, b: double) -> double` | Restituisce il minore tra due valori. |
