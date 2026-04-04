# std/bigfloat

`BigFloat` fornisce aritmetica in virgola mobile decimale a precisione arbitraria per Zen-C. È implementato come un `BigInt` scalato, consentendo calcoli ad alta precisione senza errori di arrotondamento binario.

## Panoramica

- **Precisione Arbitraria**: Supporta numeri decimali di qualsiasi dimensione, limitati solo dalla memoria.
- **Rappresentazione Scalata**: Utilizza una magnitudo `BigInt` e un `scale` intero per rappresentare i valori decimali.
- **Controllo della Precisione**: Allinea facilmente le scale per addizioni e sottrazioni precise.
- **RAII**: La memoria per la magnitudo sottostante è gestita automaticamente tramite il tratto `Drop`.

## Utilizzo

```zc
import "std/bigfloat.zc"

fn main() {
    let a = BigFloat::from_int(123);
    a.scale = 2; // Rappresenta 1.23
    
    let b = BigFloat::from_int(4567);
    b.scale = 3; // Rappresenta 4.567
    
    let sum = a.add(b);
    
    let s = sum.to_string();
    println "Somma: {s}"; // Somma: 5.797
    free(s);
} // a, b e sum vengono liberati automaticamente qui
```

## Definizione della Struttura

```zc
struct BigFloat {
    magnitude: BigInt;
    scale: int;
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `BigFloat::new() -> BigFloat` | Crea un nuovo `BigFloat` inizializzato a 0.0. |
| **from_int** | `BigFloat::from_int(val: u64) -> BigFloat` | Crea un `BigFloat` da un intero con scala 0. |

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **add** | `add(self, other: BigFloat) -> BigFloat` | Somma due valori `BigFloat`, allineando automaticamente le loro scale. Restituisce un nuovo `BigFloat`. |
| **align_scale** | `align_scale(self, target_scale: int)` | Aumenta la scala del `BigFloat` a `target_scale` spostando la magnitudo. |

### Utilità

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **clone** | `clone(self) -> BigFloat` | Restituisce una copia profonda del `BigFloat`. |
| **to_string** | `to_string(self) -> char*` | Restituisce una rappresentazione in stringa allocata nell'heap con il punto decimale. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free_mem** | `free_mem(self)` | Libera manualmente la memoria `BigInt` sottostante. |
| **Tratto** | `impl Drop for BigFloat` | Chiama automaticamente `free_mem()` quando esce dall'ambito. |
