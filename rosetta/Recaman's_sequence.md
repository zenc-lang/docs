+++
title = "Recaman's sequence"
+++

# Recaman's sequence

{{trans|Wren}}

```zc
import "std/vec.zc"
import "std/set.zc"

fn main() {
    let a = Vec<int>::new();
    a << 0;
    let used = Set<int>::new();
    used.add(0);
    let used1000 = Set<int>::new();
    used1000.add(0);
    let found_dup = false;
    let n = 1;
    while n <= 15 || !found_dup || used1000.length() < 1001 {
        let next = a[n - 1] - n;
        if next < 1 || used.contains(next) { next += 2 * n; }
        let already_used = used.contains(next);
        a << next;
        if !already_used {
            used.add(next);
            if next >= 0 && next <= 1000 { used1000.add(next); }
        }
        if n == 14 {
            println "The first 15 terms of the Recaman's sequence are:";
            print "[";
            for v in a { print "{v}, "; }
            println "\b\b]";
        }
        if !found_dup && already_used {
            println "\nThe first duplicated term is a[{n}] = {next}.";
            found_dup = true;
        }
        if used1000.length() == 1001 {
            println "\nTerms up to a[{n}] are needed to generate 0 to 1000.";
        }
        n++;
    }
}
```

**Output:**

```
The first 15 terms of the Recaman's sequence are:
[0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9] 

The first duplicated term is a[24] = 42.

Terms up to a[328002] are needed to generate 0 to 1000.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Recaman's sequence**](https://rosettacode.org/wiki/Recaman's_sequence) in Zen C.

*This article uses material from the Rosetta Code article **Recaman's sequence**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Recaman's_sequence?action=history).*
