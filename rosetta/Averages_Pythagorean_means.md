+++
title = "Averages/Pythagorean means"
+++

# Averages/Pythagorean means

```zc
import "std/math.zc"

fn a_mean(a: f64*, len: const usize) -> f64 {
    let sum = 0.0;
    for i in 0..len { sum += a[i]; }
    return sum / (f64)len;
}

fn g_mean(a: f64*, len: const usize) -> f64 {
    let prod = 1.0;
    for i in 0..len { prod *= a[i]; }
    return Math::pow(prod, 1.0 / (f64)len);
}

fn h_mean(a: f64*, len: const usize) -> f64 {
    let sum = 0.0;
    for i in 0..len { sum += 1.0 / a[i]; }
    return 1.0 / sum * (f64)len;
}

fn main() {
    let a: f64[10];
    for i in 0..10 { a[i] = (f64)(i + 1); }
    let am = a_mean(a, 10);
    let gm = g_mean(a, 10);
    let hm = h_mean(a, 10);
    let cmp = (am >= gm && gm >= hm) ? "true" : "false";
    println "For the numbers 1 to 10:";
    println "  Arithmetic mean = {am:g}";
    println "  Geometric mean  = {gm:0.14f}";
    println "  Harmonic mean   = {hm:0.14f}";
    println "  A >= G >= H     = {cmp}";
}
```

**Output:**

```
For the numbers 1 to 10:
  Arithmetic mean = 5.5
  Geometric mean  = 4.52872868811677
  Harmonic mean   = 3.41417152147406
  A >= G >= H     = true
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Averages/Pythagorean means**](https://rosettacode.org/wiki/Averages/Pythagorean_means) in Zen C.

*This article uses material from the Rosetta Code article **Averages/Pythagorean means**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Averages/Pythagorean_means?action=history).*
