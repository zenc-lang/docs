+++
title = "Digit fifth powers"
+++

# Digit fifth powers

{{trans|Wren}}

```zc
import "std/vec.zc"

fn digits(n: int) -> Vec<int> {
    let digs = Vec<int>::new();
    if n == 0 {
        digs << 0;
        return digs;
    }
    while n > 0 {
        digs << (n % 10);
        n /= 10;
    }
    return digs; // order unimportant here
}

fn main() {
    // cache 5th power of digits
    let dp5: [int; 10];
    for i in 0..10 { dp5[i] = i ** 5; }

    println "The sum of all numbers that can be written as the sum of the 5th powers of their digits is:";
    let limit = dp5[9] * 6;
    let sum = 0;
    for i in 2..=limit {
        let digs = digits(i);
        let total_dp = 0;
        for j in 0..digs.length() { total_dp += dp5[digs[j]]; }
        if total_dp == i {
            if sum > 0 { print " + {i}"; } else { print "{i}" };
            sum += i;
        }
    }
    println " = {sum}";
}
```

**Output:**

```
The sum of all numbers that can be written as the sum of the 5th powers of their digits is:
4150 + 4151 + 54748 + 92727 + 93084 + 194979 = 443839
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Digit fifth powers**](https://rosettacode.org/wiki/Digit_fifth_powers) in Zen C.

*This article uses material from the Rosetta Code article **Digit fifth powers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Digit_fifth_powers?action=history).*
