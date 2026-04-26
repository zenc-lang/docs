+++
title = "Knuth shuffle"
+++

# Knuth shuffle

As Zen C does not support empty arrays, we are unable to do the first test case.

```zc
import "std/random.zc"

fn knuth_shuffle<T>(a: T*, len: usize) {
    let rng = Random::new();
    for let i: usize = len - 1; i >= 1; --i {
        let j = rng.next_int_range(0, i);
        if j != i {
            let t = a[i];
            a[i] = a[j];
            a[j] = t;
        }
    }
}

fn main() {
    let a1 = [10];
    let a2 = [10, 20];
    let a3 = [10, 20, 30];
    let aa: int*[3] = [a1, a2, a3];
    for i in 0..3 {
        let a = aa[i];
        for j in 0..(i + 1) { print "{a[j]}, "; }
        print "\b\b -> ";
        knuth_shuffle<int>(a, (usize)(i + 1));
        for j in 0..(i + 1) { print "{a[j]}, "; }
        println "\b\b ";
    }
}
```

**Output:**

Sample output:

```
10 -> 10  
10, 20 -> 20, 10  
10, 20, 30 -> 20, 30, 10
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Knuth shuffle**](https://rosettacode.org/wiki/Knuth_shuffle) in Zen C.

*This article uses material from the Rosetta Code article **Knuth shuffle**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Knuth_shuffle?action=history).*
