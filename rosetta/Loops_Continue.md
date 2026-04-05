+++
title = "Loops/Continue"
+++

# Loops/Continue

```zc
fn main() {
    for i in 1..=10 {
        print "{i}";
        if i % 5 == 0 {
            println "";
            continue;
        }
        print ", ";
    }
}
```

**Output:**

```
1, 2, 3, 4, 5
6, 7, 8, 9, 10
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Loops/Continue**](https://rosettacode.org/wiki/Loops/Continue) in Zen C.

*This article uses material from the Rosetta Code article **Loops/Continue**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Loops/Continue?action=history).*
