+++
title = "Forward difference"
+++

# Forward difference

```zc
fn forward_diff(a: int*, ac: int, order: const uint) {
    if ac == 0 || order == 0 { return; }
    for o in 0..=order {
        print "{o:2u}: ";
        for i in 0..ac {
            print "{a[i]:5d} ";
            if i == ac - 1 { break; }
            a[i] = a[i + 1] - a[i];
        }
        println "";
        if !(--ac) { return; }
    }
}

fn main() {
    let a = [90, 47, 58, 29, 22, 32, 55, 5, 55, 73];
    forward_diff(a, 10, 9);
}
```

**Output:**

```
0:    90    47    58    29    22    32    55     5    55    73 
 1:   -43    11   -29    -7    10    23   -50    50    18 
 2:    54   -40    22    17    13   -73   100   -32 
 3:   -94    62    -5    -4   -86   173  -132 
 4:   156   -67     1   -82   259  -305 
 5:  -223    68   -83   341  -564 
 6:   291  -151   424  -905 
 7:  -442   575 -1329 
 8:  1017 -1904 
 9: -2921
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Forward difference**](https://rosettacode.org/wiki/Forward_difference) in Zen C.

*This article uses material from the Rosetta Code article **Forward difference**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Forward_difference?action=history).*
