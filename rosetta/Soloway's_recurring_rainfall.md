+++
title = "Soloway's recurring rainfall"
+++

# Soloway's recurring rainfall

{{trans|Wren}}

```zc
import "std/io.zc"

fn main() {
    let n = 0;
    let sum = 0;
    loop {
        print "Enter integral rainfall (99999 to quit): ";
        autofree let input = readln();
        if strchr(input, '.') {
            println "Must be a non-zero integer, try again.";
            continue;
        }
        let i = atoi(input);
        if !i {
            println "Must be a non-zero integer, try again.";
            continue;
        }
        if i == 99999 { break; }
        n++;
        sum += i;
        let avg = (f64)sum / (f64)n;
        println "  The current average rainfall is {avg:g}";
    }
}
```

**Output:**

Sample run:

```
Enter integral rainfall (99999 to quit): 5.4
Must be a non-zero integer, try again.
Enter integral rainfall (99999 to quit): five
Must be a non-zero integer, try again.
Enter integral rainfall (99999 to quit): 5
  The current average rainfall is 5
Enter integral rainfall (99999 to quit): -2
  The current average rainfall is 1.5
Enter integral rainfall (99999 to quit): 4
  The current average rainfall is 2.33333
Enter integral rainfall (99999 to quit): 10
  The current average rainfall is 4.25
Enter integral rainfall (99999 to quit): 99999
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Soloway's recurring rainfall**](https://rosettacode.org/wiki/Soloway's_recurring_rainfall) in Zen C.

*This article uses material from the Rosetta Code article **Soloway's recurring rainfall**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Soloway's_recurring_rainfall?action=history).*
