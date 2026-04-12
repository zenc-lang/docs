+++
title = "Gapful numbers"
+++

# Gapful numbers

{{trans|Go}}

```zc
import "locale.h"

fn main() {
    setlocale(LC_NUMERIC, "en_US.UTF-8");
    let starts: u64[5] = [100, 1_000_000, 10_000_000, 1_000_000_000, 7123];
    let totals: int[5] = [30, 15, 15, 10, 25];
    for i in 0..5 {
        let count = 0;
        let j = starts[i];
        let pow: u64 = 100;
        loop {
            if j < pow * 10 { break; }
            pow *= 10;
        }
        println "First {totals[i]} gapful numbers starting at {starts[i]:'lu}";
        while totals[i] > count {    
            let fl = j / pow * 10 + (j % 10);
            if !(j % fl) {
                print "{j} ";
                count++;
            }
            if ++j >= 10 * pow { pow *= 10; }
        }
        println "\n";
    }
}
```

**Output:**

```
First 30 gapful numbers starting at 100
100 105 108 110 120 121 130 132 135 140 143 150 154 160 165 170 176 180 187 190 192 195 198 200 220 225 231 240 242 253 

First 15 gapful numbers starting at 1,000,000
1000000 1000005 1000008 1000010 1000016 1000020 1000021 1000030 1000032 1000034 1000035 1000040 1000050 1000060 1000065 

First 15 gapful numbers starting at 10,000,000
10000000 10000001 10000003 10000004 10000005 10000008 10000010 10000016 10000020 10000030 10000032 10000035 10000040 10000050 10000060 

First 10 gapful numbers starting at 1,000,000,000
1000000000 1000000001 1000000005 1000000008 1000000010 1000000016 1000000020 1000000027 1000000030 1000000032 

First 25 gapful numbers starting at 7,123
7125 7140 7171 7189 7210 7272 7275 7280 7296 7350 7373 7420 7425 7474 7488 7490 7560 7575 7630 7632 7676 7700 7725 7770 7777
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Gapful numbers**](https://rosettacode.org/wiki/Gapful_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Gapful numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Gapful_numbers?action=history).*
