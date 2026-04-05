+++
title = "Averages/Median"
+++

# Averages/Median

```zc
import "std/sort.zc"

fn median(a: f64*, len: const usize) -> f64 {
    // Avoid mutating 'a' by copying it to a new buffer 'b'.
    let bytes = len * sizeof(f64);
    autofree let b = (f64*)malloc(bytes);
    memcpy(b, a, bytes);
    sort_double(b, len);
    let hl = len / 2;
    let med = len % 2 ? b[hl] : (b[hl - 1] + b[hl]) / 2.0;
    return med;
}

fn main() {
    let a1 = [4.1, 5.6, 7.2, 1.7, 9.3, 4.4, 3.2];
    let a2 = [4.1, 7.2, 1.7, 9.3, 4.4, 3.2];
    let as: f64*[2] = [a1, a2];
    let lens = [7, 6];
    for i in 0..2 { println "{median(as[i], lens[i]):g}" };
}
```

**Output:**

```
4.4
4.25
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Averages/Median**](https://rosettacode.org/wiki/Averages/Median) in Zen C.

*This article uses material from the Rosetta Code article **Averages/Median**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Averages/Median?action=history).*
