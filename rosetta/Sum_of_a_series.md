+++
title = "Sum of a series"
+++

# Sum of a series

```zc
import "std/math.zc";

fn sum_series(n: int) -> f64 {
    let sum = 0.0;
    for i in 1..=n { sum += 1.0 / (f64)(i * i); }
    return sum;
}

fn main() {
    println "s(1000) = {sum_series(1000):0.16f}";
    let zeta2 = Math::PI() * Math::PI() / 6.0;
    println "zeta(2) = {zeta2:0.16f}";
}
```

**Output:**

```
s(1000) = 1.6439345666815615
zeta(2) = 1.6449340668482264
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sum of a series**](https://rosettacode.org/wiki/Sum_of_a_series) in Zen C.

*This article uses material from the Rosetta Code article **Sum of a series**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sum_of_a_series?action=history).*
