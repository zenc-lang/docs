+++
title = "Pascal's triangle"
+++

# Pascal's triangle

{{trans|Wren}}

```zc
fn factorial(n: uint) -> u64 {
    let prod: u64 = 1;
    for i in 2..=n { prod *= i; }
    return prod;
}

fn binomial(n: uint, k: uint) -> u64 {
    assert(n >= k, "The second argument cannot be more than the first");
    if n == k { return 1; }
    let prod: u64 = 1;
    let i = n - k + 1;
    while i <= n { prod *= i++; }
    return prod / factorial(k);
}

fn pascal_triangle(n: uint) {
    if n < 1 { return; }
    for i in 0..n {
        for _ in 1..(n - i) { print "   "; }
        for j in 0..=i {
            print "{binomial(i, j):3lu}   ";
        }
        println "";
    }
}

fn main() {
    pascal_triangle(13);
}
```

**Output:**

```
1   
                                   1     1   
                                1     2     1   
                             1     3     3     1   
                          1     4     6     4     1   
                       1     5    10    10     5     1   
                    1     6    15    20    15     6     1   
                 1     7    21    35    35    21     7     1   
              1     8    28    56    70    56    28     8     1   
           1     9    36    84   126   126    84    36     9     1   
        1    10    45   120   210   252   210   120    45    10     1   
     1    11    55   165   330   462   462   330   165    55    11     1   
  1    12    66   220   495   792   924   792   495   220    66    12     1
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Pascal's triangle**](https://rosettacode.org/wiki/Pascal's_triangle) in Zen C.

*This article uses material from the Rosetta Code article **Pascal's triangle**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Pascal's_triangle?action=history).*
