+++
title = "Towers of Hanoi"
+++

# Towers of Hanoi

```zc
fn hanoi(disk: int, from: string, to: string, via: string, pmoves: int*) {
    if disk > 0 {
        hanoi(disk - 1, from, via, to, pmoves);
        *pmoves += 1;
        println "Move disk {disk} from {from} to {to}";
        hanoi(disk - 1, via, to, from, pmoves);
    }
}

fn main() {
    let disks = [3, 4];
    for disk in disks {
        println "Towers of Hanoi with {disk} disks:\n";
        let moves = 0;
        hanoi(disk, "L", "C", "R", &moves);
        println "\nCompleted in {moves} moves.\n";
    }
}
```

**Output:**

```
Towers of Hanoi with 3 disks:

Move disk 1 from L to C
Move disk 2 from L to R
Move disk 1 from C to R
Move disk 3 from L to C
Move disk 1 from R to L
Move disk 2 from R to C
Move disk 1 from L to C

Completed in 7 moves.

Towers of Hanoi with 4 disks:

Move disk 1 from L to R
Move disk 2 from L to C
Move disk 1 from R to C
Move disk 3 from L to R
Move disk 1 from C to L
Move disk 2 from C to R
Move disk 1 from L to R
Move disk 4 from L to C
Move disk 1 from R to C
Move disk 2 from R to L
Move disk 1 from C to L
Move disk 3 from R to C
Move disk 1 from L to R
Move disk 2 from L to C
Move disk 1 from R to C

Completed in 15 moves.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Towers of Hanoi**](https://rosettacode.org/wiki/Towers_of_Hanoi) in Zen C.

*This article uses material from the Rosetta Code article **Towers of Hanoi**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Towers_of_Hanoi?action=history).*
