+++
title = "Hash from two arrays"
+++

# Hash from two arrays

{{trans|Wren}}
Note that Zen C makes no guarantee about iteration order which is not necessarily the same order in which the entries were added. 

```zc
import "std/map.zc"

fn main() {
    let keys = ["1", "2", "3", "4", "5"];
    let values = ["first", "second", "third", "fourth","fifth"];
    let hash = Map<string>::new();
    for i in 0..5 { hash.put(keys[i], values[i]); }
    for entry in hash {
        print "{{{entry.key}: {entry.val}}}, ";
    }
    println "\b\b ";
}
```

**Output:**

```
{5: fifth}, {3: third}, {4: fourth}, {1: first}, {2: second}
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Hash from two arrays**](https://rosettacode.org/wiki/Hash_from_two_arrays) in Zen C.

*This article uses material from the Rosetta Code article **Hash from two arrays**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Hash_from_two_arrays?action=history).*
