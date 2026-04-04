# std/bigint

`BigInt` fornisce aritmetica intera a precisione arbitraria per Zen-C. Consente calcoli con interi che superano la capacità dei tipi numerici standard come `u64`.

## Panoramica

- **Precisione Arbitraria**: I numeri sono limitati solo dalla memoria disponibile.
- **Basato sul decimale**: Attualmente utilizza una semplice rappresentazione in base 10 per semplicità.
- **RAII**: Implementa il tratto `Drop` per la gestione automatica della memoria dello storage interno delle cifre.
- **Conveniente**: Supporta l'overloading degli operatori per un'aritmetica intuitiva.

## Utilizzo

```zc
import "std/bigint.zc"

fn main() {
    let a = BigInt::from_int(1_000_000_000_000_000);
    let b = BigInt::from_int(2_000_000_000_000_000);
    
    // Utilizza l'overloading degli operatori
    let sum = a + b; 
    
    let s = sum.to_string();
    println "Somma: {s}";
    free(s);
} // sum, a e b vengono liberati automaticamente qui
```

## Definizione della Struttura

```zc
struct BigInt {
    digits: Vec<u8>*;
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `BigInt::new() -> BigInt` | Crea un nuovo `BigInt` inizializzato a 0. |
| **from_int** | `BigInt::from_int(val: u64) -> BigInt` | Crea un nuovo `BigInt` da un intero a 64 bit. |

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **add_in_place** | `add_in_place(self, other: BigInt)` | Aggiunge `other` a `self` mutando lo stato interno. |

### Utilità

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **clone** | `clone(self) -> BigInt` | Restituisce una copia profonda del `BigInt`. |
| **to_string** | `to_string(self) -> char*` | Restituisce una rappresentazione in stringa allocata nell'heap. |

## Operatori

| Operatore | Metodo | Descrizione |
| :--- | :--- | :--- |
| `+` | **add** | Restituisce un nuovo `BigInt` contenente la somma di due valori. |
| `{}` | **to_string** | Abilita automaticamente l'interpolazione nelle stringhe formattate. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free_mem** | `free_mem(self)` | Libera manualmente il `Vec` sottostante e lo storage del `BigInt`. |
| **Tratto** | `impl Drop for BigInt` | Chiama automaticamente `free_mem()` quando esce dall'ambito. |
