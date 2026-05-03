+++
title = "Population count"
+++

# Population count

{{trans|Wren}}

```zc
import "std/vec.zc"

fn pop_count<T>(n: T) -> int {
    let count = 0;
    while n {
        n = n & (n - 1);
        count++;
    }
    return count;
}

fn main() {
    println "The population count of the first 30 powers of 3 is:";
    let p3: u64 = 1;
    for i in 0..30 {
        print "{pop_count<u64>(p3)} ";
        p3 *= 3;
    }
    let odious = Vec<int>::new();
    println "\n\nThe first 30 evil numbers are:";
    let count = 0;
    let n = 0
    for ; count < 30; ++n {
        let pc = pop_count<int>(n);
        if !(pc % 2) {
            print "{n} ";
            count++;
        } else {
            odious << n;
        }
    }
    odious << n;
    println "\n\nThe first 30 odious numbers are:";
    for o in odious { print "{o} "; }
    println "";
}
```

**Output:**

```
The population count of the first 30 powers of 3 is:
1 2 2 4 3 6 6 5 6 8 9 13 10 11 14 15 11 14 14 17 17 20 19 22 16 18 24 30 25 25 

The first 30 evil numbers are:
0 3 5 6 9 10 12 15 17 18 20 23 24 27 29 30 33 34 36 39 40 43 45 46 48 51 53 54 57 58 

The first 30 odious numbers are:
1 2 4 7 8 11 13 14 16 19 21 22 25 26 28 31 32 35 37 38 41 42 44 47 49 50 52 55 56 59
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Population count**](https://rosettacode.org/wiki/Population_count) in Zen C.

*This article uses material from the Rosetta Code article **Population count**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Population_count?action=history).*
