+++
title = "Collections"
+++

# Collections

As well as C style arrays, Zen C's standard library also supports vectors, maps, sets, stacks and queues. The following example uses a vector which is a generic growable array:

```zc
import "std/vec.zc";

fn main() {
    let vec = Vec<int>::new();
    vec << 1;
    vec << 2;
    vec << 3;
    for v in vec { println "{v}"; }
}
```

**Output:**

```
1
2
3
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Collections**](https://rosettacode.org/wiki/Collections) in Zen C.

*This article uses material from the Rosetta Code article **Collections**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Collections?action=history).*
