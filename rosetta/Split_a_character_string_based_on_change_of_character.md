+++
title = "Split a character string based on change of character"
+++

# Split a character string based on change of character

```zc
fn split(s: string) {
    let len = strlen(s);
    if len == 0 { return; }
    let last = s[0];
    for i in 0..len {
        let curr = s[i];
        if curr == last {
            print "{curr:c}";
        } else {
            print ", {curr:c}";
            last = curr;
        }
    }
    println "";
}

fn main() {
    let s = "gHHH5YY++///\\";
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
