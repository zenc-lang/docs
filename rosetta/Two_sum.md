+++
title = "Two sum"
+++

# Two sum

```zc
fn two_sum(a: int*, len: const usize, target: int) -> (int, int, bool) {
    if len < 2 { return (0, 0, false); }
    for i in 0..(len - 1) {
        if a[i] <= target {
            for j in (i + 1)..len {
                let sum = a[i] + a[j]; 
                if sum == target { return (i, j, true); }
                if sum > target { break; }
            }
        } else { break; }
    }
    return (0, 0, false);
}

fn main() {
    let a = [0, 2, 11, 19, 90];
    let targets  = [21, 25, 90];
    for target in targets {
        let (p1, p2, ok) = two_sum(a, a.len, target);
        if !ok {
            println "No two numbers were found whose sum is {target}.";
        } else {
            println "The numbers with indices {p1} annd {p2} sum to {target}.";
        }
        println "";
    }
}
```

**Output:**

```
The numbers with indices 1 annd 3 sum to 21.

No two numbers were found whose sum is 25.

The numbers with indices 0 annd 4 sum to 90.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Two sum**](https://rosettacode.org/wiki/Two_sum) in Zen C.

*This article uses material from the Rosetta Code article **Two sum**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Two_sum?action=history).*
