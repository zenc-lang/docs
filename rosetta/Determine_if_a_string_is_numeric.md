+++
title = "Determine if a string is numeric"
+++

# Determine if a string is numeric

More or less the same function as the C entry except that I don't see why we should exclude otherwise numeric strings simply because they begin with whitespace.

```zc
fn is_numeric(s: const string) -> bool {
    if !s || *s == '\0' { return false; }
    let p: char*;
    strtod(s, &p);
    return *p == '\0';
}

fn main() {
    println "Are these strings numeric?\n"
    let tests: const string[8] = [NULL, "1", " 3.14", "-100", "1e2", "NaN", "0xaf", "rose"];
    for t in tests {
        let isnum = is_numeric(t);
        let yn = isnum ? "yes" : "no";
        println "{t:-6s} -> {yn}";
    }
}
```

**Output:**

```
Are these strings numeric?

(null) -> no
1      -> yes
 3.14  -> yes
-100   -> yes
1e2    -> yes
NaN    -> yes
0xaf   -> yes
rose   -> no
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Determine if a string is numeric**](https://rosettacode.org/wiki/Determine_if_a_string_is_numeric) in Zen C.

*This article uses material from the Rosetta Code article **Determine if a string is numeric**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Determine_if_a_string_is_numeric?action=history).*
