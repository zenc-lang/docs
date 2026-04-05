+++
title = "Ternary logic"
+++

# Ternary logic

```zc
struct Trit {
    val: int; // 0: False, 1: Unknown, 2: True
}

// Struct-based constants participate in operator overloading
let FALSE   = Trit { val: 0 };
let UNKNOWN = Trit { val: 1 };
let TRUE    = Trit { val: 2 };

impl Trit {
    fn new(v: int) -> Trit { return Trit { val: v }; }

    // Maps to the '!' operator
    fn not(self) -> Trit { return Trit { val: 2 - self.val }; }

    // Maps to the '~' operator
    fn bitnot(self) -> Trit { return !self; }

    // Maps to the '&' operator (Kleene AND: min(a, b))
    fn bitand(self, other: Trit) -> Trit {
        let a = self.val;
        let b = other.val;
        return Trit { val: a < b ? a : b };
    }

    // Maps to the '|' operator (Kleene OR: max(a, b))
    fn bitor(self, other: Trit) -> Trit {
        let a = self.val;
        let b = other.val;
        return Trit { val: a > b ? a : b };
    }

    // Maps to the '^' operator
    fn bitxor(self, other: Trit) -> Trit {
        // Kleene XOR logic: (A or B) and not (A and B)
        return (self | other) & !(self & other);
    }

    fn to_string(self) -> char* {
        if self.val == 0 return "F";
        if self.val == 1 return "?";
        return "T";
    }
}

fn main() {
    let vals: Trit[3] = [FALSE, UNKNOWN, TRUE];

    println "Truth Table (Kleene Logic):";
    println "A B | !A | A&B | A|B | A^B";
    println "----+----+-----+-----+----";
    for i in 0..3 {
        for j in 0..3 {
            let a = vals[i];
            let b = vals[j];
            println "{a.to_string()} {b.to_string()} | {(!a).to_string()}  | { (a&b).to_string() }   | { (a|b).to_string() }   | { (a^b).to_string() }";
        }
    }

    println "\nPractical Case: SQL-style Null/Unknown Filtering";
    
    // Evaluation without branching
    let r1 = (TRUE & TRUE) | FALSE;      // Authorized
    let r2 = (FALSE & UNKNOWN) | FALSE;  // Denied
    let r3 = (TRUE & UNKNOWN) | FALSE;   // Manual Review (?)
    let r4 = (UNKNOWN & FALSE) | TRUE;   // Authorized (Emergency override)

    let results: Trit[4] = [r1, r2, r3, r4];

    for i in 0..4 {
        let r = results[i];
        print "Result {i+1}: {r.to_string()} -> ";
        if r.val == 2 println "Authorized";
        else if r.val == 1 println "Manual Review Required";
        else println "Denied";
    }
}
```

**Output:**

```
Truth Table (Kleene Logic):
A B | !A | A&B | A|B | A^B
----+----+-----+-----+----
F F | T  | F   | F   | F
F ? | T  | F   | ?   | ?
F T | T  | F   | T   | T
? F | ?  | F   | ?   | ?
? ? | ?  | ?   | ?   | ?
? T | ?  | ?   | T   | ?
T F | F  | F   | T   | T
T ? | F  | ?   | T   | ?
T T | F  | T   | T   | F

Practical Case: SQL-style Null/Unknown Filtering
Result 1: T -> Authorized
Result 2: F -> Denied
Result 3: ? -> Manual Review Required
Result 4: T -> Authorized
```

{{omit from|GUISS}}

---
**Attribution:** This is a community solution for the Rosetta Code task [**Ternary logic**](https://rosettacode.org/wiki/Ternary_logic) in Zen C.

*This article uses material from the Rosetta Code article **Ternary logic**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Ternary_logic?action=history).*
