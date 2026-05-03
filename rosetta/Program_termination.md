+++
title = "Program termination"
+++

# Program termination

```zc
fn main() {
    let problem: bool[2] = [false, true];
    for p in problem {
        if !p {
            println "There isn't a problem.";
        } else {
            println "There is now, exiting with code 1.";
            exit(1);
        }
    }
}
```

**Output:**

```
There isn't a problem.
There is now, exiting with code 1.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Program termination**](https://rosettacode.org/wiki/Program_termination) in Zen C.

*This article uses material from the Rosetta Code article **Program termination**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Program_termination?action=history).*
