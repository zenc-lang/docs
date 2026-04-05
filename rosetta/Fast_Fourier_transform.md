+++
title = "Fast Fourier transform"
+++

# Fast Fourier transform

```zc
import "std/complex.zc"
import "std/vec.zc"

fn fft_recursive(input: Vec<Complex>) -> Vec<Complex> {
    let N = input.len;
    
    if N <= 1 {
        let res = Vec<Complex>::with_capacity(1);
        if N == 1 {
            res.push(input.get(0));
        }
        return res;
    }

    let even = Vec<Complex>::with_capacity(N / 2);
    let odd = Vec<Complex>::with_capacity(N / 2);
    
    for let i: usize = 0; i < N; i += 2 {
        even.push(input.get(i));
        if i + 1 < N {
            odd.push(input.get(i + 1));
        }
    }

    let even_fft = fft_recursive(even);
    let odd_fft = fft_recursive(odd);

    let result = Vec<Complex>::with_capacity(N);
    for _i in 0..N {
        result.push(Complex::new(0.0, 0.0));
    }

    let half_N = N / 2;
    for k in 0..half_N {
        let theta = -2.0 * Math::PI() * (double)k / (double)N;
        let twiddle = Complex::new(Math::cos(theta), Math::sin(theta));
        
        let t = twiddle * odd_fft.get(k);
        let e = even_fft.get(k);
        
        result.set(k, e + t);
        result.set(k + half_N, e - t);
    }
    
    return result;
}

fn pad_to_power_of_2(input: Vec<Complex>*) {
    let current_len = input.len;
    let next_power = 1;
    while next_power < current_len {
        next_power *= 2;
    }
    
    for _i in current_len..next_power {
        input.push(Complex::new(0.0, 0.0));
    }
}

fn main() {
    println "=> Fast Fourier Transform (FFT)";
    
    let signal = Vec<Complex>::with_capacity(8);
    for _i in 0..4 {
        signal.push(Complex::new(1.0, 0.0));
    }
    for _i in 4..8 {
        signal.push(Complex::new(0.0, 0.0));
    }

    pad_to_power_of_2(&signal);

    println "Input Signal (len: {signal.len}):";
    let i = 0;
    for val in signal {
        let mag = val.magnitude();
        let s = val.to_string();
        let s_ptr = s.c_str();
        println "\tx[{i}] = {s_ptr}  (Magnitude: {mag})";
        i += 1;
    }
    
    let fft_output = fft_recursive(signal);
    
    println "\nFFT Output:";
    let k = 0;
    for X in fft_output {
        let mag = X.magnitude();
        let s = X.to_string();
        let s_ptr = s.c_str();
        println "\tX[{k}] = {s_ptr}  (Magnitude: {mag})";
        k += 1;
    }
}
```

**Output:**

```
=> Fast Fourier Transform (FFT)
Input Signal (len: 8):
    x[0] = 1.000000 + 0.000000i  (Magnitude: 1.000000)
    x[1] = 1.000000 + 0.000000i  (Magnitude: 1.000000)
    x[2] = 1.000000 + 0.000000i  (Magnitude: 1.000000)
    x[3] = 1.000000 + 0.000000i  (Magnitude: 1.000000)
    x[4] = 0.000000 + 0.000000i  (Magnitude: 0.000000)
    x[5] = 0.000000 + 0.000000i  (Magnitude: 0.000000)
    x[6] = 0.000000 + 0.000000i  (Magnitude: 0.000000)
    x[7] = 0.000000 + 0.000000i  (Magnitude: 0.000000)

FFT Output:
    X[0] = 4.000000 + 0.000000i  (Magnitude: 4.000000)
    X[1] = 1.000000 - 2.414213i  (Magnitude: 2.613126)
    X[2] = 0.000000 + 0.000000i  (Magnitude: 0.000000)
    X[3] = 1.000000 - 0.414214i  (Magnitude: 1.082392)
    X[4] = 0.000000 + 0.000000i  (Magnitude: 0.000000)
    X[5] = 1.000000 + 0.414213i  (Magnitude: 1.082392)
    X[6] = 0.000000 + 0.000000i  (Magnitude: 0.000000)
    X[7] = 1.000001 + 2.414214i  (Magnitude: 2.613126)
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Fast Fourier transform**](https://rosettacode.org/wiki/Fast_Fourier_transform) in Zen C.

*This article uses material from the Rosetta Code article **Fast Fourier transform**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Fast_Fourier_transform?action=history).*
