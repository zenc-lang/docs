+++
title = "Leonardo numbers"
+++

# Leonardo numbers

```zc
fn leonardo(first: (int, int), leo: int*, add: const int, limit: const int) {
    leo[0] = first.0;
    leo[1] = first.1;
    for i in 2..limit { leo[i] = leo[i-1] + leo[i-2] + add; }
}

fn main() {
    def LIMIT = 25;
    let leo: [int; LIMIT];
    println "The first {LIMIT} Leonardo numbers with L(0) = 1, L(1) = 1 and Add = 1 are:";
    leonardo((1, 1), (int*)leo, 1, LIMIT);
    for l in leo { print "{l} "}
    println "\n\nThe first {LIMIT} Leonardo numbers with L(0) = 0, L(1) = 1 and Add = 0 are:";
    for i in 0..LIMIT { leo[i] = 0; }
    leonardo((0, 1), (int*)leo, 0, LIMIT);
    for l in leo { print "{l} "}
    println "";
}
```

**Output:**

```
The first 25 Leonardo numbers with L(0) = 1, L(1) = 1 and Add = 1 are:
1 1 3 5 9 15 25 41 67 109 177 287 465 753 1219 1973 3193 5167 8361 13529 21891 35421 57313 92735 150049 

The first 25 Leonardo numbers with L(0) = 0, L(1) = 1 and Add = 0 are:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Leonardo numbers**](https://rosettacode.org/wiki/Leonardo_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Leonardo numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Leonardo_numbers?action=history).*
