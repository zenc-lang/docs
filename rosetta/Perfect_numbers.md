+++
title = "Perfect numbers"
+++

# Perfect numbers

```zc
import "std/math.zc"

fn is_perfect(n: int) -> bool {
    if n <= 2 { return false; }
    let tot = 1;
    for i in 2..=Math::floor(Math::sqrt((f64)n)) {
        if n % i == 0 {
            tot += i;
            let q = n / i;
            if q > i { tot += q; }
        }
    }
    return n == tot;
}

fn main() {
    println "The first four perfect numbers are:";
    let count = 0;
    let i = 2;
    while count < 4 {
        if is_perfect(i) {
            println "{i} ";
            count++;
        }
        i += 2;  // there are no known odd perfect numbers
    }
}
```

**Output:**

```
The first four perfect numbers are:
6
28
496
8128
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Perfect numbers**](https://rosettacode.org/wiki/Perfect_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Perfect numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Perfect_numbers?action=history).*
