+++
title = "Arithmetic-geometric mean"
+++

# Arithmetic-geometric mean

{{trans|Go}}

```zc
import "std/math.zc"

fn agm(a: f64, g: f64) -> f64 {
    let eps: const f64 = 1e-14;
    while Math::abs(a - g) > Math::abs(a) * eps {
        let t = a;
        a = (a + g) / 2.0;
        g = Math::sqrt(t * g);
    }
    return a;
}

fn main() {
    let a = agm(1.0, 1.0 / Math::sqrt(2.0));
    println "{a:0.16f}";
}
```

**Output:**

```
0.8472130847939792
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Arithmetic-geometric mean**](https://rosettacode.org/wiki/Arithmetic-geometric_mean) in Zen C.

*This article uses material from the Rosetta Code article **Arithmetic-geometric mean**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Arithmetic-geometric_mean?action=history).*
