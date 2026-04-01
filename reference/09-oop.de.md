+++
title = "9. Objektorientierte Programmierung (OOP)"
weight = 9
+++

# 9. Objektorientierte Programmierung (OOP)


#### Methoden
Methoden auf Typen mit `impl` definieren.
```zc
impl Point {
    // Statische Methode (Konstruktor-Konvention)
    fn new(x: int, y: int) -> Self {
        return Point{x: x, y: y};
    }

    // Instanzmethode
    fn dist(self) -> float {
        return sqrt(self.x * self.x + self.y * self.y);
    }
}
```

**Self-Kurzschreibweise**: In Methoden mit `self` kann `.feld` als Kurzform für `self.feld` verwendet werden:
```zc
impl Point {
    fn dist(self) -> float {
        return sqrt(.x * .x + .y * .y);  // Entspricht self.x, self.y
    }
}
```

#### Primitive Methoden
Zen C erlaubt es dir, Methoden für primitive Datentypen (wie `int`, `bool` usw.) mit der gleichen `impl`-Syntax zu definieren.

```zc
impl int {
    fn abs(self) -> int {
        return *self < 0 ? -(*self) : *self;
    }
}

let x = -10;
let y = x.abs();    // 10
let z = (-5).abs(); // 5 (Literals unterstützt)
```

#### Traits
Definieren gemeinsames Verhalten.
```zc
struct Circle { radius: f32; }

trait Drawable {
    fn draw(self);
}

impl Drawable for Circle {
    fn draw(self) { ... }
}

let circle = Circle{};
let drawable: Drawable = &circle;
```

#### Standard-Traits
Zen C beinhaltet Standardmerkmale, die sich in die Sprachsyntax integrieren.

**Iterable**  

Implementiere `Iterable<T>`, um `for-in`-Schleifen für eigene Typen zu ermöglichen.

```zc
import "std/iter.zc"

// Iterator definieren
struct MyIter {
    curr: int;
    stop: int;
}

impl MyIter {
    fn next(self) -> Option<int> {
        if self.curr < self.stop {
            self.curr += 1;
            return Option<int>::Some(self.curr - 1);
        }
        return Option<int>::None();
    }
}

// Iterable implementieren
impl MyRange {
    fn iterator(self) -> MyIter {
        return MyIter{curr: self.start, stop: self.end};
    }
}

// Nutzung in Schleife
for i in my_range {
    println "{i}";
}
```

**Drop**  

Implementiere `Drop`, um einen Destruktor zu definieren, der ausgeführt wird, wenn das Objekt seinen Gültigkeitsbereich verlässt (RAII).

```zc
import "std/mem.zc"

struct Resource {
    ptr: void*;
}

impl Drop for Resource {
    fn drop(self) {
        if self.ptr != NULL {
            free(self.ptr);
        }
    }
}
```

{% alert(type="important") %}
**Anmerkung:** Wenn eine Variable verschoben wird, wird `drop` NICHT für die ursprüngliche Variable aufgerufen. Dies folgt der [Ressourcen-Semantik](@/tour/08-memory-management.de.md#ressourcen-semantik-move-by-default).
{% end %}

**Copy**  

Marker-Trait zur Aktivierung des `Copy`-Verhaltens (implizite Duplizierung) anstelle der Move-Semantik. Verwendung über `@derive(Copy)`.

{% alert(type="caution") %}
**Regel:** Typen, die `Copy` implementieren, dürfen keinen Destruktor (`Drop`) definieren.
{% end %}

```zc
@derive(Copy)
struct Point { x: int; y: int; }

fn main() {
    let p1 = Point{x: 1, y: 2};
    let p2 = p1; // Kopiert! p1 bleibt gültig
}
```

**Clone**  

Implementiert `Clone` für explizites Duplizieren von Ressourcen-Typen.

```zc
import "std/mem.zc"

struct MyBox { val: int; }

impl Clone for MyBox {
    fn clone(self) -> MyBox {
        return MyBox{val: self.val};
    }
}

fn main() {
    let b1 = MyBox{val: 42};
    let b2 = b1.clone(); // Explizite Kopie
}
```

#### Komposition
Verwende `use`, um andere Strukturen einzubetten. Du kannst diese entweder direkt einbetten (Felder vereinfachen) oder ihnen Namen geben (Felder verschachteln).

```zc
struct Entity { id: int; }

struct Player {
	// Mixin (unbenannt): Glättet Felder
    use Entity;  // Fügt 'id' direkt hinzu
    name: string;
}

struct Match {
    // Komposition (benannt): Verschachtelte Felder
    use p1: Player; // Zugriff über match.p1
    use p2: Player; // Zugriff über match.p2
}
```
