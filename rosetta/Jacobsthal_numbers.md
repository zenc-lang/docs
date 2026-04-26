+++
title = "Jacobsthal numbers"
+++

# Jacobsthal numbers

{{trans|C}}
{{libheader|GMP}}

```zc
//> link: -lgmp

import "gmp.h"

fn jacobsthal(r: mpz_t, n: c_ulong) {
    let s: mpz_t;
    mpz_init(s);
    mpz_set_ui(r, 1);
    mpz_mul_2exp(r, r, n);
    mpz_set_ui(s, 1);
    if n % 2 { mpz_neg(s, s); }
    mpz_sub(r, r, s);
    mpz_div_ui(r, r, 3);
}

fn jacobsthal_lucas(r: mpz_t, n: c_ulong) {
    let a: mpz_t;
    mpz_init(a);
    mpz_set_ui(r, 1);
    mpz_mul_2exp(r, r, n);
    mpz_set_ui(a, 1);
    if n % 2 { mpz_neg(a, a); }
    mpz_add(r, r, a);
}

fn main() {
    let jac: mpz_t[30];
    let j: mpz_t;
    println "First 30 Jacobsthal numbers:";
    for i in 0..30 {
        mpz_init(jac[i]);
        jacobsthal(jac[i], i);
        gmp_printf("%9Zd ", jac[i]);
        if !((i + 1) % 5) { println ""; }
    }

    println "\nFirst 30 Jacobsthal-Lucas numbers:";
    mpz_init(j);
    for i in 0..30 {
        jacobsthal_lucas(j, i);
        gmp_printf("%9Zd ", j);
        if !((i + 1) % 5) { println ""; }
    }

    println "\nFirst 20 Jacobsthal oblong numbers:";
    for i in 0..20 {
        mpz_mul(j, jac[i], jac[i + 1]);
        gmp_printf("%11Zd ", j);
        if !((i + 1) % 5) { println ""; }
    }

    println "\nFirst 20 Jacobsthal primes:";
    let count = 0;
    for let i = 0; count < 20; ++i {
        jacobsthal(j, i);
        if mpz_probab_prime_p(j, 15) > 0 {
            gmp_printf("%Zd\n", j);
            ++count;
        }
    }
}
```

**Output:**

```
First 30 Jacobsthal numbers:
        0         1         1         3         5 
       11        21        43        85       171 
      341       683      1365      2731      5461 
    10923     21845     43691     87381    174763 
   349525    699051   1398101   2796203   5592405 
 11184811  22369621  44739243  89478485 178956971 

First 30 Jacobsthal-Lucas numbers:
        2         1         5         7        17 
       31        65       127       257       511 
     1025      2047      4097      8191     16385 
    32767     65537    131071    262145    524287 
  1048577   2097151   4194305   8388607  16777217 
 33554431  67108865 134217727 268435457 536870911 

First 20 Jacobsthal oblong numbers:
          0           1           3          15          55 
        231         903        3655       14535       58311 
     232903      932295     3727815    14913991    59650503 
  238612935   954429895  3817763271 15270965703 61084037575 

First 20 Jacobsthal primes:
3
5
11
43
683
2731
43691
174763
2796203
715827883
2932031007403
768614336404564651
201487636602438195784363
845100400152152934331135470251
56713727820156410577229101238628035243
62357403192785191176690552862561408838653121833643
1046183622564446793972631570534611069350392574077339085483
267823007376498379256993682056860433753700498963798805883563
5562466239377370006237035693149875298444543026970449921737087520370363869220418099018130434731
95562442332919646317117537304253622533190207882011713489066201641121786503686867002917439712921903606443
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Jacobsthal numbers**](https://rosettacode.org/wiki/Jacobsthal_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Jacobsthal numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Jacobsthal_numbers?action=history).*
