+++
title = "Sum and product of an array"
+++

# Sum and product of an array

```zc
fn main() {
    let a: int[10] = [7, 10, 2, 4, 6, 1, 8, 3, 9, 5];
    let sum  = 0;
    let prod = 1;
    print "Array    : ";
    for e in a {
        sum  += e;
        prod *= e;
        print "{e} ";
    }
    println "";
    println "Sum      : {sum}";
    println "Product  : {prod}";
}
```

**Output:**

```
Array    : 7 10 2 4 6 1 8 3 9 5 
Sum      : 55
Product  : 3628800
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sum and product of an array**](https://rosettacode.org/wiki/Sum_and_product_of_an_array) in Zen C.

*This article uses material from the Rosetta Code article **Sum and product of an array**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sum_and_product_of_an_array?action=history).*
