+++
title = "3. Aggregate Types"
weight = 3
+++

# 3. Aggregate Types


#### Arrays
Fixed-size arrays with value semantics.
```zc
def SIZE = 5;
let ints: int[SIZE] = [1, 2, 3, 4, 5];
let zeros: [int; SIZE]; // Zero-initialized
```

#### Tuples

Group multiple values together into a single compound value. Tuples support
arbitrary arities (2, 3, 4, … up to 10+), nested composition, mutation of
individual fields, and destructuring.

**Basic usage**

```zc
let pair = (1, "hello");          // 2-tuple, types inferred
let triple = (1, "hello", 3.14);  // 3-tuple
let five = (1, 2, 3, 4, 5);      // 5-tuple
let typed: (int, string, f64) = (1, "two", 3.0);  // explicit annotation
```

**Field access**

Elements are accessed positionally with `.0`, `.1`, `.2` etc., or via
raw struct field names `.v0`, `.v1`:

```zc
let t = (1, "hello", 3.14);
assert(t.0 == 1);       // positional
assert(t.v1 == "hello"); // raw field name
```

**Multiple return values**

Functions can return tuples to provide multiple results:

```zc
fn stats(data: int) -> (int, int) {
    return (data * 2, data + 1);
}

let r = stats(5);
assert(r.0 == 10);
assert(r.1 == 6);
```

**Destructuring**

```zc
let (sum, diff) = add_and_subtract(3, 2);
// sum = 5, diff = 1

let (a: string, b: u8) = ("hello", 42);  // typed destructuring
let (x, y: i32) = (1, 2);                // mixed: x inferred, y explicit
```

**Nested tuples**

```zc
let nested = ((1, 2), (3, 4));
let inner = nested.v0;
assert(inner.v0 == 1);
assert(inner.v1 == 2);
```

**Mutation**

Individual fields can be reassigned:

```zc
let t = (1, 2);
t.v0 = 99;
assert(t.v0 == 99);
```

**String comparison**

Tuples with `string` fields must use `strcmp()` for comparison,
not `==` (which does pointer comparison on `char*`):

```zc
let t = (1, "hello");
assert(strcmp(t.1, "hello") == 0);
```

**Enum tuple payloads**

Enum variants can carry tuple data:

```zc
enum Shape {
    Point,
    Line(int, int),
    Labeled(int, string, f64),
}

match shape {
    Shape::Line(x, y) => { … }
    Shape::Labeled(id, name, val) => { … }
}
```

#### Structs
Data structures with optional bitfields.
```zc
struct Point {
    x: int;
    y: int;
}

// Struct initialization
let p = Point { x: 10, y: 20 };

// Bitfields
struct Flags {
    valid: U8 : 1;
    mode:  U8 : 3;
}
```

{% alert(type="note") %}
Structs use [Move Semantics](@/tour/08-memory-management.md#resource-semantics-move-by-default) by default. Fields can be accessed via `.` even on pointers (Auto-Dereference).
{% end %}

#### Opaque Structs
You can define a struct as `opaque` to restrict access to its fields to the defining module only, while still allowing the struct to be allocated on the stack (size is known).

```zc
// In user.zc
opaque struct User {
    id: int;
    name: string;
}

fn new_user(name: string) -> User {
    return User{id: 1, name: name}; // OK: Inside module
}

// In main.zc
import "user.zc";

fn main() {
    let u = new_user("Alice");
    // let id = u.id; // Error: Cannot access private field 'id'
}
```

#### Enums
Tagged unions (Sum types) capable of holding data.
```zc
enum Shape {
    Circle(float),      // Holds radius
    Rect(float, float), // Holds width, height
    Point               // No data
}
```

#### Unions
Standard C unions (unsafe access).
```zc
union Data {
    i: int;
    f: float;
}
```

#### SIMD Vectors
Native SIMD vector types using GCC/Clang vector extensions. Annotate a struct with `@vector(N)` to define a vector of N elements.
```zc
import "std/simd.zc";

fn main() {
    let a = f32x4{v: 1.0};              // Broadcast: {1.0, 1.0, 1.0, 1.0}
    let b = f32x4{1.0, 2.0, 3.0, 4.0};  // Per-element init
    let c = a + b;                       // Element-wise addition
    let x = c[0];                        // Element access (float)
}
```
Arithmetic (`+`, `-`, `*`, `/`) and bitwise (`&`, `|`, `^`) operators work element-wise. See [`std/simd.zc`](std/simd.zc) for predefined types.

#### Type Aliases
Create a new name for an existing type.
```zc
alias ID = int;
alias PointMap = Map<string, Point>
alias OpFunc = fn(int, int) -> int
```

#### Opaque Type Aliases
You can define a type alias as `opaque` to create a new type that is distinct from its underlying type outside of the defining module. This provides strong encapsulation and type safety without the runtime overhead of a wrapper struct.

```zc
// In library.zc
opaque alias Handle = int;

fn make_handle(v: int) -> Handle {
    return v; // Implicit conversion allowed inside module
}

// In main.zc
import "library.zc";

fn main() {
    let h: Handle = make_handle(42);
    // let i: int = h; // Error: Type validation failed
    // let h2: Handle = 10; // Error: Type validation failed
}
```
