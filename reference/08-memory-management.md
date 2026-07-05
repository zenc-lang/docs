+++
title = "8. Memory Management"
weight = 8
+++

# 8. Memory Management


Zen C allows manual memory management with ergonomic aids.

#### Defer
Execute code when the current scope exits. Defer statements are executed in LIFO (last-in, first-out) order.
```zc
let f = fopen("file.txt", "r");
defer fclose(f);
```

{% alert(type="warning") %}
To prevent undefined behavior, control flow statements (`return`, `break`, `continue`, `goto`) are **not allowed** inside a `defer` block.
{% end %}

#### Autofree
Automatically free the variable when scope exits.
```zc
autofree let types = malloc(1024);
```

#### Resource Semantics (Move by Default)
Zen C treats types with destructors (like `File`, `Vec`, or malloc'd pointers) as **Resources**. To prevent double-free errors, resources cannot be implicitly duplicated.

- **Move by Default**: Assigning a resource variable transfers ownership. The original variable becomes invalid (Moved).
- **Copy Types**: Types without destructors may opt-in to `Copy` behavior, making assignment a duplication.

**Diagnostics & Philosophy**:
If you see an error "Use of moved value", the compiler is telling you: *"This type owns a resource (like memory or a handle) and blindly copying it is unsafe."*

{% alert(type="note") %}
**Contrast:** Unlike C/C++, Zen C does not implicitly duplicate resource-owning values.
{% end %}

**Function Arguments**:
Passing a value to a function follows the same rules as assignment: resources are moved unless passed by reference.

```zc
fn process(r: Resource) { ... } // 'r' is moved into function
fn peek(r: Resource*) { ... }   // 'r' is borrowed (reference)
```

**Explicit Cloning**:
If you *do* want two copies of a resource, make it explicit:

```zc
let b = a.clone(); // Calls the 'clone' method from the Clone trait
```

**Opt-in Copy (Value Types)**:
For small types without destructors:

```zc
struct Point { x: int; y: int; }
impl Copy for Point {} // Opt-in to implicit duplication

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = p1; // Copied. p1 stays valid.
}
```

#### RAII / Drop Trait
Implement `Drop` to run cleanup logic automatically.
```zc
impl Drop for MyStruct {
    fn drop(self) {
        self.free();
    }
}
```
