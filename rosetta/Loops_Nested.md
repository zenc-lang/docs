+++
title = "Loops/Nested"
+++

# Loops/Nested

```zc
import "std/random.zc"

fn main() {
    let rng = Random::new();
    let a: int[20][20];
    for i in 0..=19 {
        for j in 0..=19 {
            a[i][j] = rng.next_int_range(1, 20);
        }
    }

    outer: for i in 0..=19 {
        for j in 0..=19 {
            print "{a[i][j]:2d} ";
            if a[i][j] == 20 {
                println "";
                break outer;
            }
            if (j + 1) % 10 == 0 { println ""; }
        }
    }
}
```

**Output:**

Sample output:

```
13  5  6  3 19 18 11  5  5 19 
 5 14 19 15 15  9 18 16 12  2 
13 17 17  1  7 19  4  4 12 14 
 9  4 18  6  6 16  3  9  1 19 
 7  5  4 18 11 18  6 20
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Loops/Nested**](https://rosettacode.org/wiki/Loops/Nested) in Zen C.

*This article uses material from the Rosetta Code article **Loops/Nested**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Loops/Nested?action=history).*
