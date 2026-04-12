+++
title = "RPG attributes generator"
+++

# RPG attributes generator

{{trans|Wren}}

```zc
import "std/random.zc"
import "std/sort.zc"

fn main() {
    let rng = Random::new();
    let vals: [int; 6];
    loop {
        for i in 0..6 {
            let rns: [int; 4];
            for j in 0..4 { rns[j] = rng.next_int_range(1, 6); }
            let sum = 0;
            for v in rns { sum += v; }
            sort_int((int*)rns, 4);
            vals[i] = sum - rns[0];
        }
        let total = 0;
        for v in vals { total += v; }
        if total > 75 {
            let fifteens = 0;
            for v in vals {
                if v >= 15 { fifteens++; }
            }
            if fifteens >= 2 {
                print "The six values are: ";
                for v in vals { print "{v}, "; }
                println "\b\b ";
                println "Their total is: {total} and {fifteens} of them are >= 15.";
                break;
            }
        }
    }
}
```

**Output:**

Sample run:

```
The six values are: 4, 16, 17, 18, 12, 12  
Their total is: 79 and 3 of them are >= 15.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**RPG attributes generator**](https://rosettacode.org/wiki/RPG_attributes_generator) in Zen C.

*This article uses material from the Rosetta Code article **RPG attributes generator**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/RPG_attributes_generator?action=history).*
