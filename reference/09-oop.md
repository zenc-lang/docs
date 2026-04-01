+++
title = "9. Object Oriented Programming"
weight = 9
+++

# 9. Object Oriented Programming


#### Methods
Define methods on types using `impl`.
```zc
impl Point {
    // Static method (constructor convention)
    fn new(x: int, y: int) -> Self {
        return Point{x: x, y: y};
    }

    // Instance method
    fn dist(self) -> float {
        return sqrt(self.x * self.x + self.y * self.y);
    }
}
```

**Self Shorthand**: In methods with a `self` parameter, you can use `.field` as shorthand for `self.field`:
```zc
impl Point {
    fn dist(self) -> float {
        return sqrt(.x * .x + .y * .y);  // Equivalent to self.x, self.y
    }
}
```

#### Primitive Methods
Zen C allows you to define methods on primitive types (like `int`, `bool`, etc.) using the same `impl` syntax.

```zc
impl int {
    fn abs(self) -> int {
        return *self < 0 ? -(*self) : *self;
    }
}

let x = -10;
let y = x.abs(); // 10
let z = (-5).abs(); // 5 (Literals supported)
```

#### Traits
Define shared behavior.
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

#### Standard Traits
Zen C includes standard traits that integrate with language syntax.

**Iterable**

Implement `Iterable<T>` to enable `for-in` loops for your custom types.

```zc
import "std/iter.zc"

// Define an Iterator
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

// Implement Iterable
impl MyRange {
    fn iterator(self) -> MyIter {
        return MyIter{curr: self.start, stop: self.end};
    }
}

// Use in Loop
for i in my_range {
    println "{i}";
}
```

**Drop**

Implement `Drop` to define a destructor that runs when the object goes out of scope (RAII).

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
**Note:** If a variable is moved, `drop` is NOT called on the original variable. It adheres to [Resource Semantics](@/tour/08-memory-management.md#resource-semantics-move-by-default).
{% end %}

**Copy**

Marker trait to opt-in to `Copy` behavior (implicit duplication) instead of Move semantics. Used via `@derive(Copy)`.

{% alert(type="caution") %}
**Rule:** Types that implement `Copy` must not define a destructor (`Drop`).
{% end %}

```zc
@derive(Copy)
struct Point { x: int; y: int; }

fn main() {
    let p1 = Point{x: 1, y: 2};
    let p2 = p1; // Copied! p1 remains valid.
}
```

**Clone**

Implement `Clone` to allow explicit duplication of resource-owning types.

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
    let b2 = b1.clone(); // Explicit copy
}
```

#### Composition
Use `use` to embed other structs. You can either mix them in (flatten fields) or name them (nest fields).

```zc
struct Entity { id: int; }

struct Player {
    // Mixin (Unnamed): Flattens fields
    use Entity;  // Adds 'id' to Player directly
    name: string;
}

struct Match {
    // Composition (Named): Nests fields
    use p1: Player; // Accessed via match.p1
    use p2: Player; // Accessed via match.p2
}
```
