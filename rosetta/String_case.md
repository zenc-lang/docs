+++
title = "String case"
+++

# String case

```zc
import "std/string.zc"

fn main() {
    let s = String::from("alphaBETA");
    println "{s.to_uppercase()}";
    println "{s.to_lowercase()}";
}
```

**Output:**

```
ALPHABETA
alphabeta
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**String case**](https://rosettacode.org/wiki/String_case) in Zen C.

*This article uses material from the Rosetta Code article **String case**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/String_case?action=history).*
