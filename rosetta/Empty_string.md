+++
title = "Empty string"
+++

# Empty string

```zc
import "std/string.zc"

fn main() {
    // C style null-terminated strings.
    let s = "";
    if s == NULL || strlen(s) == 0 {
        println "'s' is empty.";
    } else {
        println "'s' is not empty.";
    }

    // Zen C style growable Strings.
    let z = String::from("0");
    if z.length() == 0 {
        println "'z' is empty.";
    } else {
        println "'z' is not empty.";
    }
}
```

**Output:**

```
's' is empty.
'z' is not empty.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Empty string**](https://rosettacode.org/wiki/Empty_string) in Zen C.

*This article uses material from the Rosetta Code article **Empty string**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Empty_string?action=history).*
