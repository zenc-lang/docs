+++
title = "Sorting algorithms/Bubble sort"
+++

# Sorting algorithms/Bubble sort

Based on the pseudo-code in the Wikipedia article.

```zc
fn bubble_sort(a: int*, n: const usize) {
    if n < 2 { return; }
    loop {
        let swapped = false;
        for i in 1..n {
            if a[i - 1] > a[i] {
                let t = a[i - 1];
                a[i - 1] = a[i];
                a[i] = t;
                swapped = true;
            }
        }
        if !swapped { return; }
    }
}

fn main() {
    let a1 = [4, 65, 2, -31, 0, 99, 2, 83, 782, 1];
    let a2 = [7, 5, 2, 6, 1, 4, 2, 6, 3];
    let aa: int*[2] = [a1, a2];
    let lens = [a1.len, a2.len];
    for i in 0..aa.len {
        print "Before: [";
        for j in 0..lens[i] { print "{aa[i][j]}, "; }
        println "\b\b]";
        bubble_sort(aa[i], lens[i]);
        print "After : [";
        for j in 0..lens[i] { print "{aa[i][j]}, "; }
        println "\b\b]\n";
    }
}
```

**Output:**

```
Before: [4, 65, 2, -31, 0, 99, 2, 83, 782, 1] 
After : [-31, 0, 1, 2, 2, 4, 65, 83, 99, 782] 

Before: [7, 5, 2, 6, 1, 4, 2, 6, 3] 
After : [1, 2, 2, 3, 4, 5, 6, 6, 7]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sorting algorithms/Bubble sort**](https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort) in Zen C.

*This article uses material from the Rosetta Code article **Sorting algorithms/Bubble sort**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort?action=history).*
