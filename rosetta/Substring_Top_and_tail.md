+++
title = "Substring/Top and tail"
+++

# Substring/Top and tail

```zc
import "std/string.zc"

fn main() {
    let s = "Beyoncé";
    let a = String::from(s);
    let l = a.utf8_len();
    let b = a.utf8_substr(1, l - 1);
    let c = a.utf8_substr(0, l - 1);
    let d = a.utf8_substr(1, l - 2);
    let e: String[4] = [a, b, c, d];
    for i in 0..e.len { println "{e[i]}"; }
}
```

**Output:**

```
Beyoncé
eyoncé
Beyonc
eyonc
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Substring/Top and tail**](https://rosettacode.org/wiki/Substring/Top_and_tail) in Zen C.

*This article uses material from the Rosetta Code article **Substring/Top and tail**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Substring/Top_and_tail?action=history).*
