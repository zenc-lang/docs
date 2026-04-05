+++
title = "Command-line arguments"
+++

# Command-line arguments

As in C, the first argument is the name of the program.

```zc
fn main(argc: int, argv: char**) {
    for i in 0..argc {
        println "{argv[i]}";
    }
}
```

**Output:**

```
$ zc build Command-line_arguments.zc
   Compiling Command-line_arguments.zc
    Finished build in 0.04s

$./Command-line_arguments -c "alpha beta" -h "gamma"
./Command-line_arguments
-c
alpha beta
-h
gamma
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Command-line arguments**](https://rosettacode.org/wiki/Command-line_arguments) in Zen C.

*This article uses material from the Rosetta Code article **Command-line arguments**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Command-line_arguments?action=history).*
