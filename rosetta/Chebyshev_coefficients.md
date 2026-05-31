+++
title = "Chebyshev coefficients"
+++

# Chebyshev coefficients

{{trans|Wren}}

```zc
import "std/math.zc";
import "std/string.zc";

alias cheb_fn = fn*(f64) -> f64;

fn map_range(x: f64, min: f64, max: f64, min_to: f64, max_to: f64) -> f64 {
    return (x - min) / (max - min) * (max_to - min_to) + min_to;
}

fn cheb_coeffs(func: cheb_fn, n: int, min: f64, max: f64, coeffs: f64*) {
    for i in 0..n {
        let ii = (f64)i;
        let nn = (f64)n;
        let f = func(map_range(Math::cos(Math::PI() * (ii + 0.5) / nn), -1.0, 1.0, min, max));
        f = f * 2.0 / nn;
        for j in 0..n {
            let jj = (f64)j;
            coeffs[j] += f * Math::cos(Math::PI() * jj * (ii + 0.5) / nn);
        }
    }
}

fn cheb_approx(x: f64, n: int, min: f64, max: f64, coeffs: f64*) -> f64 {
    assert(n >= 2, "'n' can't be less than 2.";
    let a = 1.0;
    let b = map_range(x, min, max, -1.0, 1.0);
    let res = coeffs[0] / 2.0 + coeffs[1] * b;
    let xx = 2.0 * b;
    for i in 2..n {
        let c = xx * b - a;
        res += coeffs[i] * c;
        a = b;
        b = c;
    }
    return res;
}

fn cheb_func(x: f64)-> f64 { return Math::cos(x); }

fn main() {
    def N = 10;
    let min = 0.0;
    let max = 1.0;
    let coeffs: [f64; N];
    cheb_coeffs(cheb_func, N, min, max, coeffs);
    println "Coefficients:";
    for coeff in coeffs {
        let s = coeff >= 0 ? " ": "";
        println "{s}{coeff:1.14f}";
    }
    println "\nApproximations:\n  x      func(x)    approx       diff";
    for i in 0..=20 {
        let x = map_range((f64)i, 0.0, 20.0, min, max);
        let f = Math::cos(x);
        let approx = cheb_approx(x, N, min, max, coeffs);
        let diff = approx - f;
        let ds = String::from("{diff:g}");
        let len = ds.length();
        let e = ds.substring(len - 4, 4);
        let ds2 = ds.substring(0, len - 5);
        let ds3: String;
        if diff >= 0 {
            ds3 = ds2.substring(0, 4);
            ds3.insert_rune(0, ' ');
        } else {
            ds3 = ds2.substring(0, 5);
        }
        ds3.append(&e);
        println "{x:1.3f}  {f:1.8f} {approx:1.8f}  {ds3}";
    }
}
```

**Output:**

```
Coefficients:
 1.64716947539031
-0.23229937161517
-0.05371511462205
 0.00245823526698
 0.00028211905743
-0.00000772222916
-0.00000058985565
 0.00000001152143
 0.00000000065963
-0.00000000001002

Approximations:
  x      func(x)    approx       diff
0.000  1.00000000 1.00000000   4.68e-13
0.050  0.99875026 0.99875026  -9.35e-14
0.100  0.99500417 0.99500417   4.61e-13
0.150  0.98877108 0.98877108  -4.72e-14
0.200  0.98006658 0.98006658  -4.60e-13
0.250  0.96891242 0.96891242  -2.31e-13
0.300  0.95533649 0.95533649   2.61e-13
0.350  0.93937271 0.93937271   4.61e-13
0.400  0.92106099 0.92106099   1.98e-13
0.450  0.90044710 0.90044710  -2.47e-13
0.500  0.87758256 0.87758256  -4.58e-13
0.550  0.85252452 0.85252452  -2.46e-13
0.600  0.82533561 0.82533561   1.95e-13
0.650  0.79608380 0.79608380   4.52e-13
0.700  0.76484219 0.76484219   2.54e-13
0.750  0.73168887 0.73168887  -2.27e-13
0.800  0.69670671 0.69670671  -4.47e-13
0.850  0.65998315 0.65998315  -4.37e-14
0.900  0.62160997 0.62160997   4.45e-13
0.950  0.58168309 0.58168309  -8.99e-14
1.000  0.54030231 0.54030231   4.47e-13
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Chebyshev coefficients**](https://rosettacode.org/wiki/Chebyshev_coefficients) in Zen C.

*This article uses material from the Rosetta Code article **Chebyshev coefficients**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Chebyshev_coefficients?action=history).*
