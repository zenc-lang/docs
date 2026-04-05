+++
title = "Jewels and stones"
+++

# Jewels and stones

```zc
fn count_jewels(stones: string, jewels: string) -> int {
    let count = 0;
    for i in 0..strlen(stones) {
        for j in 0..strlen(jewels) {
            if stones[i] == jewels[j] { count++; break; }
        }
    }
    return count;
}

fn main() {
    let stones = "aAAbbbb";
    let jewels = "aA";
    println "{count_jewels(stones, jewels)}";
}
```

**Output:**

```
3
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Jewels and stones**](https://rosettacode.org/wiki/Jewels_and_stones) in Zen C.

*This article uses material from the Rosetta Code article **Jewels and stones**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Jewels_and_stones?action=history).*
