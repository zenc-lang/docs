+++
title = "Accumulator factory"
+++

# Accumulator factory

```zc
fn accumulator<T>(acc: T) -> fn(T) -> T {
    return fn(f: T) -> T {
        acc += f;
        return acc;
    }
}

fn main() {
    // Example with f64s.
    let x = accumulator(1.0);
    x(5.0);
    accumulator(3.0);
    println "{x(2.3):g}";

    // Example with ints.
    let y = accumulator(1);
    y(5);
    accumulator(3);
    println "{y(2)}";
}
```

**Output:**

```
8.3
8
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Accumulator factory**](https://rosettacode.org/wiki/Accumulator_factory) in Zen C.

*This article uses material from the Rosetta Code article **Accumulator factory**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Accumulator_factory?action=history).*
