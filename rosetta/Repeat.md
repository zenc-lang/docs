+++
title = "Repeat"
+++

# Repeat

### Standard Closures

```zc
// The procedure accepts a standard closure and an integer
fn times(proc: fn(), n: uint) {
    for _ in 0..n {
        proc();
    }
}

fn main() {
    times(fn() { 
        println "Hello from closure!"; 
    }, 3);
}
```

**Output:**

```
Hello from closure!
Hello from closure!
Hello from closure!
```

### State-Capturing Closures

```zc
// Reusing the 'times' procedure defined above
fn main() {
    let count = 0;
    times(fn[&]() {
        count++;
        println "Iteration {count}";
    }, 5);
}
```

**Output:**

```
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

### Raw Function Pointers

```zc
// The procedure accepts a raw C-style function pointer
fn times_fp(proc: fn*(), n: uint) {
    for _ in 0..n {
        proc();
    }
}

// A standard named function
fn say_hello() {
    println "Hello from function pointer!";
}

fn main() {
    times_fp(say_hello, 2);
}
```

**Output:**

```
Hello from function pointer!
Hello from function pointer!
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Repeat**](https://rosettacode.org/wiki/Repeat) in Zen C.

*This article uses material from the Rosetta Code article **Repeat**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Repeat?action=history).*
