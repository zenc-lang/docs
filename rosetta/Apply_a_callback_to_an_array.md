+++
title = "Apply a callback to an array"
+++

# Apply a callback to an array

In the absence of anything to the contrary in the task description, we mutate the original array rather than creating a new one.

```zc
fn square(n: int) -> int {
    return n * n;
}

fn main() {
    let a = [1, 2, 3, 4, 5];
    for i in 0..a.len {
        a[i] = square(a[i]);
        println "{a[i]}";
    }
}
```

**Output:**

```
1
4
9
16
25
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Apply a callback to an array**](https://rosettacode.org/wiki/Apply_a_callback_to_an_array) in Zen C.

*This article uses material from the Rosetta Code article **Apply a callback to an array**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Apply_a_callback_to_an_array?action=history).*
