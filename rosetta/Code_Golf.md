+++
title = "Code Golf"
+++

# Code Golf

### With Literals

Zen C allows string literals to be evaluated as statements to print them to standard output. By appending the <code>..</code> operator, the implicit trailing newline is suppressed, emitting exactly the 9 required characters.

```zc
fn main(){"Code Golf"..}
```

Length: 24 bytes.

### Without Literals

This version assumes the compiled executable is renamed to <code>Code Golf</code> and executed via <code>./Code Golf</code>. It uses the program's own execution path in <code>argv[0]</code>, offsets the pointer by 2 to skip the <code>./</code> prefix, and uses the POSIX <code>write</code> function to emit exactly 9 bytes to stdout (file descriptor 1). Omitting the explicit declaration for <code>write</code> triggers a compiler warning but saves bytes.

```zc
fn main(argc:int,argv:char**){write(1,argv[0]+2,9)}
```

Length: 51 bytes.

### Executable Size

A standard build produces an executable of around **17KB**. However, when the binary is stripped and compiled using the Tiny C Compiler (TCC) backend, the footprint can be reduced to just **8.6KB**.

---
**Attribution:** This is a community solution for the Rosetta Code task [**Code Golf**](https://rosettacode.org/wiki/Code_Golf) in Zen C.

*This article uses material from the Rosetta Code article **Code Golf**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Code_Golf?action=history).*
