+++
title = "Sum of primes in odd positions is prime"
+++

# Sum of primes in odd positions is prime

```zc
import "locale.h"

fn is_prime(n: int) -> bool {
    if n < 2      { return false; }
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
    setlocale(LC_NUMERIC, "");
    let sum = 0;
    let i = 1;
    println " i   p[i]  Σp[i]";
    println "----------------";
    let p = 2;
    while p < 1000 {
        if is_prime(p) {
            if i % 2 {
                sum += p;
                if is_prime(sum) {
                    printf("%3d  %3d  %'6d\n", i , p, sum);
                }
            }
            i++;
        }
        p = p > 2 ? p + 2 : p + 1;
    }
}
```

**Output:**

```
i   p[i]  Σp[i]
----------------
  1    2       2
  3    5       7
 11   31      89
 27  103     659
 35  149   1,181
 67  331   5,021
 91  467   9,923
 95  499  10,909
 99  523  11,941
119  653  17,959
143  823  26,879
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sum of primes in odd positions is prime**](https://rosettacode.org/wiki/Sum_of_primes_in_odd_positions_is_prime) in Zen C.

*This article uses material from the Rosetta Code article **Sum of primes in odd positions is prime**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sum_of_primes_in_odd_positions_is_prime?action=history).*
