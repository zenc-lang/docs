+++
title = "Find square difference"
+++

# Find square difference

```zc
fn main() {
    for let i = 1; ; ++i {
        let j = i - 1;
        if i * i - j * j > 1000 {
            println "{i}";
            break;
        }
    }
}
```

**Output:**

```
501
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Find square difference**](https://rosettacode.org/wiki/Find_square_difference) in Zen C.

*This article uses material from the Rosetta Code article **Find square difference**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Find_square_difference?action=history).*
