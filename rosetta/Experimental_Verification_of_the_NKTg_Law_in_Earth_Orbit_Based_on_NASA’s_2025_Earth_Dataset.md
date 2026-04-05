+++
title = "Experimental Verification of the NKTg Law in Earth Orbit Based on NASA’s 2025 Earth Dataset"
+++

# Experimental Verification of the NKTg Law in Earth Orbit Based on NASA’s 2025 Earth Dataset

{{trans|Rust}}

```zc
def DM_DT = -1.8; // kg/s

struct OrbitalData {
    date: string;
    x: f64;
    v: f64;
    m: f64;
}

fn new_od(date: string, x: f64, v: f64, m: f64) -> OrbitalData {
    return OrbitalData { date: date, x: x, v: v, m: m };
}
        
struct ResultRow {
    date:   string;
    p:      f64;
    nktg1:  f64;
    nktg2:  f64;
    v_sim:  f64;
    v_nasa: f64;
    error:  f64;
}

impl ResultRow {
    fn display(self) -> void {
        println "{.date:-12s} {.p:14.3e} {.nktg1:14.3e} {.nktg2:14.3e} {.v_sim:12.3e} {.v_nasa:12.3e} {.error:10.4f}%";
    }
}

fn momentum(m: f64, v: f64) -> f64 {
    return m * v;
}

fn nktg1(x: f64, p: f64) -> f64 {
    return x * p;
}

fn nktg2(p: f64) -> f64 {
    return DM_DT * p;
}

fn relative_error(sim: f64, nasa: f64) -> f64 {
    return (sim - nasa) / nasa * 100.0;
}

fn main() {
    // Simulated NKTg 2025 dataset
    let sim_2025: OrbitalData[5] = [
        new_od("01/01/2025", 1.471012e11, 3.0276e4, 5.97219e24),
        new_od("04/01/2025", 1.494953e11, 2.9791e4, 5.97218999999998e24),
        new_od("07/01/2025", 1.520965e11, 2.9282e4, 5.97218999999997e24),
        new_od("10/01/2025", 1.496328e11, 2.9764e4, 5.97218999999995e24),
        new_od("12/31/2025", 1.471025e11, 3.0276e4, 5.97218999999994e24)
    ];

    // NASA observed velocities
    let nasa_2025: (string, f64)[5] = [
        ("01/01/2025", 3.0287e4),
        ("04/01/2025", 2.9791e4),
        ("07/01/2025", 2.9291e4),
        ("10/01/2025", 2.9778e4),
        ("12/31/2025", 3.0286e4)
    ];

    println "\nExperimental Verification of NKTg Law (Earth 2025)\n";

    println "Date            Momentum(p)          NKTg1          NKTg2        v_sim       v_NASA      Error";
    println "-----------------------------------------------------------------------------------------------";

    for i, data in sim_2025 {
        let p      = momentum(data.m, data.v);
        let n1     = nktg1(data.x, p);
        let n2     = nktg2(p);
        let v_nasa = nasa_2025[i].1;
        let error  = relative_error(data.v, v_nasa);

        let row = ResultRow {
            date  : data.date,
            p     : p,
            nktg1 : n1,
            nktg2 : n2,
            v_sim : data.v,
            v_nasa: v_nasa,
            error : error
        };
        row.display();
    }
}
```

**Output:**

```
Experimental Verification of NKTg Law (Earth 2025)

Date            Momentum(p)          NKTg1          NKTg2        v_sim       v_NASA      Error
-----------------------------------------------------------------------------------------------
01/01/2025        1.808e+29      2.660e+40     -3.255e+29    3.028e+04    3.029e+04    -0.0363%
04/01/2025        1.779e+29      2.660e+40     -3.203e+29    2.979e+04    2.979e+04     0.0000%
07/01/2025        1.749e+29      2.660e+40     -3.148e+29    2.928e+04    2.929e+04    -0.0307%
10/01/2025        1.778e+29      2.660e+40     -3.200e+29    2.976e+04    2.978e+04    -0.0470%
12/31/2025        1.808e+29      2.660e+40     -3.255e+29    3.028e+04    3.029e+04    -0.0330%
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Experimental Verification of the NKTg Law in Earth Orbit Based on NASA’s 2025 Earth Dataset**](https://rosettacode.org/wiki/Experimental_Verification_of_the_NKTg_Law_in_Earth_Orbit_Based_on_NASA’s_2025_Earth_Dataset) in Zen C.

*This article uses material from the Rosetta Code article **Experimental Verification of the NKTg Law in Earth Orbit Based on NASA’s 2025 Earth Dataset**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Experimental_Verification_of_the_NKTg_Law_in_Earth_Orbit_Based_on_NASA’s_2025_Earth_Dataset?action=history).*
