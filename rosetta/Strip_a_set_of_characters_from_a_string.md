+++
title = "Strip a set of characters from a string"
+++

# Strip a set of characters from a string

```zc
import "std/string.zc"

fn strip_chars(s: String, t: String) -> String {
    let r = String::from("");
    for c in s {
        if !t.contains(c) { r.push_rune(c); }
    }
    return r;
}

fn main() {
    let s = String::from("She was a soul stripper. She took my heart!");
    let t = String::from("aei");
    let r = strip_chars(s, t);
    println "{r}";
}
```

**Output:**

```
Sh ws  soul strppr. Sh took my hrt!
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Strip a set of characters from a string**](https://rosettacode.org/wiki/Strip_a_set_of_characters_from_a_string) in Zen C.

*This article uses material from the Rosetta Code article **Strip a set of characters from a string**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Strip_a_set_of_characters_from_a_string?action=history).*
