+++
title = "4. Funzioni e Lambda"
weight = 4
+++

# 4. Funzioni e Lambda {#4-funzioni-e-lambda}


#### Funzioni
```zc
fn somma(a: int, b: int) -> int {
    return a + b;
}

// Supporto per argomenti nominati nelle chiamate
somma(a: 10, b: 20);
```

{% alert(type="note") %}
Gli argomenti nominati devono seguire rigorosamente l'ordine predefinito dei parametri. `somma(b: 20, a: 10)` è errato.
{% end %}

#### Argomenti Costanti
Gli argomenti di una funzione possono essere marcati come `const` (lett. _costanti_) per reinforzare semantiche di sola lettura. Questo è un qualificatore del tipo, non una costante esplicita.

```zc
fn stampa_valore(v: const int) {
    // v = 10; // Errore: Impossibile assegnare un valore ad una variabile costante
    println "{v}";
}
```

#### Argomenti di default
Le funzioni posso definire dei valori default per gli argomenti in caso che questi non vengano specificati durante la chiamata. Questi valori possono essere letterali, espressioni, o codice Zen C valido (come il costruttore di uno struct).
```zc
// Valore default semplice
fn incrementa(val: int, quantità: int = 1) -> int {
    return val + quantità;
}

// Espressione come valore default (calcolato)
fn offset(val: int, pad: int = 10 * 2) -> int {
    return val + pad;
}

// Struct come valore default
struct Config { debug: bool; }
fn init(cfg: Config = Config { debug: true }) {
    if cfg.debug { println "Modalità Debug"; }
}

fn main() {
    incrementa(10);      // 11
    offset(5);          // 25
    init();             // Stampa "Modalità Debug"
}
```

#### Lambda (Closure)
Funzioni anonime che possono catturare il loro ambiente.
```zc
let fattore = 2;
let raddoppia = x -> x * fattore;  // Sintassi con freccia
let pieno = fn(x: int) -> int { return x * fattore; }; // Sintassi a blocco

// Cattura per Riferimento (Sintassi a Blocco)
let val = 10;
let modify = fn[&]() { val += 1; }; 
modify(); // val ora è 11

// Cattura per Riferimento (Sintassi a Freccia)
let modify_arrow = [&] x -> val += x;
modify_arrow(5); // val ora è 16

// Cattura per Riferimento (Sintassi a Freccia con Argomenti Multipli)
let sum_into = [&] (a, b) -> val += (a + b);
sum_into(2, 2); // val ora è 20

// Cattura per Valore (Predefinito)
let original = 100;
let implicit = x -> original + x;       // Cattura implicita per valore (senza parentesi)
let explicit = [=] x -> original + x;   // Cattura esplicita per valore
// let fail = x -> original += x;       // Errore: impossibile assegnare a valore catturato

```

#### Puntatori-Funzione grezzi
Zen C supporta i puntatori-funzione grezzi utilizzando la sintassi `fn*`. Questo permette un'interoperabilità fluida con le librerie C che si aspettano puntatori-funzione senza overhead di closure.

```zc
// Funzione che prende un puntatore-funzione grezzo
fn imposta_callback(cb: fn*(int)) {
    cb(42);
}

// Funzione che restituisce un puntatore-funzione grezzo
fn ottieni_callback() -> fn*(int) {
    return il_mio_handler;
}

// I puntatori a puntatori-funzione sono supportati (fn**)
let pptr: fn**(int) = &ptr;
```

#### Argomenti Variadici
Le funzioni possono accettare un numero variabile di argomenti utilizzando la sintassi `...` e il tipo `va_list`.
```zc
fn log(lvl: int, fmt: char*, ...) {
    let ap: va_list;
    va_start(ap, fmt);
    vprintf(fmt, ap); // Usa lo stdio C
    va_end(ap);
}
```
