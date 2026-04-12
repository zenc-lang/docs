+++
title = "Tokenize a string"
+++

# Tokenize a string

```zc
import "std/string.zc"

fn main() {
    let s = String::from("Hello,How,Are,You,Today");
    let words = s.split(',');
    for i in 0..words.length() { print "{words[i]}."; }
    println "\b ";
}
```

**Output:**

```
Hello.How.Are.You.Today
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Tokenize a string**](https://rosettacode.org/wiki/Tokenize_a_string) in Zen C.

*This article uses material from the Rosetta Code article **Tokenize a string**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Tokenize_a_string?action=history).*
