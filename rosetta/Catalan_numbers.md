+++
title = "Catalan numbers"
+++

# Catalan numbers

```zc
import "locale.h"

fn factorial(n: u64) -> u64 {
    let prod: u64 = 1;
    for i in 2..=n { prod *= i; }
    return prod;
}

fn catalan(n: u64) -> u64 {
    let prod: u64 = 1;
    let i = n + 2;
    while i <= n * 2 { prod *= i++; }
    return prod / factorial(n);
}

fn catalan_rec(n: u64) -> u64 {
    return (n != 0) ? 2 * (2 * n - 1) * catalan_rec(n - 1) / (n + 1) : 1;
}

fn main() {
    setlocale(LC_NUMERIC, "en_US.UTF-8");
    println " n  Catalan number";
    println "------------------";
    for i in 0..=15 { printf("%2d  %'9llu\n", i, catalan((u64)i)); }
    println "\nand again using a recursive function:\n";
    for i in 0..=15 { printf("%2d  %'9llu\n", i, catalan_rec((u64)i)); }
}
```

**Output:**

```
n  Catalan number
------------------
 0          1
 1          1
 2          2
 3          5
 4         14
 5         42
 6        132
 7        429
 8      1,430
 9      4,862
10     16,796
11     58,786
12    208,012
13    742,900
14  2,674,440
15  9,694,845

and again using a recursive function:

 0          1
 1          1
 2          2
 3          5
 4         14
 5         42
 6        132
 7        429
 8      1,430
 9      4,862
10     16,796
11     58,786
12    208,012
13    742,900
14  2,674,440
15  9,694,845
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Catalan numbers**](https://rosettacode.org/wiki/Catalan_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Catalan numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Catalan_numbers?action=history).*
