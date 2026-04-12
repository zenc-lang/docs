+++
title = "Sort an integer array"
+++

# Sort an integer array

```zc
import "std/sort.zc"

fn main() {
    let a = [7, 2, 4, 9, 1, 3, 8, 6, 5];
    sort_int((int*)a, 9);
    for i in a { print "{i} " }
    println "";
}
```

**Output:**

```
1 2 3 4 5 6 7 8 9
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sort an integer array**](https://rosettacode.org/wiki/Sort_an_integer_array) in Zen C.

*This article uses material from the Rosetta Code article **Sort an integer array**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sort_an_integer_array?action=history).*
