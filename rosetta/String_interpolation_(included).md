+++
title = "String interpolation (included)"
+++

# String interpolation (included)

Zen C supports implicit string interpolation. By enclosing a variable or expression in braces <code>{}</code> within a string literal, the compiler automatically formats and inserts the value. 

Further documentation on string formatting and escaping can be found in the [https://github.com/z-libs/Zen-C official language reference].

```zc
fn main() {
    let word = "little";
    
    // The variable 'word' is interpolated directly into the string
    println "Mary had a {word} lamb";
}
```

**Output:**

```
Mary had a little lamb
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**String interpolation (included)**](https://rosettacode.org/wiki/String_interpolation_(included)) in Zen C.

*This article uses material from the Rosetta Code article **String interpolation (included)**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/String_interpolation_(included)?action=history).*
