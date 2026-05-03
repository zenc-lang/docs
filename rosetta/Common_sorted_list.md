+++
title = "Common sorted list"
+++

# Common sorted list

```zc
import "std/vec.zc"
import "std/sort.zc"

fn distinct_union(a: Vec<int>*, b: Vec<int>*) -> Vec<int> {
    let res = Vec<int>::new();
    for e in *a { if !res.contains(e) { res << e; } }
    for e in *b { if !res.contains(e) { res << e; } }
    return res;
}

fn main() {
    let a1 = [5, 1, 3, 8, 9, 4, 8, 7];
    let a2 = [3, 5, 9, 8, 4];
    let a3 = [1, 3, 7, 9];
    let v1 = Vec<int>::new();
    let v2 = Vec<int>::new();
    let v3 = Vec<int>::new();
    for e in a1 { v1 << e; }
    for e in a2 { v2 << e; }
    for e in a3 { v3 << e; }
    let du1 = distinct_union(&v1, &v2);
    let du2 = distinct_union(&du1, &v3);
    sort_int(du2.data, du2.len);
    print "[";
    for e in du2 { print "{e}, "; }
    println "\b\b]";
}
```

**Output:**

```
[1, 3, 4, 5, 7, 8, 9]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Common sorted list**](https://rosettacode.org/wiki/Common_sorted_list) in Zen C.

*This article uses material from the Rosetta Code article **Common sorted list**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Common_sorted_list?action=history).*
