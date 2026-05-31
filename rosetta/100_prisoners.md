+++
title = "100 prisoners"
+++

# 100 prisoners

{{trans|Wren}}

```zc
import "std/random.zc"
import "locale.h"

let rng: Random;

fn shuffle(a: int*, len: usize) {
    for let i: usize = len - 1; i >= 1; --i {
        let j = rng.next_int_range(0, (int)i);
        if j != i {
            let t = a[i];
            a[i] = a[j];
            a[j] = t;
        }
    }
}

fn do_trials(trials: int, np: int, strategy: string) {
    let pardoned = 0;
    for t in 0..trials {
        let drawers: [int; 100];
        for i in 0..100 { drawers[i] = i; }
        shuffle((int*)drawers, 100);
        let next_trial = false;
        for p in 0..np {
            let next_prisoner = false;
            if strcmp(strategy, "optimal") == 0 {
                let prev = p;
                for d in 0..50 {
                    let curr = drawers[prev];
                    if curr == p {
                        next_prisoner = true;
                        break;
                    }
                    prev = curr;
                }
            } else {
                let opened: [bool; 100];
                for d in 0..50 {
                    let n: int;
                    loop {
                        n = rng.next_int_range(0, 99);
                        if !opened[n] {
                            opened[n] = true;
                            break;
                        }
                    }
                    if drawers[n] == p {
                        next_prisoner = true;
                        break;
                    }
                }
            }
            if !next_prisoner {
                next_trial = true;
                break;
            }
        }
        if !next_trial { pardoned++; }
    }
    let rf = (f64)pardoned / (f64)trials * 100.0;
    println "  strategy = {strategy:-7s}  pardoned = {pardoned:'6d}  relative frequency = {rf:5.2f}%\n";
}

fn main() {
    rng = Random::new();
    setlocale(LC_NUMERIC, "");
    let trials = 100_000;
    let nps = [10, 100];
    let strategies = ["random", "optimal"];
    for np in nps {
        println "Results from {trials:'d} trials with {np} prisoners:\n";
        for i in 0..strategies.len { do_trials(trials, np, strategies[i]); }
    }
}
```

**Output:**

Sample run:

```
Results from 100,000 trials with 10 prisoners:

  strategy = random   pardoned =    102  relative frequency =  0.10%

  strategy = optimal  pardoned = 31,252  relative frequency = 31.25%

Results from 100,000 trials with 100 prisoners:

  strategy = random   pardoned =      0  relative frequency =  0.00%

  strategy = optimal  pardoned = 31,151  relative frequency = 31.15%
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**100 prisoners**](https://rosettacode.org/wiki/100_prisoners) in Zen C.

*This article uses material from the Rosetta Code article **100 prisoners**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/100_prisoners?action=history).*
