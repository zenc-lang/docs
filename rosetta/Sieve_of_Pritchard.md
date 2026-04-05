+++
title = "Sieve of Pritchard"
+++

# Sieve of Pritchard

```zc
import "std/vec.zc"

fn sieve_of_pritchard(limit: usize) -> Vec<int> {
    let s = Vec<bool>::new();
    s.grow_to_fit(limit + 1);
    for i in 0..=limit {
        s << false;
    }
    s.set(1, true);
    
    let primes = Vec<int>::new();
    let pr: usize = 1;
    let p: usize = 2;
    
    while p * p <= limit {
        let pr_next = pr * p;
        
        if pr_next <= limit {
            for k in 1..p {
                for w in 1..=pr {
                    if s.get(w) {
                        s.set(w + k * pr, true);
                    }
                }
            }
            pr = pr_next;
        } else {
            for w in 1..=pr {
                if s.get(w) {
                    let mut_k = 1;
                    let current_pos = w + mut_k * pr;
                    while current_pos <= limit {
                        s.set(current_pos, true);
                        mut_k = mut_k + 1;
                        current_pos = w + mut_k * pr;
                    }
                }
            }
            pr = limit;
        }
        
        for w in (pr / p)..=1 step -1 {
            if s.get(w) {
                s.set(w * p, false);
            }
        }
        
        primes << (int)p;
        
        let next_p = p + 1;
        while next_p <= limit {
            let rem = next_p % pr;
            let wheel_pos = (rem == 0) ? pr : rem;
            if s.get(wheel_pos) {
                break;
            }
            next_p = next_p + 1;
        }
        p = next_p;
    }
    
    if pr < limit {
        for w in 1..=pr {
            if s.get(w) {
                let mut_k = 1;
                let current_pos = w + mut_k * pr;
                while current_pos <= limit {
                    s.set(current_pos, true);
                    mut_k = mut_k + 1;
                    current_pos = w + mut_k * pr;
                }
            }
        }
    }
    
    for i in 2..=limit {
        if s.get(i) {
            primes << (int)i;
        }
    }
    
    return primes;
}

fn main() {
    let limit: usize = 150;
    let primes = sieve_of_pritchard(limit);
    
    print "Primes up to {limit}: [";
    for i in 0..primes.len {
        print "{primes[i]}";
        if i < primes.len - 1 {
            print ", ";
        }
    }
    println "]";
    println "Total primes found: {primes.len}";
}
```

**Output:**

```
Primes up to 150: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
Total primes found: 35
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sieve of Pritchard**](https://rosettacode.org/wiki/Sieve_of_Pritchard) in Zen C.

*This article uses material from the Rosetta Code article **Sieve of Pritchard**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sieve_of_Pritchard?action=history).*
