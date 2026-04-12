+++
title = "Positive decimal integers with the digit 1 occurring exactly twice"
+++

# Positive decimal integers with the digit 1 occurring exactly twice

```zc
fn two_ones(n: int) -> bool {
    let s = "{n}";
    let ones = 0;
    for i in 0..strlen(s) {
        if s[i] == '1' { ones++; }
    }
    return ones == 2;
}

fn main() {
    println "Decimal numbers under 1,000 whose digits include two 1's:";
    let count = 0;
    for i in 1..1000 {
        if two_ones(i) {
            print "{i:3d}  ";
            if !(++count % 9) { println ""; }
        }
    }
    println "\nFound {count} such numbers.";
}
```

**Output:**

```
Decimal numbers under 1,000 whose digits include two 1's:
 11  101  110  112  113  114  115  116  117  
118  119  121  131  141  151  161  171  181  
191  211  311  411  511  611  711  811  911  

Found 27 such numbers.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Positive decimal integers with the digit 1 occurring exactly twice**](https://rosettacode.org/wiki/Positive_decimal_integers_with_the_digit_1_occurring_exactly_twice) in Zen C.

*This article uses material from the Rosetta Code article **Positive decimal integers with the digit 1 occurring exactly twice**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Positive_decimal_integers_with_the_digit_1_occurring_exactly_twice?action=history).*
