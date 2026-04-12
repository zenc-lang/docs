+++
title = "Arena storage pool"
+++

# Arena storage pool

Note that, as the Arena struct implements the Drop trait, the memory used is freed automatically when it goes out of scope.

```zc
import "std/arena.zc"

fn main() {
    // Create an arena with 100 bytes capacity.
    let a = Arena::new(100);

    // Allocate an array of 8 32-bit integers i.e. 32 bytes.
    let arr = a.alloc_n<int>(8);
    for i in 0..8 {
        arr[i] = i + 1;
        print "{arr[i]} ";
    }
    println "";

    // Duplicate a C string into the arena.
    let s = a.dup_str("Rosetta Code"); // uses 13 bytes including final '\0'
    println "{s}";

    println "Arena has used     : {a.bytes_used()} bytes";
    println "Capacity remaining : {a.bytes_free()} bytes";
}
```

**Output:**

```
1 2 3 4 5 6 7 8 
Rosetta Code
Arena has used     : 45 bytes
Capacity remaining : 55 bytes
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Arena storage pool**](https://rosettacode.org/wiki/Arena_storage_pool) in Zen C.

*This article uses material from the Rosetta Code article **Arena storage pool**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Arena_storage_pool?action=history).*
