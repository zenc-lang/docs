+++
title = "Approximate equality"
+++

# Approximate equality

```zc
import "std/math.zc"

fn main() {
    let tol = 1.0e-16;
    let sqrt2 = Math::sqrt(2.0);
    let pairs: (f64, f64)[8] = [
        (100000000000000.01, 100000000000000.011),
        (100.01, 100.011),
        (10000000000000.001 / 10000.0, 1000000000.0000001000),
        (0.001, 0.0010000001),
        (0.000000000000000000000101, 0.0),
        (sqrt2 * sqrt2, 2.0),
        (-sqrt2 * sqrt2, -2.0),
        (3.14159265358979323846, 3.14159265358979324)
    ];
    println "Approximate equality of test cases for a tolerance of {tol:g}:";
    for i in 0..pairs.len {
        let (p0, p1) = pairs[i];
        let res: bool = Math::abs(p0 - p1) < tol;
        println "  {i + 1} -> {res}";
    }
}
```

**Output:**

```
Approximate equality of test cases for a tolerance of 1e-16:
  1 -> true
  2 -> false
  3 -> false
  4 -> false
  5 -> true
  6 -> false
  7 -> false
  8 -> true
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Approximate equality**](https://rosettacode.org/wiki/Approximate_equality) in Zen C.

*This article uses material from the Rosetta Code article **Approximate equality**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Approximate_equality?action=history).*
