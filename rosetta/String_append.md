+++
title = "String append"
+++

# String append

```zc
import "std/string.zc"

fn main() {
    let s = String::from("Hello, ");
    s.append_c("world!");
    println "{s}";
}
```

**Output:**

```
Hello, world!
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**String append**](https://rosettacode.org/wiki/String_append) in Zen C.

*This article uses material from the Rosetta Code article **String append**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/String_append?action=history).*
