+++
title = "Sub-unit squares"
+++

# Sub-unit squares

{{trans|Wren}}

```zc
import "std/vec.zc"
import "std/math.zc"

fn digits<T>(n: T) -> Vec<int> {
    let digs = Vec<int>::new();
    if n == 0 {
        digs << 0;
        return digs;
    }
    while n > 0 {
        digs << (n % 10);
        n /= 10;
    }
    digs.reverse();
    return digs;
}

fn is_square<T>(n: T) -> bool {
    let sqrt = (T)Math::round(Math::sqrt((f64)n));
    return sqrt * sqrt == n;
}

fn main() {
    println "The first 7 sub-unit squares are:";
    println "1";
    let count = 1;
    for let i: u64 = 2; count < 7; i++ {
        let sq = i * i;
        let digs = digits(sq);
        if digs[0] != 1 && !digs.contains(0) {
            let sum: u64 = digs[0] - 1;
            for j in 1..digs.length() { sum = sum * 10 + digs[j] - 1; }
            if is_square(sum) {
                println "{sq]";
                count++;
            }
        }
    }
}
```

**Output:**

```
The first 7 sub-unit squares are:
1
36
3136
24336
5973136
71526293136
318723477136
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sub-unit squares**](https://rosettacode.org/wiki/Sub-unit_squares) in Zen C.

*This article uses material from the Rosetta Code article **Sub-unit squares**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sub-unit_squares?action=history).*
