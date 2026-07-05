+++
title = "8. Gestione della memoria"
weight = 8
+++

# 8. Gestione della memoria


Zen C permette una gestione manuale della memoria con aiuti ergonomici.

#### Rimando
Esegui il codice quando l’ambito corrente termina. Le istruzioni defer vengono eseguite in ordine LIFO (last-in, first-out).
```zc
let f = fopen("file.txt", "r");
defer fclose(f);
```

> Per prevenire comportamenti indefiniti, le istruzioni del controllo di flusso (`return`, `break`, `continue`, `goto`) **non sono ammesse** dentro un blocco `defer`.

#### Liberazione automatica
Libera automaticamente la memoria occupata dalla variabile quando l'ambito corrente termina.
```zc
autofree let tipi = malloc(1024);
```

#### Semantiche delle risorse (Muovi di Default)
Zen C tratta i tipi con distruttori (come `File`, `Vec`, o puntatori allocati manualmente con `malloc`) come **Risorse**. Per prevenire errori di doppia-liberazione, le risorse non possono essere implicitamente duplicate.

- **Muovi di Default**: Assegnare una risorsa variabile ne trasferisce il proprietario. La variabile originale diventa invalida (Spostata).
- **Tipi di Copia**: Tipi senza distruttori possono opzionalmente avere un comportamento `Copy`, rendendo l'assegnazione una duplicazione.

**Diagnostica & Filosofia**:
Se vedi un errore "Utilizzo di una variabile spostata", il compilatore ti sta dicendo: *"Questo tipo è proprietario di una risorsa (come memoria o un handle) e copiarlo ciecamente non è sicuro."*

> **Contrasto:** Al contrario di come fanno C/C++, Zen C non duplica implicitamente i valori che posseggono risorse.

**Argomento di una funzione**:
Passare un valore ad una funzione segue le stesse regole dell'assegnazione: le risorse vengono spostate se non passate per referenza.

```zc
fn processo(r: Risorsa) { ... } // 'r' viene spostato nella funzione
fn peek(r: Risorsa*) { ... }    // 'r' viene preso in prestito (referenza)
```

**Clonazione Esplicita**:
Se *vuoi* avere più copie di una risorsa, rendilo esplicito:

```zc
let b = a.clona(); // Chiama il metodo `clona` dal tratto `Clone`
```

**Duplicazione opt-in (Tipi dei valori)**:
Per tipi piccoli senza distruttore:

```zc
struct Punto { x: int; y: int; }
impl Copy for Punto {} // Opt-in per la duplicazione implicita

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = p1; // Copiato. p1 rimane valido.
}
```

#### RAII / Rilascio Tratti
Implementa `Drop` per una logica di pulizia automatica.
```zc
impl Drop for MioStruct {
    fn drop(self) {
        self.free();
    }
}
```
