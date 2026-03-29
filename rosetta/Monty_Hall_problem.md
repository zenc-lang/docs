+++
title = "Monty Hall problem"
+++

# Monty Hall problem

{{trans|Wren}}

```zc
import "std/random.zc"
import "locale.h";

fn monty_hall(games: int) {
    let rng = Random::new();
    let switch_wins = 0;
    let stay_wins = 0;
    for _ in 1..=games {
        let doors: int[3] = [0, 0, 0];         // all zero (goats) by default
        doors[rng.next_int_range(0, 2)] = 1;   // put car in a random door
        let choice = rng.next_int_range(0, 2); // choose a door at random
        let shown = 0;
        do {
            shown = rng.next_int_range(0, 2);   // the shown door
        } while doors[shown] == 1 || shown == choice;
        stay_wins += doors[choice];
        switch_wins += doors[3 - choice - shown];
    }
    setlocale(LC_NUMERIC, "en_US.UTF-8");
    println "Simulating {games:'d} games:";
    println "Staying   wins {stay_wins:'d} times";
    println "Switching wins {switch_wins:'d} times";
}

fn main() {
    monty_hall(1_000_000);
}
```

**Output:**

Sample output:

```
Simulating 1,000,000 games:
Staying   wins 333,496 times
Switching wins 666,504 times
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Monty Hall problem**](https://rosettacode.org/wiki/Monty_Hall_problem) in Zen C.

*This article uses material from the Rosetta Code article **Monty Hall problem**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Monty_Hall_problem?action=history).*
