+++
title = "17. MISRA-Regeln"
weight = 17
+++

# 17. MISRA-Regeln

Zen C beinhaltet einen **MISRA C:2012-Konformitatsmodus**, der mit dem `--misra`-Flag aktiviert wird.
Zusatzlich zu den standardmassigen MISRA-Prufungen erzwingt der Compiler mehrere **Zen-spezifische Regeln**,
die sichereren und wartbareren Code fordern.

#### MISRA-Modus aktivieren

```bash
zc build app.zc --misra
```

Verstosse werden als Compiler-Fehler zur Kompilierzeit gemeldet:

```
error: MISRA Rule Zen 2.2: tuple with 3 or more fields shall be replaced
       with a named struct (use 'struct' instead of positional tuple)
  --> app.zc:5:1
   |
 5 | fn get_stats() -> (int, int, int) { ... }
```

{% alert(type="note") %}
Der MISRA-Standardtext unterliegt dem Urheberrecht des MISRA Consortium Ltd. Die
Implementierung von Zen C pruft die Konformitat, gibt den Standard jedoch nicht wieder.
Die offiziellen Regeldefinitionen finden Sie in der Dokumentation zu
[MISRA C:2012](https://www.misra.org.uk/).
{% end %}

#### Zen-Spezifische Regeln

Diese Regeln sind einzigartig fur Zen C. Jede Regel wird gepruft, wenn `--misra` aktiv ist.

#### Zen 1.1 -- Keine Raw-Blocke

Verbietet `raw { }`-Blocke, die den Transpiler umgehen.

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

#### Zen 1.2 -- Keine Plugin-Blocke

Verbietet `plugin ... end`-Blocke, die beliebigen Build-Zeit-Code ausfuhren.

```zc
// Bad:
plugin my_plugin

// Good:
import "std/some_module.zc"
```

#### Zen 1.3 -- Vollstandiges Enum-Match

Verbietet den `_`-Platzhalter in `match` auf Enum-Typen -- alle Varianten mussen explizit behandelt werden.

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

#### Zen 1.4 -- Keine Praprozessor-Direktiven

Verbietet C-Praprozessor-Direktiven (`#define`, `#include`, `#if`, usw.).
Verwenden Sie stattdessen Zen's `import` und `def`.

```zc
// Bad:
#define BUFFER_SIZE 256
#include <stdio.h>

// Good:
def BUFFER_SIZE = 256;
import "std/io.zc"
```

#### Zen 1.5 -- Kein `var` / `const` fur Deklarationen

Die Schlusselworter `var` und `const` sind fur Variablen-/Konstantendeklarationen veraltet.
Verwenden Sie `let` fur Variablen und `def` fur Kompilierzeit-Konstanten.

```zc
// Bad:
var x = 10;
const MAX = 100;

// Good:
let x = 10;
def MAX = 100;
```

> `const` bleibt als **Typ-Qualifizierer** fur C-Interop gultig
> (z.B. `const int` in FFI-Deklarationen).

#### Zen 1.8 -- Kein Bezeichner-Shadowing

Verbietet die Deklaration eines Namens, der einen aus einem ausseren Gultigkeitsbereich verdeckt.

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

#### Zen 2.1 -- Keine reservierten Bezeichner

Verbietet Bezeichner, die mit `__`, `_[A-Z]` oder `_z_` beginnen, welche fur den Compiler
und die C-Implementierung reserviert sind.

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

#### Zen 2.2 -- Tupel-Grossenbeschrankung

Tupel mit **3 oder mehr Feldern** durfen nicht als Funktionsruckgabetypen oder
-parameter verwendet werden. Verwenden Sie stattdessen eine benannte Struktur.
2-Tupel sind ausgenommen.

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

#### Zen 2.3 -- String-Vergleich

`string == string` darf nicht verwendet werden. Verwenden Sie stattdessen `strcmp()`.

```zc
// Bad (when a, b are string):
if a == b { ... }

// Good:
if strcmp(a, b) == 0 { ... }

// OK -- int, bool, pointer comparisons are safe:
if x == y { ... }
```

## Standard-MISRA-C:2012-Abdeckung

Der Compiler pruft die folgenden standardmassigen MISRA-C:2012-Regeln.
Klicken Sie auf ein Kapitel, um die Regelliste zu erweitern.

{% misra_table() %}

Den vollstandigen Regeltext finden Sie in der offiziellen
[MISRA C:2012](https://www.misra.org.uk/)-Dokumentation.
