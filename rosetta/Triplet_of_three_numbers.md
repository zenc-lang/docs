+++
title = "Triplet of three numbers"
+++

# Triplet of three numbers

```zc
import "locale.h"

fn is_prime(n: int) -> bool {
    if n < 2      { return false; }
    if n % 2 == 0 { return n == 2; }
    if n % 3 == 0 { return n == 3; }
    let d = 5;
    while d * d <= n {
        if n % d == 0 { return false; }
        d += 2;
        if n % d == 0 { return false; }
        d += 4;
    }
    return true;
}

fn main() {
    setlocale(LC_NUMERIC, "");
    println "Triplets of primes: (n - 1, n + 3, n + 5) where n < 6,000:";
    let count = 0;
    for n in 4..6000 step 2 {
        if is_prime(n - 1) && is_prime(n + 3) && is_prime(n + 5) {
            println "{n:'5d}  =>  {n - 1:'5d}  {n + 3:'5d}  {n + 5:'5d}";
            count++;
        }
    }
    println "\n{count} such triplets found.";
}
```

**Output:**

```
Triplets of primes: (n - 1, n + 3, n + 5) where n < 6,000:
    8  =>      7     11     13
   14  =>     13     17     19
   38  =>     37     41     43
   68  =>     67     71     73
   98  =>     97    101    103
  104  =>    103    107    109
  194  =>    193    197    199
  224  =>    223    227    229
  278  =>    277    281    283
  308  =>    307    311    313
  458  =>    457    461    463
  614  =>    613    617    619
  824  =>    823    827    829
  854  =>    853    857    859
  878  =>    877    881    883
1,088  =>  1,087  1,091  1,093
1,298  =>  1,297  1,301  1,303
1,424  =>  1,423  1,427  1,429
1,448  =>  1,447  1,451  1,453
1,484  =>  1,483  1,487  1,489
1,664  =>  1,663  1,667  1,669
1,694  =>  1,693  1,697  1,699
1,784  =>  1,783  1,787  1,789
1,868  =>  1,867  1,871  1,873
1,874  =>  1,873  1,877  1,879
1,994  =>  1,993  1,997  1,999
2,084  =>  2,083  2,087  2,089
2,138  =>  2,137  2,141  2,143
2,378  =>  2,377  2,381  2,383
2,684  =>  2,683  2,687  2,689
2,708  =>  2,707  2,711  2,713
2,798  =>  2,797  2,801  2,803
3,164  =>  3,163  3,167  3,169
3,254  =>  3,253  3,257  3,259
3,458  =>  3,457  3,461  3,463
3,464  =>  3,463  3,467  3,469
3,848  =>  3,847  3,851  3,853
4,154  =>  4,153  4,157  4,159
4,514  =>  4,513  4,517  4,519
4,784  =>  4,783  4,787  4,789
5,228  =>  5,227  5,231  5,233
5,414  =>  5,413  5,417  5,419
5,438  =>  5,437  5,441  5,443
5,648  =>  5,647  5,651  5,653
5,654  =>  5,653  5,657  5,659
5,738  =>  5,737  5,741  5,743

46 such triplets found.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Triplet of three numbers**](https://rosettacode.org/wiki/Triplet_of_three_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Triplet of three numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Triplet_of_three_numbers?action=history).*
