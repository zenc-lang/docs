+++
title = "McNuggets problem"
+++

# McNuggets problem

{{trans|Go}}

```zc
fn mcnugget(limit: int) {
    autofree let sv = (bool*)calloc(limit + 1, sizeof(bool));
    for s in 0..=limit step 6 {
        for n in s..=limit step 9 {
            for t in n..=limit step 20 { sv[t] = true; }
        }
    }
    for i in limit..=0 step -1 {
        if !sv[i] {
            println "Maximum non-McNuggets number is {i}.";
            return;
        }
    }
}

fn main() {
    mcnugget(100);
}
```

**Output:**

```
Maximum non-McNuggets number is 43.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**McNuggets problem**](https://rosettacode.org/wiki/McNuggets_problem) in Zen C.

*This article uses material from the Rosetta Code article **McNuggets problem**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/McNuggets_problem?action=history).*
