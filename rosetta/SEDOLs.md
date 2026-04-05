+++
title = "SEDOLs"
+++

# SEDOLs

```zc
import "ctype.h"

fn is_upper_vowel(c: char) -> bool {
    return c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
}

fn sedol_checkdigit(s: const string) -> int {
    if strlen(s) != 6 { return -1; }
    let weights: int[6] = [1, 3, 1, 7, 3, 9];
    let sum = 0;
    for i in 0..=5 {
        let c = s[i];
        if !isupper(c) && !isdigit(c) { return -1; }
        if is_upper_vowel(c) { return -1; }
        let j = (c <= '9') ? c - '0' : c - 'A' + 10;
        sum += j * weights[i];
    }
    return (10 - sum % 10) % 10;
}

fn main() {
    let tests: const string[12] = [
        "710889",
        "B0YBKJ",
        "406566",
        "B0YBLH",
        "228276",
        "B0YBKL",
        "557910",
        "B0YBKR",
        "585284",
        "B0YBKT",
        "B00030",
        "I23456"
    ];

    for t in tests {
        let cd = sedol_checkdigit(t);
        if cd >= 0 {
            println "{t} -> {t}{cd}";
        } else {
            println "{t} -> not valid";
        }
    }
}
```

**Output:**

```
710889 -> 7108899
B0YBKJ -> B0YBKJ7
406566 -> 4065663
B0YBLH -> B0YBLH2
228276 -> 2282765
B0YBKL -> B0YBKL9
557910 -> 5579107
B0YBKR -> B0YBKR5
585284 -> 5852842
B0YBKT -> B0YBKT7
B00030 -> B000300
I23456 -> not valid
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**SEDOLs**](https://rosettacode.org/wiki/SEDOLs) in Zen C.

*This article uses material from the Rosetta Code article **SEDOLs**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/SEDOLs?action=history).*
