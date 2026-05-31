+++
title = "Arithmetic/Complex"
+++

# Arithmetic/Complex

```zc
import "std/complex.zc"
import "std/string.zc"

fn negate(c: Complex) -> Complex {
    return Complex{real: -c.real, imag: -c.imag};
}

fn inverse(c: Complex) -> Complex {
    return Complex::new(1, 0) / c;
}

fn conjugate(c: Complex) -> Complex {
    return Complex{real: c.real, imag: -c.imag};
}

fn cstr(c: Complex) -> String {
    let rsign = c.real < 0 ? "-" : " ";
    let isign = c.imag < 0 ? "-" : "+";
    let s = "{rsign}{fabs(c.real):g} {isign} {fabs(c.imag):g}i";
    return String::from(s);
}

fn main() {
    let x = Complex::new(1.0, 3.0);
    let y = Complex::new(5.0, 2.0);
    println "x     =  {cstr(x)}";
    println "y     =  {cstr(y)}";
    println "x + y =  {cstr(x + y)}";
    println "x - y =  {cstr(x - y)}";
    println "x * y =  {cstr(x * y)}";
    println "x / y =  {cstr(x / y)}";
    println "-x    =  {cstr(negate(x))}";
    println "1 / x =  {cstr(inverse(x))}";
    println "x*    =  {cstr(conjugate(x))}";
}
```

**Output:**

```
x     =   1 + 3i
y     =   5 + 2i
x + y =   6 + 5i
x - y =  -4 + 1i
x * y =  -1 + 17i
x / y =   0.37931 + 0.448276i
-x    =  -1 - 3i
1 / x =   0.1 - 0.3i
x*    =   1 - 3i
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Arithmetic/Complex**](https://rosettacode.org/wiki/Arithmetic/Complex) in Zen C.

*This article uses material from the Rosetta Code article **Arithmetic/Complex**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Arithmetic/Complex?action=history).*
