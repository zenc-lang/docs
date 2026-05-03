+++
title = "Dynamic variable names"
+++

# Dynamic variable names

{{trans|Wren}}
Zen C is a statically typed, compiled language and so it is not possible to create new variables, dynamically, at run time. As other entries have done, we therefore simulate this using a map.

```zc
import "std/map.zc"
import "std/io.zc"

fn main() {
    let vars = Map<int>::new();
    println "Enter three variables:";
    for _ in 0..3 {
        print "  name  : ";
        autofree let name = readln();
        print "  value : ";
        autofree let value = readln();
        vars.put(name, atoi(value));
        println "";
    }

    println "Your variables are:";
    for v in vars {
        println "  {v.key} = {v.val}";
    }
}
```

**Output:**

Sample input/output:

```
Enter three variables:
  name  : faith
  value : 1

  name  : hope
  value : 2

  name  : charity
  value : 3

Your variables are:
  hope = 2
  charity = 3
  faith = 1
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Dynamic variable names**](https://rosettacode.org/wiki/Dynamic_variable_names) in Zen C.

*This article uses material from the Rosetta Code article **Dynamic variable names**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Dynamic_variable_names?action=history).*
