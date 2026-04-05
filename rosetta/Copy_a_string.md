+++
title = "Copy a string"
+++

# Copy a string

```zc
fn main() {
    autofree let dup = strdup("I'm a duplicate!");
    println "{dup}";
}
```

**Output:**

```
I'm a duplicate!
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Copy a string**](https://rosettacode.org/wiki/Copy_a_string) in Zen C.

*This article uses material from the Rosetta Code article **Copy a string**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Copy_a_string?action=history).*
