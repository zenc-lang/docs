+++
title = "Bell numbers"
+++

# Bell numbers

```zc
import "std/bigint.zc"

fn main() {
    let a: BigInt[51];
    let bells: BigInt[51];
    
    a[0] = BigInt::from_int(1);
    bells[0] = BigInt::from_int(1);
    for i in 1..=50 {
        a[i] = BigInt::new();
        bells[i] = BigInt::new();
    }
    
    println "First 10 rows of the Bell Triangle\n1";
    
    for i in 1..=50 {
        let prev = (&a[0]).clone();
        a[0] = (&a[i - 1]).clone();
        bells[i] = (&a[0]).clone();
        
        let pr = i < 10;
        if pr { print "{a[0]} "; }
        
        for j in 1..=i {
            let next_val = (&a[j]).clone();
            a[j] = prev + &a[j-1];
            prev = next_val;
            
            if pr { print "{a[j]} "; }
        }
        if pr { println ""; }
    }
    
    println "\nFirst 15 Bell Numbers";
    for i in 0..15 { println "B({i}) = {bells[i]}"; }
    
    println "\n50th Bell Number";
    println "B(50) = {bells[50]}";
}
```

**Output:**

```
First 10 rows of the Bell Triangle
1
1 2 
2 3 5 
5 7 10 15 
15 20 27 37 52 
52 67 87 114 151 203 
203 255 322 409 523 674 877 
877 1080 1335 1657 2066 2589 3263 4140 
4140 5017 6097 7432 9089 11155 13744 17007 21147 
21147 25287 30304 36401 43833 52922 64077 77821 94828 115975 

First 15 Bell Numbers
B(0) = 1
B(1) = 1
B(2) = 2
B(3) = 5
B(4) = 15
B(5) = 52
B(6) = 203
B(7) = 877
B(8) = 4140
B(9) = 21147
B(10) = 115975
B(11) = 678570
B(12) = 4213597
B(13) = 27644437
B(14) = 190899322

50th Bell Number
B(50) = 185724268771078270438257767181908917499221852770
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Bell numbers**](https://rosettacode.org/wiki/Bell_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Bell numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Bell_numbers?action=history).*
