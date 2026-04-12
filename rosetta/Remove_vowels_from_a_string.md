+++
title = "Remove vowels from a string"
+++

# Remove vowels from a string

```zc
import "std/string.zc"

fn remove_vowels(s: string) -> string {
    let res = String::from(s);
    let vowels = String::from("aeiouAEIOU");
    let len = res.utf8_len();
    for (let i: isize = len - 1; i >= 0; --i) {
        let c = res.utf8_get(i);
        if vowels.contains(c) { res.remove_rune_at(i); }
    }
    return res.c_str();
}

fn main() {
    let s = "The Zen C Programming Language";
    println "Input  : {s}";
    s = remove_vowels(s);
    println "Output : {s}";
}
```

**Output:**

```
Input  : The Zen C Programming Language
Output : Th Zn C Prgrmmng Lngg
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Remove vowels from a string**](https://rosettacode.org/wiki/Remove_vowels_from_a_string) in Zen C.

*This article uses material from the Rosetta Code article **Remove vowels from a string**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Remove_vowels_from_a_string?action=history).*
