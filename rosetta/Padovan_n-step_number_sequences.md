+++
title = "Padovan n-step number sequences"
+++

# Padovan n-step number sequences

{{trans|C}}

```zc
fn padovan_n(n: int, t: usize, p: int*) {
    if n < 2 || t < 3 { 
        for i in 0..t { p[i] = 1; }
        return;
    }
    padovan_n(n - 1, t, p);
    for i in (n + 1)..t {
        p[i] = 0;
        for j in (i - 2)..=(i - n - 1) step -1 { p[i] += p[j]; }
    }
}

fn main() {
    let t: const usize = 15;
    let p: int[t];
    println "First {t} terms of the Padovan n-step number sequences:";
    for n in 2..=8 {
        for i in 0..t { p[i] = 0; }
        padovan_n(n, t, p);
        print "{n}: ";
        for i in 0..t { print "{p[i]:3d} "; }
        println "";
    }
}
```

**Output:**

```
First 15 terms of the Padovan n-step number sequences:
2:   1   1   1   2   2   3   4   5   7   9  12  16  21  28  37 
3:   1   1   1   2   3   4   6   9  13  19  28  41  60  88 129 
4:   1   1   1   2   3   5   7  11  17  26  40  61  94 144 221 
5:   1   1   1   2   3   5   8  12  19  30  47  74 116 182 286 
6:   1   1   1   2   3   5   8  13  20  32  51  81 129 205 326 
7:   1   1   1   2   3   5   8  13  21  33  53  85 136 218 349 
8:   1   1   1   2   3   5   8  13  21  34  54  87 140 225 362
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Padovan n-step number sequences**](https://rosettacode.org/wiki/Padovan_n-step_number_sequences) in Zen C.

*This article uses material from the Rosetta Code article **Padovan n-step number sequences**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Padovan_n-step_number_sequences?action=history).*
