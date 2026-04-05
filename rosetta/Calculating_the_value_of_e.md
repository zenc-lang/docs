+++
title = "Calculating the value of e"
+++

# Calculating the value of e

```zc
import "std/math.zc"

fn main() {
    def EPS = 1e-15;
    let e = 2.0;
    let fact: u64 = 1;
    let n: u64 = 2;
    loop {
        let e0 = e;
        fact *= n++;
        e += 1.0 / (f64)fact;
        if Math::abs(e - e0) < EPS { break; }
    }
    println "e = {e:0.15f}";
}
```

**Output:**

```
e = 2.718281828459046
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Calculating the value of e**](https://rosettacode.org/wiki/Calculating_the_value_of_e) in Zen C.

*This article uses material from the Rosetta Code article **Calculating the value of e**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Calculating_the_value_of_e?action=history).*
