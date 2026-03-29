+++
title = "Gosper's hack"
+++

# Gosper's hack

```zc
fn gospers_hack(x: int) -> int {
    let c = x & -x;
    let r = x + c;
    return (((r ^ x) >> 2) / c) | r;
}

fn main() {
    let a = [1, 3, 7, 15];
    for start in a {
        print "{start:2d}:";
        let x = start;
        for i in 0..10 {
            x = gospers_hack(x);
            print " {x:4d}";
        }
        println "";
    }
}
```

**Output:**

```
1:    2    4    8   16   32   64  128  256  512 1024
 3:    5    6    9   10   12   17   18   20   24   33
 7:   11   13   14   19   21   22   25   26   28   35
15:   23   27   29   30   39   43   45   46   51   53
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Gosper's hack**](https://rosettacode.org/wiki/Gosper's_hack) in Zen C.

*This article uses material from the Rosetta Code article **Gosper's hack**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Gosper's_hack?action=history).*
