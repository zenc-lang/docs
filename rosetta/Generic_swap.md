+++
title = "Generic swap"
+++

# Generic swap

Zen C has a generic swap function in its *std/mem* module. The variables whose values are to be swapped must be of the same type.

```zc
import "std/mem.zc"

fn main() {
    let a = 1;
    let b = 2;
    println "Before: a = {a}, b = {b}";
    swap(&a, &b);
    println "After : a = {a}, b = {b}";
    println "";
    let s = "Rosetta";
    let t = "Code";
    println "Before: s = {s}, t = {t}";
    swap(&s, &t);
    println "After : s = {s}, t = {t}";
}
```

**Output:**

```
Before: a = 1, b = 2
After : a = 2, b = 1

Before: s = Rosetta, t = Code
After : s = Code, t = Rosetta
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Generic swap**](https://rosettacode.org/wiki/Generic_swap) in Zen C.

*This article uses material from the Rosetta Code article **Generic swap**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Generic_swap?action=history).*
