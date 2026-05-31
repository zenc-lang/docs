+++
title = "Kaprekar numbers"
+++

# Kaprekar numbers

{{trans|Wren}}

```zc
import "std/string.zc"

fn kaprekar(n: u64, base: u64) -> (bool, int) {
    if n == 1 { return (true, -1); }
    let order = 0;
    let nn = n * n;
    let power: u64 = 1;
    while power <= nn {
        power *= base;
        order++;
    }
    power /= base;
    order--;
    for ; power > 1; power /= base {
        let q = nn / power;
        let r = nn % power;
        if q >= n { return (false, -1); }
        if q + r == n { return (true, order); }
        order--;
    }
    return (false, -1);
}

let digits = "0123456789abcdefghijklmnopqrstuvwxyz";

fn atoi_b(s: string, base: u64) -> u64 {
    let res: u64 = 0;
    for i in 0..strlen(s) {
        let ix: u64 = strchr(digits, s[i]) - digits;
        res = res * base + ix;
    }
    return res;
}

fn itoa_b(n: u64, base: u64) -> String {
    if n == 0 { return String::from("0"); }
    let vr = Vec<rune>::new();
    while n > 0 {
        vr << digits[n % base];
        n /= base;
    }
    vr.reverse();
    return String::from_runes_vec(vr);
}

fn main() {
    let max: u64 = 10_000;
    println "Kaprekar numbers < {max}:";
    for let m: u64 = 0; m < max; ++m {
        if kaprekar(m, 10).v0 { println "  {m}"; }
    }

    // extra credit
    max = 1_000_000;
    let count = 0;
    for let m: u64 = 0; m < max; ++m {
        if kaprekar(m, 10).v0 { count++; }
    }
    println "\nThere are {count} Kaprekar numbers < {max}.";

    // extra extra credit
    let base: const int = 17;
    let max_b = "1000000";
    println "\nKaprekar numbers between 1 and {max_b} (base {base}):";
    max = atoi_b(max_b, base);
    println "\n Base 10  Base {base}        Square       Split";
    for let m: u64 = 2; m < max; ++m {
        let (is, pos) = kaprekar(m, base);
        if !is { continue; }
        let sq  = itoa_b(m * m, base);
        let str = itoa_b(m, base);
        let len = sq.length();
        let split = len - pos;
        let sub1 = sq.substring(0, split);
        let sub2 = sq.substring(split, len - split);
        println "{m:8lu}  {str.c_str():7s}  {sq.c_str():12s}  {sub1.c_str():6s} + {sub2}";
    }
}
```

**Output:**

```
Kaprekar numbers < 10000:
  1
  9
  45
  55
  99
  297
  703
  999
  2223
  2728
  4879
  4950
  5050
  5292
  7272
  7777
  9999

There are 54 Kaprekar numbers < 1000000.

Kaprekar numbers between 1 and 1000000 (base 17):

 Base 10  Base 17        Square       Split
      16        g            f1       f + 1
      64       3d           e2g       e + 2g
     225       d4          a52g      a5 + 2g
     288       gg          gf01      gf + 01
    1536      556        1b43b2     1b4 + 3b2
    3377      bbb        8093b2     809 + 3b2
    4912      ggg        ggf001     ggf + 001
    7425     18bd       24e166g     24e + 166g
    9280     1f1f       39b1b94     39b + 1b94
   16705     36db       b992c42     b99 + 2c42
   20736     43cd      10de32fg    10de + 32fg
   30016     61eb      23593f92    2359 + 3f92
   36801     785d      351e433g    351e + 433g
   37440     7a96      37144382    3714 + 4382
   46081     967b      52g94382    52g9 + 4382
   46720     98b4      5575433g    5575 + 433g
   53505     af26      6ga43f92    6ga4 + 3f92
   62785     cd44      9a5532fg    9a55 + 32fg
   66816     da36      aeg42c42    aeg4 + 2c42
   74241     f1f2      d75f1b94    d75f + 1b94
   76096     f854      e1f5166g    e1f5 + 166g
   83520     gggg      gggf0001    gggf + 0001
  266224    33334     a2c52a07g    a2c5 + 2a07g
 1153633    ddddd    b3d5e2a07g   b3d5e + 2a07g
 1334529    fgacc    f0540f1a78    f054 + 0f1a78
 1419856    ggggg    ggggf00001   ggggf + 00001
 1787968   146fca   19g4c12dg7f   19g4c + 12dg7f
 3122497   236985   4e3be1f95d8   4e3be + 1f95d8
 3773952   2b32b3   711cb2420f9   711cb + 2420f9
 4243968   2gde03   8fegb27eg09   8fegb + 27eg09
 5108481   3a2d6f   cg10b2e3c64   cg10b + 2e3c64
 5561920   3fa16d   f5eae3043cg   f5eae + 3043cg
 6031936   443ccd  110dde332ffg  110dde + 332ffg
 6896449   4e9c28  16a10c37gb1d  16a10c + 37gb1d
 7435233   54067b  1a72g93aa382  1a72g9 + 3aa382
 8017920   5aggb6  1ef1d43d1ef2  1ef1d4 + 3d1ef2
 9223201   687534  2835c5403g7g  2835c5 + 403g7g
 9805888   6f6f6g  2dbe3f41c131  2dbe3f + 41c131
11140416   7e692a  3a997c43dgbf  3a997c + 43dgbf
11209185   7f391e  3b58d543f059  3b58d5 + 43f059
12928384   91d7f3  4ef79b43f059  4ef79b + 43f059
12997153   92a7e7  4fd82943dgbf  4fd829 + 43dgbf
14331681   a1a1a1  5gf07041c131  5gf070 + 41c131
14914368   a89bdd  685c5e403g7g  685c5e + 403g7g
16119649   b6005b  79f2793d1ef2  79f279 + 3d1ef2
16702336   bcga96  8267143aa382  826714 + 3aa382
17241120   c274e9  8b7acd37gb1d  8b7acd + 37gb1d
18105633   ccd444  99a555332ffg  99a555 + 332ffg
18575649   d16fa4  a12be53043cg  a12be5 + 3043cg
19029088   d6e3a2  a9a83f2e3c64  a9a83f + 2e3c64
19893601   e032ge  b953g527eg09  b953g5 + 27eg09
20363617   e5de5e  c1bd752420f9  c1bd75 + 2420f9
21015072   eda78c  cf11c41f95d8  cf11c4 + 1f95d8
22349601   fca147  e9d1d912dg7f  e9d1d9 + 12dg7f
22803040   g10645  f2fcde0f1a78  f2fcde + 0f1a78
24137568   gggggg  gggggf000001  gggggf + 000001
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Kaprekar numbers**](https://rosettacode.org/wiki/Kaprekar_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Kaprekar numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Kaprekar_numbers?action=history).*
