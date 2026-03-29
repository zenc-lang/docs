+++
title = "Finite state machine"
+++

# Finite state machine

{{trans|Wren}}

```zc
import "ctype.h"

def READY     = 0;
def WAITING   = 1;
def EXIT      = 2;
def DISPENSE  = 3;
def REFUNDING = 4;

fn fsm() {
    println "Please enter your option when prompted";
    println "(any characters after the first will be ignored)";
    let state = READY;
    let input: char[10];
    let trans: int;
    loop {
        match state {
            READY => {
                do {
                    ? "\n(D)ispense or (Q)uit : " (input);
                    trans = tolower(input[0]);
                } while trans != 'd' && trans != 'q';
                state = (trans == 'd') ? WAITING : EXIT;
            },
            WAITING => {
                println "OK, put your money in the slot";
                do {
                    ? "(S)elect product or choose a (R)efund : " (input);
                    trans = tolower(input[0]);
                } while trans != 's' && trans != 'r';
                state = (trans == 's') ? DISPENSE : REFUNDING ;
            },
            DISPENSE => {
                do {
                    ? "(R)emove product : " (input);
                    trans = tolower(input[0]);
                } while trans != 'r' ;
                state = READY;
            },
            REFUNDING => {
                // No transitions defined.
                println "OK, refunding your money";
                state = READY;
            },
            EXIT => {
                println "OK, quitting";
                return;
            }
        }
    }
}

fn main() {
    fsm();
}
```

**Output:**

Sample session:

```
Please enter your option when prompted
(any characters after the first will be ignored)

(D)ispense or (Q)uit : d
OK, put your money in the slot
(S)elect product or choose a (R)efund : s
(R)emove product : r

(D)ispense or (Q)uit : d
OK, put your money in the slot
(S)elect product or choose a (R)efund : r
OK, refunding your money

(D)ispense or (Q)uit : q
OK, quitting
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Finite state machine**](https://rosettacode.org/wiki/Finite_state_machine) in Zen C.

*This article uses material from the Rosetta Code article **Finite state machine**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Finite_state_machine?action=history).*
