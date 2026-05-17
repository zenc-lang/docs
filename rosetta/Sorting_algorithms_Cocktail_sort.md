+++
title = "Sorting algorithms/Cocktail sort"
+++

# Sorting algorithms/Cocktail sort

{{trans|Wren}}

```zc
fn cocktail_sort(a: int*, len: const usize) {
    let last = (int)len - 1;
    loop {
        let swapped = false;
        for i in 0..last {
            if a[i] > a[i + 1] {
                let t = a[i];
                a[i] = a[i + 1];
                a[i + 1] = t;
                swapped = true;
            }
        }
        if !swapped { return; }
        swapped = false;
        if last >= 1 {
            for i in (last - 1)..=0 step - 1 {
                if a[i] > a[i + 1] {
                    let t = a[i];
                    a[i] = a[i + 1];
                    a[i + 1] = t;
                    swapped = true;
                }
            }
        }
        if !swapped { return; }
    }
}

fn main() {
    let a = [170, 45, 75, -90, -802, 24, 2, 66];
    print "Before: [";
    for i in 0..a.len { print "{a[i]}, "; }
    println "\b\b]";
    cocktail_sort((int*)a, a.len);
    print "After : [";
    for i in 0..a.len { print "{a[i]}, "; }
    println "\b\b] ";
}
```

**Output:**

```
Before: [170, 45, 75, -90, -802, 24, 2, 66] 
After : [-802, -90, 2, 24, 45, 66, 75, 170]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sorting algorithms/Cocktail sort**](https://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort) in Zen C.

*This article uses material from the Rosetta Code article **Sorting algorithms/Cocktail sort**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort?action=history).*
