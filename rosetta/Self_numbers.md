+++
title = "Self numbers"
+++

# Self numbers

{{trans|Java}}

```zc
import "locale.h";

fn sieve(sv: bool*) {
    let ds: [int; 10000];
    let i = 9999;
    for a in 9..=0 step -1 {
        for b in 9..=0 step -1 {
            let s = a + b;
            for c in 9..=0 step -1 {
                let t = s + c;
                for d in 9..=0 step -1 {
                    ds[i--] = t + d;
                }
            }
        }
    }
    let n = 0;
    for a in 0..103 {
        let d = ds[a];
        for b in  0..1000 {
            let s = d + ds[b] + n;
            for c in 0..10000 {
                sv[ds[c] + (s++)] = true;
            }
            n += 10000;
        }
    }
}

fn main() {
    def MC = 103 * 1000 * 10000 + 11 * 9 + 1;
    autofree let sv = (bool*)calloc(MC + 1, sizeof(bool));
    sieve(sv);
    let count = 0;
    println "The first 50 self numbers are:";
    for let i = 0; count <= 50; ++i {
        if !sv[i] {
            if ++count <= 50 {
                print "{i:3d}  ";
                if !(count % 10) { println ""; }
            } else {
                setlocale(LC_NUMERIC, "");
                println "\n       Index     Self number";
            }
        }
    }
    let limit = 1;
    count = 0;
    for let i = 0; i < MC; ++i {
        if !sv[i] {
            if ++count == limit {
                println "{count:'12d}  {i:'13d}";
                limit *= 10;
            }
        }
    }
}
```

**Output:**

```
The first 50 self numbers are:
  1    3    5    7    9   20   31   42   53   64  
 75   86   97  108  110  121  132  143  154  165  
176  187  198  209  211  222  233  244  255  266  
277  288  299  310  312  323  334  345  356  367  
378  389  400  411  413  424  435  446  457  468  

       Index     Self number
           1              1
          10             64
         100            973
       1,000         10,188
      10,000        102,225
     100,000      1,022,675
   1,000,000     10,227,221
  10,000,000    102,272,662
 100,000,000  1,022,727,208
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Self numbers**](https://rosettacode.org/wiki/Self_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Self numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Self_numbers?action=history).*
