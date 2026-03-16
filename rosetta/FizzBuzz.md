+++
title = "FizzBuzz"
+++

# FizzBuzz

Zen C offers multiple ways to solve FizzBuzz. Here are two approaches: one using standard <code>if/else</code> statements and another using the <code>match</code> control flow feature.

### Using if/else

This approach demonstrates Zen C's inclusive range loops (<code>..=</code>), basic modulo arithmetic, and implicit string interpolation.

```zc
fn main() {
    for i in 1..=100 {
        if i % 15 == 0 {
            println "FizzBuzz";
        } else if i % 3 == 0 {
            println "Fizz";
        } else if i % 5 == 0 {
            println "Buzz";
        } else {
            println "{i}";
        }
    }
}
```

### Using match

This implementation utilizes the <code>match</code> statement, which serves as a powerful alternative to <code>switch</code>. It supports multiple value matching on a single branch using commas, and includes a catch-all wildcard (<code>_</code>).

```zc
fn main() {
    for i in 1..=100 {
        match i % 15 {
            0           => { println "FizzBuzz" },
            3, 6, 9, 12 => { println "Fizz" },
            5, 10       => { println "Buzz" },
            _           => { println "{i}" },
        }
    }
}
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**FizzBuzz**](https://rosettacode.org/wiki/FizzBuzz) in Zen C.

*This article uses material from the Rosetta Code article **FizzBuzz**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/FizzBuzz?action=history).*
