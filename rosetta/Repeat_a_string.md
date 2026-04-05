+++
title = "Repeat a string"
+++

# Repeat a string

```zc
import "std/string.zc"

fn main() {
    let s = String::new("");
    for _ in 0..5 { s.append_c("ha"); }
    println "{s}";
}
```

**Output:**

```
hahahahaha
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Repeat a string**](https://rosettacode.org/wiki/Repeat_a_string) in Zen C.

*This article uses material from the Rosetta Code article **Repeat a string**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Repeat_a_string?action=history).*
