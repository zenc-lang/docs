+++
title = "Hailstone sequence"
+++

# Hailstone sequence

```zc
import "std/vec.zc"

fn hailstone(n: int) -> Vec<int> {
    assert(n > 0, "Parameter must be a positive integer.");
    let h = Vec<int>::new();
    h << n;
    while n != 1 {
        n = (n % 2 == 0) ? n / 2 : 3 * n + 1;
        h << n;
    }
    return h;
}

fn main() {
    let h = hailstone(27);
    let len = h.length();
    println "For the Hailstone sequence starting with n = 27:";
    println "   Number of elements  = {len}";
    print "   First four elements = ";
    for i in 0..4 { print "{h[i]} "; }
    print "\n   Final four elements = ";
    for i in (len - 4)..len { print "{h[i]} "; }
    println "";

    println "\nThe Hailstone sequence for n < 100,000 with the longest length is:";
    let longest = 0;
    let longlen: u64 = 0;
    for n in 1..100_000 {
        let hs = hailstone(n);
        let c = h.length();
        if c > longlen {
            longest = n;
            longlen = c;
        }
    }
    println "   Longest = {longest}";
    println "   Length  = {longlen}";
}
```

**Output:**

```
For the Hailstone sequence starting with n = 27:
   Number of elements  = 112
   First four elements = 27 82 41 124 
   Final four elements = 8 4 2 1 

The Hailstone sequence for n < 100,000 with the longest length is:
   Longest = 1
   Length  = 112
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Hailstone sequence**](https://rosettacode.org/wiki/Hailstone_sequence) in Zen C.

*This article uses material from the Rosetta Code article **Hailstone sequence**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Hailstone_sequence?action=history).*
