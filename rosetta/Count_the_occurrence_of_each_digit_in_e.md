+++
title = "Count the occurrence of each digit in e"
+++

# Count the occurrence of each digit in e

{{trans|Wren}}

```zc
fn count_digits_in_e(n: int) {
    autofree let v: int* = malloc(n * sizeof(int));
    for i in 0..n { v[i] = 1; }
    let dc: [int; 10];
    dc[2] = 1;  // to count the non-fractional digit
    for col in 1..(2 * n) {
        let a = n + 1;
        let c = 0;
        for i in 0..n {
            c += v[i] * 10;
            v[i] = c % a;
            c /= a--;
        }
        dc[c]++;
    }
    for d in 0..=9 { println "{d}: {dc[d]}"; }
    let t = 0;
    for d in dc { t += d; }
    println "Total digits: {t}";
}

fn main() {
    count_digits_in_e(2000);
    println "";
    count_digits_in_e(3000);
}
```

**Output:**

```
0: 396
1: 395
2: 390
3: 403
4: 387
5: 390
6: 422
7: 408
8: 397
9: 412
Total digits: 4000

0: 602
1: 592
2: 604
3: 625
4: 559
5: 586
6: 644
7: 600
8: 597
9: 591
Total digits: 6000
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Count the occurrence of each digit in e**](https://rosettacode.org/wiki/Count_the_occurrence_of_each_digit_in_e) in Zen C.

*This article uses material from the Rosetta Code article **Count the occurrence of each digit in e**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Count_the_occurrence_of_each_digit_in_e?action=history).*
