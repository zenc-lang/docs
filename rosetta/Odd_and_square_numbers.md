+++
title = "Odd and square numbers"
+++

# Odd and square numbers

```zc
import "std/math.zc"

fn is_square(n: int) -> bool {
    let sqrt = (int)Math::round(Math::sqrt((f64)n));
    return sqrt * sqrt == n;
}

fn main() {
    for i in 101..1000 step 2 {
        if is_square(i) { print "{i} "; }
    }
    println "";
}
```

**Output:**

```
121 169 225 289 361 441 529 625 729 841 961
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Odd and square numbers**](https://rosettacode.org/wiki/Odd_and_square_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Odd and square numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Odd_and_square_numbers?action=history).*
