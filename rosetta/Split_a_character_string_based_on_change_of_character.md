+++
title = "Split a character string based on change of character"
+++

# Split a character string based on change of character

```zc
import "std/string.zc"

fn split(s: String) {
    if s.length() == 0 { return; }
    let last = s.utf8_at(0);
    let curr = last;
    for i, code in s {
        if i != 0 {
            let c = String::from_rune(code);
            if c == last {
                curr += &c;
            } else {
                print "{curr}, ";
                curr = c;
            }
            last = c;
        }
    }
    println "{curr}";
}

fn main() {
    let s = String::from("gHHH5YY++///\\");
    split(s);
}
```

**Output:**

```
g, HHH, 5, YY, ++, ///, \
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Split a character string based on change of character**](https://rosettacode.org/wiki/Split_a_character_string_based_on_change_of_character) in Zen C.

*This article uses material from the Rosetta Code article **Split a character string based on change of character**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Split_a_character_string_based_on_change_of_character?action=history).*
