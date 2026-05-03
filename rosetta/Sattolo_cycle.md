+++
title = "Sattolo cycle"
+++

# Sattolo cycle

As Zen C does not support empty arrays, we are unable to do the first test case. However, to compensate, we add some string array examples.

```zc
import "std/random.zc"

let rng: Random;

fn sattolo<T>(a: T*, len: const usize) {
    for let i = len - 1; i >= 1; --i {
        let j = rng.next_int_range(0, i - 1);
        let t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}

fn main() {
    rng = Random::new();

    let a1 = [10];
    let a2 = [10, 20];
    let a3 = [10, 20, 30];
    let a4 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22];
    let aa: int*[4]= [a1, a2, a3, a4];
    let alen: usize[4] = [1, 2, 3, 12];
    for i in 0..4 {
        let a = aa[i];
        print "Original: ["
        for j in 0..alen[i] { print "{a[j]}, "; }
        println "\b\b]";
        sattolo(a, alen[i]);
        print "Sattolo : [";
        for j in 0..alen[i] { print "{a[j]}, "; }
        println "\b\b]\n";
    }

    let b1 = ["a", "b", "c", "d", "e"];
    let b2 = ["fgh", "ijk", "lmn", "opq", "rst", "uvw", "xyz"];
    let bb: string*[2] = [b1, b2];
    let blen: usize[2] = [5, 7];
    for i in 0..2 {
        let b = bb[i];
        print "Original: ["
        for j in 0..blen[i] { print "{b[j]}, "; }
        println "\b\b]";
        sattolo(b, blen[i]);
        print "Sattolo : [";
        for j in 0..blen[i] { print "{b[j]}, "; }
        println "\b\b]\n";
    }
}
```

**Output:**

Sample output:

```
Original: [10] 
Sattolo : [10] 

Original: [10, 20] 
Sattolo : [20, 10] 

Original: [10, 20, 30] 
Sattolo : [30, 10, 20] 

Original: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] 
Sattolo : [17, 13, 21, 20, 11, 14, 16, 15, 18, 12, 22, 19] 

Original: [a, b, c, d, e] 
Sattolo : [b, d, a, e, c] 

Original: [fgh, ijk, lmn, opq, rst, uvw, xyz] 
Sattolo : [lmn, xyz, uvw, ijk, fgh, opq, rst]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sattolo cycle**](https://rosettacode.org/wiki/Sattolo_cycle) in Zen C.

*This article uses material from the Rosetta Code article **Sattolo cycle**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sattolo_cycle?action=history).*
