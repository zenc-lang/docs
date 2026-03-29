+++
title = "Averages/Root mean square"
+++

# Averages/Root mean square

```zc
import "std/math.zc"

fn rms(a: f64[], len: const int) -> f64 {
    let sum = 0.0;
    for i in 0..len { sum += a[i] * a[i]; }
    return Math::sqrt(sum / len);
}

fn main() {
    let a = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0];
    println "{rms(a, 10):0.16f}";
}
```

**Output:**

```
6.2048368229954285
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Averages/Root mean square**](https://rosettacode.org/wiki/Averages/Root_mean_square) in Zen C.

*This article uses material from the Rosetta Code article **Averages/Root mean square**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Averages/Root_mean_square?action=history).*
