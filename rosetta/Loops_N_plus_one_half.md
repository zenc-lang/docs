+++
title = "Loops/N plus one half"
+++

# Loops/N plus one half

```zc
fn main() {
    for i in 1..=10 {
        print "{i}";
        let s = i < 10 ? ", " : "\n"
        print "{s}"
    }
}
```

**Output:**

```
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Loops/N plus one half**](https://rosettacode.org/wiki/Loops/N_plus_one_half) in Zen C.

*This article uses material from the Rosetta Code article **Loops/N plus one half**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Loops/N_plus_one_half?action=history).*
