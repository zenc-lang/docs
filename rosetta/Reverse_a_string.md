+++
title = "Reverse a string"
+++

# Reverse a string

```zc
import "std/string.zc"

fn reverse_str(s: string) -> string {
    let s2 = String::from(s);
    let r = s2.runes();
    r.reverse();
    return String::from_runes_vec(r).c_str();
}

fn main() {
    let words= ["asdf", "josé", "møøse", "was it a car or a cat I saw", "😀🚂🦊"];
    for word in words {
        let rev = reverse_str(word);
        println "{rev}";
    }
}
```

**Output:**

```
fdsa
ésoj
esøøm
was I tac a ro rac a ti saw
🦊🚂😀
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Reverse a string**](https://rosettacode.org/wiki/Reverse_a_string) in Zen C.

*This article uses material from the Rosetta Code article **Reverse a string**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Reverse_a_string?action=history).*
