+++
title = "Function definition"
+++

# Function definition

Zen C functions are defined using the <code>fn</code> keyword, with the return type indicated by an arrow <code>-></code>. While standard C preprocessor macros are supported via <code>#define</code>, their use is generally discouraged in favor of Zen C's native <code>def</code> keyword for manifest constants or <code>comptime</code> blocks for metaprogramming.

Instead of an <code>inline</code> keyword, Zen C uses an attribute system to modify compiler behavior. You can hint the compiler to inline a function using the <code>@inline</code> attribute (or prevent it with <code>@noinline</code>). An inline version of a multiplication function looks like this:

```zc
@inline
fn multiply(a: f64, b: f64) -> f64 {
    return a * b;
}
```

If the function needs to handle arbitrary types (similar to C++ templates), Zen C provides Generics. This allows for type-safe templates for functions:

```zc
fn multiply_generic<T>(a: T, b: T) -> T {
    return a * b;
}
```

Here is a complete example demonstrating a standard function with default arguments, an inline function, and a generic function:

```zc
// Standard function with a default argument
fn increment(val: int, amount: int = 1) -> int {
    return val + amount;
}

// Inline function attribute hint
@inline
fn multiply(a: float, b: float) -> float {
    return a * b;
}

// Generic function
fn multiply_generic<T>(a: T, b: T) -> T {
    return a * b;
}

fn main() {
    // Default argument evaluated
    let res1 = increment(10);
    println "10 + default = {res1}";

    // Inline execution
    let res2 = multiply(5.0, 4.0);
    println "5.0 * 4.0 = {res2}";

    // Generic execution with f32 (float)
    let res3 = multiply_generic<f32>(2.5, 2.0);
    println "2.5 * 2.0 = {res3}";
    
    // Generic execution with int
    let res4 = multiply_generic<int>(10, 3);
    println "10 * 3 = {res4}";
}
```

**Output:**

```
10 + default = 11
5.0 * 4.0 = 20.000000
2.5 * 2.0 = 5.000000
10 * 3 = 30
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Function definition**](https://rosettacode.org/wiki/Function_definition) in Zen C.

*This article uses material from the Rosetta Code article **Function definition**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Function_definition?action=history).*
