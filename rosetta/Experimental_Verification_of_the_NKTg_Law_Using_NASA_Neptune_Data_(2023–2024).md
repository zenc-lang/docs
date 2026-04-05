+++
title = "Experimental Verification of the NKTg Law Using NASA Neptune Data (2023–2024)"
+++

# Experimental Verification of the NKTg Law Using NASA Neptune Data (2023–2024)

{{trans|Q#}}

```zc
import "std/math.zc"

fn compute_nktg(x: f64, v: f64, m: f64, dm_dt: f64) {
    let p = m * v;
    let nktg1 = x * p;
    let nktg2 = dm_dt * p;
    let nktg  = Math::sqrt(nktg1 * nktg1 + nktg2 * nktg2);

    println "--------------------------------------------";
    println "Position (x)         : {x:0.0f}";
    println "Velocity (v)         : {v:0.2f}";
    println "Mass (m)             : {m:0.0f}";
    println "Momentum (p = m * v) : {p:0.0f}";
    println "NKTg1 = x * p        : {nktg1:0.0f}";
    println "NKTg2 = dm_dt * p    : {nktg2:0.0f}";
    println "Total NKTg           : {nktg:0.0f}";
}

fn main() {
    println "============================================";
    println "NKTg Law - Neptune 2023 NASA Data";
    println "============================================";

    // 2023 NASA Data (Neptune)
    let dm_dt = -0.00002000;

    let data2023: (f64, f64, f64)[5] = [
        [4498396440.0, 5.43, 1.02430000e26],
        [4503443661.0, 5.43, 1.02429980e26],
        [4553946490.0, 5.43, 1.02429960e26],
        [4503443661.0, 5.43, 1.02429940e26],
        [4498396440.0, 5.43, 1.02429920e26]
    ];

    for e in data2023 {
        let (x, v, m) = e;
        compute_nktg(x, v, m, dm_dt);
    }

    println "\n============================================";
    println "NKTg Law - Neptune 2024 Simulation";
    println "============================================";

    let data2024: (f64, f64, f64)[5] = [ 
        (4498396440.0, 5.43, 1.02429900e26),
        (4503443661.0, 5.43, 1.02429880e26),
        (4553946490.0, 5.43, 1.02429860e26),
        (4503443661.0, 5.43, 1.02429840e26),
        (4498396440.0, 5.43, 1.02429820e26)
    ];

    for e in data2024 {
        let (x, v, m) = e;
        compute_nktg(x, v, m, dm_dt);
    }

    println "\n============================================";
    println "Experiment Completed";
    println "============================================";
}
```

**Output:**

```

############################################ NKTg Law - Neptune 2023 NASA Data

--------------------------------------------
Position (x)         : 4498396440
Velocity (v)         : 5.43
Mass (m)             : 102430000000000008208252928
Momentum (p = m * v) : 556194900000000047834988544
NKTg1 = x * p        : 2501985158106156083146661858719563776
NKTg2 = dm_dt * p    : -11123898000000002555904
Total NKTg           : 2501985158106156083146661858719563776
--------------------------------------------
Position (x)         : 4503443661
Velocity (v)         : 5.43
Mass (m)             : 102429979999999995655749632
Momentum (p = m * v) : 556194791399999965415604224
NKTg1 = x * p        : 2504791907611547214820196617625272320
NKTg2 = dm_dt * p    : -11123895827999999655936
Total NKTg           : 2504791907611547214820196617625272320
--------------------------------------------
Position (x)         : 4553946490
Velocity (v)         : 5.43
Mass (m)             : 102429960000000000283115520
Momentum (p = m * v) : 556194682799999951715696640
NKTg1 = x * p        : 2532880823493723022518856423204454400
NKTg2 = dm_dt * p    : -11123893656000000950272
Total NKTg           : 2532880823493723022518856423204454400
--------------------------------------------
Position (x)         : 4503443661
Velocity (v)         : 5.43
Mass (m)             : 102429940000000004910481408
Momentum (p = m * v) : 556194574200000006735265792
NKTg1 = x * p        : 2504790929463584156593795259823030272
NKTg2 = dm_dt * p    : -11123891484000000147456
Total NKTg           : 2504790929463584156593795259823030272
--------------------------------------------
Position (x)         : 4498396440
Velocity (v)         : 5.43
Mass (m)             : 102429919999999992357978112
Momentum (p = m * v) : 556194465599999924315881472
NKTg1 = x * p        : 2501983204002742083276785197042892800
NKTg2 = dm_dt * p    : -11123889311999999344640
Total NKTg           : 2501983204002742083276785197042892800

############################################ NKTg Law - Neptune 2024 Simulation

--------------------------------------------
Position (x)         : 4498396440
Velocity (v)         : 5.43
Mass (m)             : 102429899999999996985344000
Momentum (p = m * v) : 556194356999999979335450624
NKTg1 = x * p        : 2501982715476888878457221210976550912
NKTg2 = dm_dt * p    : -11123887140000000638976
Total NKTg           : 2501982715476888878457221210976550912
--------------------------------------------
Position (x)         : 4503443661
Velocity (v)         : 5.43
Mass (m)             : 102429880000000001612709888
Momentum (p = m * v) : 556194248399999965635543040
NKTg1 = x * p        : 2504789462241639274106288043766841344
NKTg2 = dm_dt * p    : -11123884967999999836160
Total NKTg           : 2504789462241639274106288043766841344
--------------------------------------------
Position (x)         : 4553946490
Velocity (v)         : 5.43
Mass (m)             : 102429860000000006240075776
Momentum (p = m * v) : 556194139800000020655112192
NKTg1 = x * p        : 2532878350700779383730369029335941120
NKTg2 = dm_dt * p    : -11123882796000001130496
Total NKTg           : 2532878350700779383730369029335941120
--------------------------------------------
Position (x)         : 4503443661
Velocity (v)         : 5.43
Mass (m)             : 102429839999999993687572480
Momentum (p = m * v) : 556194031199999938235727872
NKTg1 = x * p        : 2504788484093675920731981506611773440
NKTg2 = dm_dt * p    : -11123880624000000327680
Total NKTg           : 2504788484093675920731981506611773440
--------------------------------------------
Position (x)         : 4498396440
Velocity (v)         : 5.43
Mass (m)             : 102429819999999998314938368
Momentum (p = m * v) : 556193922599999993255297024
NKTg1 = x * p        : 2501980761373475468883154908005531648
NKTg2 = dm_dt * p    : -11123878452000001622016
Total NKTg           : 2501980761373475468883154908005531648

############################################ Experiment Completed

```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Experimental Verification of the NKTg Law Using NASA Neptune Data (2023–2024)**](https://rosettacode.org/wiki/Experimental_Verification_of_the_NKTg_Law_Using_NASA_Neptune_Data_(2023–2024)) in Zen C.

*This article uses material from the Rosetta Code article **Experimental Verification of the NKTg Law Using NASA Neptune Data (2023–2024)**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Experimental_Verification_of_the_NKTg_Law_Using_NASA_Neptune_Data_(2023–2024)?action=history).*
