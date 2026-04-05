+++
title = "Rot-13"
+++

# Rot-13

```zc
fn rot13(s: const char*, r: char*) {
    let len: usize = strlen(s);
    for i in 0..len {
        let c = s[i];
        if (c >= 'A' && c <= 'M') || (c >= 'a' && c <= 'm') {
            r[i] = c + 13;
        } else if (c >= 'N' && c <= 'Z') || (c >= 'n' && c <= 'z') {
            r[i] = c - 13;
        } else {
            r[i] = c;
        }
    }
    r[len] = '\0';
}

fn main() {
    let s = "nowhere ABJURER";
    autofree let r: char* = malloc(strlen(s) + 1);
    rot13(s, r);
    println "{r}";
}
```

**Output:**

```
abjurer NOWHERE
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Rot-13**](https://rosettacode.org/wiki/Rot-13) in Zen C.

*This article uses material from the Rosetta Code article **Rot-13**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Rot-13?action=history).*
