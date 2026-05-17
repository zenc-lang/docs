+++
title = "Sorting algorithms/Circle sort"
+++

# Sorting algorithms/Circle sort

```zc
fn circle_sort(a: int*, lo: int, hi: int, swaps: int) -> int {
    if lo == hi { return swaps; }
    let high = hi;
    let low  = lo;
    let mid  = (hi - lo) / 2;
    while lo < hi {
        if a[lo] > a[hi] {
            let t = a[lo];
            a[lo] = a[hi];
            a[hi] = t;
            swaps++;
        }
        lo++;
        hi--;
    }
    if lo == hi {
        if a[lo] > a[hi + 1] {
            let t = a[lo];
            a[lo] = a[hi + 1];
            a[hi + 1] = t;
            swaps++;
        }
    }
    circle_sort(a, low, low + mid, swaps);
    circle_sort(a, low + mid + 1, high, swaps);
    return swaps;
}

fn main() {
    let a1 = [6, 7, 8, 9, 2, 5, 3, 4, 1];
    let a2 = [2, 14, 4, 6, 8, 1, 3, 5, 7, 11, 0, 13, 12, -1];
    let aa: int*[2] = [a1, a2];
    let lens = [a1.len, a2.len];
    for i in 0..aa.len {
        print "Before: [";
        for j in 0..lens[i] { print "{aa[i][j]}, "; }
        println "\b\b]";
        while circle_sort(aa[i], 0, (int)lens[i] - 1, 0) {};
        print "After : [";
        for j in 0..lens[i] { print "{aa[i][j]}, "; }
        println "\b\b]\n";
    }
}
```

**Output:**

```
Before: [6, 7, 8, 9, 2, 5, 3, 4, 1] 
After : [1, 2, 3, 4, 5, 6, 7, 8, 9] 

Before: [2, 14, 4, 6, 8, 1, 3, 5, 7, 11, 0, 13, 12, -1] 
After : [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sorting algorithms/Circle sort**](https://rosettacode.org/wiki/Sorting_algorithms/Circle_sort) in Zen C.

*This article uses material from the Rosetta Code article **Sorting algorithms/Circle sort**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sorting_algorithms/Circle_sort?action=history).*
