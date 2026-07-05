+++
title = "17. Regole MISRA"
weight = 17
+++

# 17. Regole MISRA

Zen C include una **modalita di conformita MISRA C:2012** attivata con il flag `--misra`.
Oltre ai controlli MISRA standard, il compilatore applica diverse **regole specifiche di Zen**
che promuovono codice piu sicuro e manutenibile.

#### Attivare la modalita MISRA

```bash
zc build app.zc --misra
```

Le violazioni vengono segnalate come errori del compilatore in fase di compilazione:

```text
error: MISRA Rule Zen 2.2: tuple with 3 or more fields shall be replaced
       with a named struct (use 'struct' instead of positional tuple)
  --> app.zc:5:1
   |
 5 | fn get_stats() -> (int, int, int) { ... }
```

{% alert(type="note") %}
Il testo dello standard MISRA e protetto da copyright di MISRA Consortium Ltd.
L'implementazione di Zen C verifica la conformita ma non riproduce lo standard.
Per le definizioni ufficiali delle regole, fare riferimento alla documentazione
[MISRA C:2012](https://www.misra.org.uk/).
{% end %}

#### Regole Specifiche di Zen

Queste regole sono uniche per Zen C. Ogni regola viene controllata quando `--misra` e attivo.

#### Zen 1.1 -- Nessun blocco raw

Vieta i blocchi `raw { }` che aggirano il transpilatore.

```zc
// Bad:
fn main() {
    raw { int x = 10; }
}

// Good:
fn main() {
    let x = 10;
}
```

#### Zen 1.2 -- Nessun blocco plugin

Vieta i blocchi `plugin ... end`, che eseguono codice arbitrario in fase di compilazione.

```zc
// Bad:
plugin my_plugin

// Good:
import "std/some_module.zc"
```

#### Zen 1.3 -- Match esaustivo sugli enum

Vieta il jolly `_` nel `match` su tipi enum -- tutte le varianti devono essere gestite esplicitamente.

```zc
enum Color { Red; Green; Blue; }

// Bad -- missing Blue:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
    }
}

// Good:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
        Color::Blue => { println "blue"; }
    }
}
```

#### Zen 1.4 -- Nessuna direttiva di preprocessore

Vieta le direttive del preprocessore C (`#define`, `#include`, `#if`, ecc.).
Usare invece `import` e `def` di Zen.

```zc
// Bad:
#define BUFFER_SIZE 256
#include <stdio.h>

// Good:
def BUFFER_SIZE = 256;
import "std/io.zc"
```

#### Zen 1.5 -- Nessun `var` / `const` per le dichiarazioni

Le parole chiave `var` e `const` sono deprecate per le dichiarazioni di variabili/costanti.
Usare `let` per le variabili e `def` per le costanti a tempo di compilazione.

```zc
// Bad:
var x = 10;
const MAX = 100;

// Good:
let x = 10;
def MAX = 100;
```

> `const` rimane valido come **qualificatore di tipo** per l'interoperabilita con C
> (es. `const int` nelle dichiarazioni FFI).

#### Zen 1.8 -- Nessun oscuramento di identificatori

Vieta di dichiarare un nome che nasconde uno di un ambito esterno.

```zc
let x = 10;
if true {
    // Bad -- shadows outer x:
    let x = 20;
}

// Good:
if true {
    let inner_x = 20;
}
```

#### Zen 2.1 -- Nessun identificatore riservato

Vieta gli identificatori che iniziano con `__`, `_[A-Z]` o `_z_`, che sono riservati
per il compilatore e l'implementazione C.

```zc
// Bad:
let __my_var = 10;
let _Reserved = 20;
let _z_internal = 30;

// Good:
let my_var = 10;
let reserved = 20;
let internal = 30;
```

#### Zen 2.2 -- Limite dimensione tuple

Le tuple con **3 o piu campi** non devono essere utilizzate come tipi di ritorno o
parametri di funzione. Usare invece una struttura con nome. Le 2-tuple sono esenti.

```zc
// Bad -- 3-tuple as return type:
fn get_stats() -> (int, int, int) { ... }
fn process(p: (int, string, bool)) { ... }

// Good -- use a struct:
struct Stats { sum: int; avg: int; max: int; }
fn get_stats() -> Stats { ... }

// OK -- 2-tuples are exempt:
fn get_pair() -> (int, int) { ... }
```

#### Zen 2.3 -- Confronto di stringhe

`string == string` non deve essere usato. Usare `strcmp()` invece.

```zc
// Bad (when a, b are string):
if a == b { ... }

// Good:
if strcmp(a, b) == 0 { ... }

// OK -- int, bool, pointer comparisons are safe:
if x == y { ... }
```

## Copertura Standard MISRA C:2012

Il compilatore verifica le seguenti regole standard MISRA C:2012.
Clicca su un capitolo per espandere l'elenco delle regole.

{% misra_table() %}

Per il testo completo delle regole, fare riferimento alla documentazione ufficiale
[MISRA C:2012](https://www.misra.org.uk/).
