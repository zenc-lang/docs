+++
title = "Numbers which are not the sum of distinct squares"
+++

# Numbers which are not the sum of distinct squares

{{trans|C#}}

```zc
import "std/vec.zc"
import "std/math.zc"

// Recursively permutates the list of squares to seek a matching sum.
fn soms(n: int, f: Vec<int>*) -> bool {
    if n <= 0 { return false; }
    if f.contains(n) { return true; }
    let sum = 0;
    for v in *f { sum += v; }
    if n > sum { return false; }
    if n == sum { return true; }
    let rf = f.clone();
    rf.reverse();
    rf.remove(0);
    return soms(n - f.last(), &rf) || soms(n, &rf);
}

fn main() {
    let s = Vec<int>::new();
    let a = Vec<int>::new();
    let sf = "\nStopped checking after finding %d sequential non-gaps after the final gap of %d.\n";
    let i = 1;
    let g = 1;
    while g >= (i >> 1) {
        let r = (int)Math::sqrt((f64)i);
        if r * r == i { s << i; }
        if !soms(i, &s) {
            g = i;
            a << g;
        }
        i++;
    }
    println "Numbers which are not the sum of distinct squares:";
    for v in a { print "{v}, "; }
    println "\b\b ";
    println "\nFound {a.length()} such numbers.";
    printf(sf, i - g, g);
}
```

**Output:**

```
Numbers which are not the sum of distinct squares:
2, 3, 6, 7, 8, 11, 12, 15, 18, 19, 22, 23, 24, 27, 28, 31, 32, 33, 43, 44, 47, 48, 60, 67, 72, 76, 92, 96, 108, 112, 128  

Found 31 such numbers.

Stopped checking after finding 130 sequential non-gaps after the final gap of 128.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Numbers which are not the sum of distinct squares**](https://rosettacode.org/wiki/Numbers_which_are_not_the_sum_of_distinct_squares) in Zen C.

*This article uses material from the Rosetta Code article **Numbers which are not the sum of distinct squares**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Numbers_which_are_not_the_sum_of_distinct_squares?action=history).*
