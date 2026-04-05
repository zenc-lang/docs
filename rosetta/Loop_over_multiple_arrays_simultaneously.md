+++
title = "Loop over multiple arrays simultaneously"
+++

# Loop over multiple arrays simultaneously

```zc
fn main() {
    let a1: string[3] = ["a", "b", "c"];
    let a2: string[3] = ["A", "B", "C"];
    let a3: int[3] = [1, 2, 3];
    for i in a3 {
        println "{a1[i - 1]}{a2[i - 1]}{i}";
    }
}
```

**Output:**

```
aA1
bB2
cC3
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Loop over multiple arrays simultaneously**](https://rosettacode.org/wiki/Loop_over_multiple_arrays_simultaneously) in Zen C.

*This article uses material from the Rosetta Code article **Loop over multiple arrays simultaneously**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Loop_over_multiple_arrays_simultaneously?action=history).*
