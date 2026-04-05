+++
title = "Loops/Break"
+++

# Loops/Break

```zc
import "std/random.zc"

fn main() {
    let rng = Random::new();
    loop {
        let a = rng.next_int_range(0, 19);
        println "{a}";
        if a == 10 { break; }
        let b = rng.next_int_range(0, 19);
        println "{b}";
    }
}
```

**Output:**

Short sample run:

```
2
5
8
16
4
0
14
2
19
18
16
18
12
14
10
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Loops/Break**](https://rosettacode.org/wiki/Loops/Break) in Zen C.

*This article uses material from the Rosetta Code article **Loops/Break**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Loops/Break?action=history).*
