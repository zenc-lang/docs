+++
title = "Largest int from concatenated ints"
+++

# Largest int from concatenated ints

{{trans|C}}

```zc
fn catcmp(a: const void*, b: const void*) -> int {
    let ab = "{*(int*)a}{*(int*)b}";
    let ba = "{*(int*)b}{*(int*)a}";
    return strcmp(ba, ab);
}

fn maxcat(a: int*, len: int) {
    print "[";
    for i in 0..len { print "{a[i]}, "; }
    print "\b\b] -> ";
    qsort(a, len, sizeof(int), catcmp);
    for i in 0..len { print "{a[i]}"; }
    println "";
}

fn main() {
    let x = [1, 34, 3, 98, 9, 76, 45, 4];
    let y = [54, 546, 548, 60];
    maxcat((int*)x, 8);
    maxcat((int*)y, 4);
}
```

**Output:**

```
[1, 34, 3, 98, 9, 76, 45, 4] -> 998764543431
[54, 546, 548, 60] -> 6054854654
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Largest int from concatenated ints**](https://rosettacode.org/wiki/Largest_int_from_concatenated_ints) in Zen C.

*This article uses material from the Rosetta Code article **Largest int from concatenated ints**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Largest_int_from_concatenated_ints?action=history).*
