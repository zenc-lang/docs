+++
title = "Common list elements"
+++

# Common list elements

```zc
import "std/vec.zc"

fn intersection(a: Vec<int>*, b: Vec<int>*) -> Vec<int> {
    let res = Vec<int>::new();
    for e in *a {
        if b.contains(e) { res << e; }
    }
    return res;
}

fn main() {
    let a1 = [2, 5, 1, 3, 8, 9, 4, 6];
    let a2 = [3, 5, 6, 2, 9, 8, 4];
    let a3 = [1, 3, 7, 6, 9];
    let v1 = Vec<int>::new();
    let v2 = Vec<int>::new();
    let v3 = Vec<int>::new();
    for e in a1 { v1 << e; }
    for e in a2 { v2 << e; }
    for e in a3 { v3 << e; }
    let inter1 = intersection(&v1, &v2);
    let inter2 = intersection(&inter1, &v3);
    print "[";
    for v in inter2 { print "{v}, "; }
    println "\b\b]";
}
```

**Output:**

```
[3, 9, 6]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Common list elements**](https://rosettacode.org/wiki/Common_list_elements) in Zen C.

*This article uses material from the Rosetta Code article **Common list elements**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Common_list_elements?action=history).*
