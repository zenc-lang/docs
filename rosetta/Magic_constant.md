+++
title = "Magic constant"
+++

# Magic constant

```zc
//> link: -lm

import "locale.h"
import "std/math.zc"
import "math.h" as c_math // for cbrt function

fn magic_constant(n: u64) -> u64 {
    return (n * n + 1) * n / 2;
}

fn main() {
    "First 20 magic constants:";
    for i in 3..=22 {
        let mc = magic_constant((u64)i);
        print "{mc:5ld}";
        if i == 12 || i == 22 { println ""; }
    }

    setlocale(LC_NUMERIC, "en_US.UTF-8");
    println "\n1,000th magic constant: {magic_constant(1002):'lu}";

    println "\nSmallest order magic square with a constant greater than:";
    for i in 1..=20 {
        let goal = Math::pow(10.0, i);
        let order = (u64)(Math::floor(c_math::cbrt(goal * 2.0))) + 1;
        println "10 ^ {i:2d} : {order:'9lu}";
    }
}
```

**Output:**

```
First 20 magic constants:
   15   34   65  111  175  260  369  505  671  870
 1105 1379 1695 2056 2465 2925 3439 4010 4641 5335

1,000th magic constant: 503,006,505

Smallest order magic square with a constant greater than:
10 ^  1 :         3
10 ^  2 :         6
10 ^  3 :        13
10 ^  4 :        28
10 ^  5 :        59
10 ^  6 :       126
10 ^  7 :       272
10 ^  8 :       585
10 ^  9 :     1,260
10 ^ 10 :     2,715
10 ^ 11 :     5,849
10 ^ 12 :    12,600
10 ^ 13 :    27,145
10 ^ 14 :    58,481
10 ^ 15 :   125,993
10 ^ 16 :   271,442
10 ^ 17 :   584,804
10 ^ 18 : 1,259,922
10 ^ 19 : 2,714,418
10 ^ 20 : 5,848,036
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Magic constant**](https://rosettacode.org/wiki/Magic_constant) in Zen C.

*This article uses material from the Rosetta Code article **Magic constant**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Magic_constant?action=history).*
