+++
title = "Loops/Increment loop index within loop body"
+++

# Loops/Increment loop index within loop body

```zc
import "locale.h"

fn is_prime(n: u64) -> bool {
    if n < 2 { return false; }
    if n % 2 == 0 { return n == 2; }
    if n % 3 == 0 { return n == 3; }
    let d: u64 = 5;
    while d * d <= n {
        if n % d == 0 { return false; }
        d += 2;
        if n % d == 0 { return false; }
        d += 4;
    }
    return true;
}

fn main() {
    let count = 0;
    setlocale(LC_NUMERIC, "en_US.UTF-8");
    for let i: u64 = 42; count < 42; i++ {
    if is_prime(i) {
        count++;
        println "{count:2d}: {i:'18lu}";
        i = 2 * i - 1;
    }
}
```

**Output:**

```
1:                 43
 2:                 89
 3:                179
 4:                359
 5:                719
 6:              1,439
 7:              2,879
 8:              5,779
 9:             11,579
10:             23,159
11:             46,327
12:             92,657
13:            185,323
14:            370,661
15:            741,337
16:          1,482,707
17:          2,965,421
18:          5,930,887
19:         11,861,791
20:         23,723,597
21:         47,447,201
22:         94,894,427
23:        189,788,857
24:        379,577,741
25:        759,155,483
26:      1,518,310,967
27:      3,036,621,941
28:      6,073,243,889
29:     12,146,487,779
30:     24,292,975,649
31:     48,585,951,311
32:     97,171,902,629
33:    194,343,805,267
34:    388,687,610,539
35:    777,375,221,081
36:  1,554,750,442,183
37:  3,109,500,884,389
38:  6,219,001,768,781
39: 12,438,003,537,571
40: 24,876,007,075,181
41: 49,752,014,150,467
42: 99,504,028,301,131
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Loops/Increment loop index within loop body**](https://rosettacode.org/wiki/Loops/Increment_loop_index_within_loop_body) in Zen C.

*This article uses material from the Rosetta Code article **Loops/Increment loop index within loop body**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Loops/Increment_loop_index_within_loop_body?action=history).*
