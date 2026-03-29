+++
title = "Guess the number"
+++

# Guess the number

```zc
import "std/random.zc"

fn main() {
    let rng = Random::new();
    let comp = rng.next_int_range(1, 10); // computer number
    let attempt = 0
    let guess: int
    do {
        ? "Your guess 1 to 10 : " (guess);
        attempt++;
    } while comp != guess;
    println "\nYou guessed correctly after {attempt} attempt(s)!";
}
```

**Output:**

Sample run:

```
Your guess 1 to 10 : 3
Your guess 1 to 10 : 8
Your guess 1 to 10 : 5
Your guess 1 to 10 : 2

You guessed correctly after 4 attempt(s)!
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Guess the number**](https://rosettacode.org/wiki/Guess_the_number) in Zen C.

*This article uses material from the Rosetta Code article **Guess the number**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Guess_the_number?action=history).*
