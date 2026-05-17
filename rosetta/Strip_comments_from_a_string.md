+++
title = "Strip comments from a string"
+++

# Strip comments from a string

```zc
import "std/string.zc"

fn strip_comments(s: string) -> String {
    let str = String::from(s);
    let tokens = ['#', ';'];
    for token in tokens {
        let t = str.split(token);
        defer { for i in 0..t.length() { t[i].free(); } }
        if t.length() > 1 {
            return t[0].trim();
        }
    }
    return str.trim();
}

fn main() {
    let strings = [
        " apples, pears # and bananas",
        " apples, pears ; and bananas",
        " apples, pears \t     "
    ]

    for s in strings {
        let t = strip_comments(s);
        println "'{s}' -> '{t}'";
    }
}
```

**Output:**

```
' apples, pears # and bananas' -> 'apples, pears'
' apples, pears ; and bananas' -> 'apples, pears'
' apples, pears 	     ' -> 'apples, pears'
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Strip comments from a string**](https://rosettacode.org/wiki/Strip_comments_from_a_string) in Zen C.

*This article uses material from the Rosetta Code article **Strip comments from a string**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Strip_comments_from_a_string?action=history).*
