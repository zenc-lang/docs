+++
title = "3. Zusammengesetzte Typen"
weight = 3
+++

# 3. Zusammengesetzte Typen


#### Arrays
Festgrößen-Arrays mit Wertsemantik.
```zc
def SIZE = 5;
let ints: int[SIZE] = [1, 2, 3, 4, 5];
let zeros: [int; SIZE]; // Nullinitialisiert
```




#### Tuples

Mehrere Werte zu einem einzigen zusammengesetzten Wert gruppieren. Tupel unterstützen beliebige Stelligkeiten (2, 3, 4, … bis 10+), Verschachtelung, Mutation einzelner Felder und Destrukturierung.

**Grundlegende Verwendung**

```zc
let pair = (1, "hello");
let triple = (1, "hello", 3.14);
let five = (1, 2, 3, 4, 5);
let typed: (int, string, f64) = (1, "two", 3.0);
```

**Feldzugriff**

Elemente werden positionell mit `.0`, `.1`, `.2` usw. oder über die rohen Strukturfeldnamen `.v0`, `.v1` zugegriffen:

```zc
let t = (1, "hello", 3.14);
assert(t.0 == 1);
assert(t.v1 == "hello");
```

**Mehrere Rückgabewerte**

Funktionen können Tupel zurückgeben, um mehrere Ergebnisse zu liefern:

```zc
fn stats(data: int) -> (int, int) {
    return (data * 2, data + 1);
}
let r = stats(5);
assert(r.0 == 10);
assert(r.1 == 6);
```

**Destrukturierung**

```zc
let (sum, diff) = add_and_subtract(3, 2);
let (a: string, b: u8) = ("hello", 42);
let (x, y: i32) = (1, 2);
```

**Verschachtelte Tupel**

```zc
let nested = ((1, 2), (3, 4));
let inner = nested.v0;
assert(inner.v0 == 1);
```

**Mutation**

Einzelne Felder können neu zugewiesen werden:

```zc
let t = (1, 2);
t.v0 = 99;
```

**Zeichenkettenvergleich**

Tupel mit `string`-Feldern müssen für den Vergleich `strcmp()` verwenden, nicht `==` (das einen Zeigervergleich auf `char*` durchführt):

```zc
let t = (1, "hello");
assert(strcmp(t.1, "hello") == 0);
```

**Aufzählungstupel**

Aufzählungsvarianten können Tupeldaten tragen:

```zc
enum Shape {
    Point, Line(int, int), Labeled(int, string, f64),
}
```


#### Structs
Datenstrukturen mit optionalen Bitfeldern.
```zc
struct Punkt {
    x: int;
    y: int;
}

// Strukturinitialisierung
let p = Punkt { x: 10, y: 20 };

// Bitfelder
struct Flags {
    valid: U8 : 1;
    mode:  U8 : 3;
}
```

{% alert(type="important") %}
Strukturen verwenden standardmäßig die [Move-Semantik](@/tour/08-memory-management.de.md#resource-semantics-move-by-default). Felder können auch über `.` auf Zeiger zugegriffen werden (automatische Dereferenzierung).
{% end %}

#### Opake Strukturen
Du kannst eine Struktur als `opaque` definieren, um den Zugriff auf ihre Felder nur auf das definierende Modul zu beschränken, während die Struktur weiterhin auf dem Stack alloziert werden kann (die Größe ist bekannt).

```zc
// In user.zc
opaque struct Benutzer {
    id: int;
    name: string;
}

fn neuer_benutzer(name: string) -> Benutzer {
    return Benutzer{id: 1, name: name}; // OK: innerhalb des Moduls
}

// In main.zc
import "user.zc";

fn main() {
    let u = neuer_benutzer("Alice");
    // let id = u.id; // Fehler: Kein Zugriff auf privates Feld 'id'
}
```

#### Enums
Markierte Vereinigungen (Summentypen), die Daten speichern können.
```zc
enum Form {
    Kreis(float),       // speichert Radius
    Rechteck(float, float), // speichert Breite und Höhe
    Punkt               // keine Daten
}
```

#### Unions
Standard-C-Unions (unsicherer Zugriff).
```zc
union Daten {
    i: int;
    f: float;
}
```

#### SIMD-Vektoren
Native SIMD-Vektortypen unter Verwendung der GCC-/Clang-Vektorerweiterungen. Annotiere eine Struktur mit `@vector(N)`, um einen Vektor mit N Elementen zu definieren.
```zc
import "std/simd.zc";

fn main() {
    let a = f32x4{v: 1.0};              // Broadcast: {1.0, 1.0, 1.0, 1.0}
    let b = f32x4{1.0, 2.0, 3.0, 4.0};  // Initialisierung pro Element
    let c = a + b;                       // elementweise Addition
    let x = c[0];                        // Elementzugriff (float)
}
```

Arithmetische (`+`, `-`, `*`, `/`) und bitweise (`&`, `|`, `^`) Operatoren arbeiten elementweise. Vordefinierte Typen findest du in [`std/simd.zc`](std/simd.zc).

#### Typ-Aliase
Erstelle einen neuen Namen für einen bestehenden Typ.
```zc
alias ID = int;
alias PunktMap = Map<string, Punkt>;
alias OpFunktion = fn(int, int) -> int;
```

#### Opake Typ-Aliase
Du kannst einen Typ-Alias als `opaque` definieren, um einen neuen Typ zu erstellen, der **außerhalb des definierenden Moduls** vom zugrunde liegenden Typ unterscheidbar ist.  
Dies bietet **starke Kapselung** und **Typensicherheit**, ohne den Laufzeit-Overhead einer Wrapper-Struktur.

```zc
// In library.zc
opaque alias Handle = int;

fn erstelle_handle(v: int) -> Handle {
    return v; // Implizite Konvertierung innerhalb des Moduls erlaubt
}

// In main.zc
import "library.zc";

fn main() {
    let h: Handle = erstelle_handle(42);
    // let i: int = h; // Fehler: Typprüfung fehlgeschlagen
    // let h2: Handle = 10; // Fehler: Typprüfung fehlgeschlagen
}
```
