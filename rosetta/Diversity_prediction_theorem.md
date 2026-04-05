+++
title = "Diversity prediction theorem"
+++

# Diversity prediction theorem

{{trans|Go}}

```zc
fn average_square_diff(f: f64, preds: f64*, size: usize) -> f64 {
    let sum = 0.0;
    for i in 0..<size {
        sum += (preds[i] - f) * (preds[i] - f);
    }
    return sum / size;
}

fn diversity_theorem(truth: f64, preds: f64*, size: usize) -> (f64, f64, f64) {
    let sum = 0.0;
    for i in 0..<size {
        sum += preds[i];
    }
    let av = sum / size;
    let av_err = average_square_diff(truth, preds, size);
    let crowd_err = (truth - av) * (truth - av);
    let div = average_square_diff(av, preds, size);
    let res = (av_err, crowd_err, div);
    return res;
}

fn main() {
    let truth = 49.0;
    let a1: f64[3] = [48.0, 47.0, 51.0];
    let a2: f64[4] = [48.0, 47.0, 51.0, 42.0];
    let res: (f64, f64, f64)[2];
    res[0] = diversity_theorem(truth, a1, 3);
    res[1] = diversity_theorem(truth, a2, 4);
    for r in res {
        let (ae, ce, div) = r;
        println "Average-error {ae:6.3f}";
        println "Crowd-error   {ce:6.3f}";
        println "Diversity     {div:6.3f}\n";
    }
}
```

**Output:**

```
Average-error  3.000
Crowd-error    0.111
Diversity      2.889

Average-error 14.500
Crowd-error    4.000
Diversity     10.500
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Diversity prediction theorem**](https://rosettacode.org/wiki/Diversity_prediction_theorem) in Zen C.

*This article uses material from the Rosetta Code article **Diversity prediction theorem**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Diversity_prediction_theorem?action=history).*
