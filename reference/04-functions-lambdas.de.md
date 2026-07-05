+++
title = "4. Funktionen & Lambdas"
weight = 4
+++

# 4. Funktionen & Lambdas {#4-funktionen-lambdas}


#### Funktionen
```zc
fn addiere(a: int, b: int) -> int {
    return a + b;
}

// Benannte Argumente werden in Aufrufen unterstützt
addiere(a: 10, b: 20);
```

{% alert(type="note") %}
Benannte Argumente müssen strikt der definierten Parameterreihenfolge folgen.  
`addiere(b: 20, a: 10)` ist ungültig.
{% end %}

#### Const-Argumente
Funktionsargumente können als `const` markiert werden, um nur-lesende Semantik durchzusetzen.  
Dies ist ein Typqualifizierer, kein Konstantenwert.
```zc
fn drucke_wert(v: const int) {
    // v = 10; // Fehler: Zuweisung zu einer const-Variablen nicht erlaubt
    println "{v}";
}
```

#### Standardargumente
Funktionen können Standardwerte für nachgestellte Argumente definieren.  
Diese können Literale, Ausdrücke oder gültiger Zen C-Code sein (z. B. Struktur-Konstruktoren).
```zc
// Einfacher Standardwert
fn inkrement(val: int, menge: int = 1) -> int {
    return val + menge;
}

// Ausdruck als Standardwert (wird beim Aufruf ausgewertet)
fn versatz(val: int, pad: int = 10 * 2) -> int {
    return val + pad;
}

// Standardwert mit Struktur
struct Konfig { debug: bool; }
fn init(cfg: Konfig = Konfig { debug: true }) {
    if cfg.debug { println "Debug-Modus"; }
}

fn main() {
    inkrement(10);      // 11
    versatz(5);         // 25
    init();             // Gibt "Debug-Modus" aus
}
```

#### Lambdas (Closures)
Anonyme Funktionen, die ihre Umgebung erfassen können.
```zc
let faktor = 2;
let verdoppler = x -> x * faktor;  // Pfeil-Syntax
let komplett = fn(x: int) -> int { return x * faktor; }; // Block-Syntax

// Erfassen per Referenz (Block-Syntax)
let wert = 10;
let modifizieren = fn[&]() { wert += 1; }; 
modifizieren(); // wert ist jetzt 11

// Erfassen per Referenz (Pfeil-Syntax)
let modifizieren_pfeil = [&] x -> wert += x;
modifizieren_pfeil(5); // wert ist jetzt 16

// Erfassen per Referenz (Pfeil-Syntax mit mehreren Argumenten)
let summe_hinzu = [&] (a, b) -> wert += (a + b);
summe_hinzu(2, 2); // wert ist jetzt 20

// Erfassen per Wert (Standard)
let original = 100;
let implizit = x -> original + x;       // Implizites Erfassen per Wert (ohne Klammern)
let explizit = [=] x -> original + x;   // Explizites Erfassen per Wert
// let fehler = x -> original += x;     // Fehler: Zuweisung zu erfasstem Wert nicht erlaubt
```

#### Roh-Funktionszeiger
Zen C unterstützt Roh-Funktionszeiger wie in C über die `fn*`-Syntax.  
Dies ermöglicht eine nahtlose Interoperabilität mit C-Bibliotheken, die Funktionszeiger erwarten, ohne Closure-Overhead.

```zc
// Funktion, die einen Roh-Funktionszeiger als Parameter erhält
fn setze_callback(cb: fn*(int)) {
    cb(42);
}

// Funktion, die einen Roh-Funktionszeiger zurückgibt
fn hole_callback() -> fn*(int) {
    return mein_handler;
}

// Zeiger auf Funktionszeiger werden ebenfalls unterstützt (fn**)
let pptr: fn**(int) = &ptr;
```

#### Variadische Funktionen
Funktionen können eine variable Anzahl an Argumenten akzeptieren, indem `...` und der Typ `va_list` verwendet werden.
```zc
fn log(lvl: int, fmt: char*, ...) {
    let ap: va_list;
    va_start(ap, fmt);
    vprintf(fmt, ap); // Verwende C stdio
    va_end(ap);
}
```
