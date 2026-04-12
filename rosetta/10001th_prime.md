+++
title = "10001th prime"
+++

# 10001th prime

```zc
import "locale.h"

fn is_prime(n: int) -> bool {
    if n < 2 { return false; }
    if n % 2 == 0 { return n == 2; }
    if n % 3 == 0 { return n == 3; }
    let d = 5;
    while d * d <= n {
        if n % d == 0 { return false; }
        d += 2;
        if n % d == 0 { return false; }
        d += 4;
    }
    return true;
}

fn main() {
    setlocale(LC_NUMERIC, "en_US.UTF-8");
    print "The 10,001th prime is ";
    let count = 1;
    let i = 3;
    loop {
        if is_prime(i) {
            if ++count == 10_001 {
                println "{i:'d}.";
                break;
            }
        }
        i += 2;
    }
}
```

**Output:**

```
The 10,001th prime is 104,743.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**10001th prime**](https://rosettacode.org/wiki/10001th_prime) in Zen C.

*This article uses material from the Rosetta Code article **10001th prime**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/10001th_prime?action=history).*
