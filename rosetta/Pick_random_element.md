+++
title = "Pick random element"
+++

# Pick random element

```zc
import "std/random.zc"

fn main() {
    let rng = Random::new();
    let planets = ["Earth", "Venus", "Mercury", "Mars", "Jupiter"];
    // Permits repeats.
    for _ in 0..5 {
        let r = rng.next_int_range(0, 4);
        println "{planets[r]}";
    }
}
```

**Output:**

Sample output:

```
Mercury
Jupiter
Mercury
Mars
Venus
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Pick random element**](https://rosettacode.org/wiki/Pick_random_element) in Zen C.

*This article uses material from the Rosetta Code article **Pick random element**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Pick_random_element?action=history).*
