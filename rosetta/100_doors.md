+++
title = "100 doors"
+++

# 100 doors

{{trans|Wren}}

### Unoptimized

```zc
fn main() {
    let doors: [bool; 100];
    for i in 0..100 { doors[i] = true; }
    for i in 1..=100 {
        let j = i;
        while j < 100 {
            doors[j] = !doors[j];
            j += i + 1;
        }
    }
    for i in 0..100 {
        if doors[i] { print "{i + 1} "; }
    }
    println "";
}
```

### Optimized

```zc
fn main() {
    let door = 1;
    let inc = 3;
    while door <= 100 {
        print "{door} ";
        door += inc;
        inc += 2;
    }
    println "";
}
```

**Output:**

For both versions:

```
1 4 9 16 25 36 49 64 81 100
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**100 doors**](https://rosettacode.org/wiki/100_doors) in Zen C.

*This article uses material from the Rosetta Code article **100 doors**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/100_doors?action=history).*
