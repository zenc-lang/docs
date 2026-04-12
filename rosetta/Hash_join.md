+++
title = "Hash join"
+++

# Hash join

```zc
import "std/map.zc"
import "std/vec.zc"

struct A {
    age : int;
    name: string;
}

struct B {
    character: string;
    nemesis  : string;
}

fn main() {
    let tableA = [
        A{age: 27, name: "Jonah"}, A{age: 18, name: "Alan"},
        A{age: 28, name: "Glory"}, A{age: 18, name: "Popeye"},
        A{age: 28, name: "Alan"}
    ];

    let tableB = [
        B{character: "Jonah", nemesis: "Whales"},
        B{character: "Jonah", nemesis: "Spiders"},
        B{character: "Alan",  nemesis: "Ghosts"},
        B{character: "Alan",  nemesis: "Zombies"},
        B{character: "Glory", nemesis: "Buffy"}
    ];

    let h = Map<Vec<int>>::new();
    for i in 0..tableA.len {
        let a = tableA[i];
        let vec = h.contains(a.name) ? h[a.name].unwrap() : Vec<int>::new();
        vec.push(i);
        h.put(a.name, vec);
    }

    println "Age  Name   Character Nemesis";
    println "---  -----  --------- -------";
    for i in 0..tableB.len {
        let b = tableB[i];
        if h.contains(b.character) {
            let c = h[b.character].unwrap();
            let f = "%3d  %-5s  %-9s %s\n";
            for j in c {
                let t = tableA[j];
                printf(f, t.age, t.name, b.character, b.nemesis);
            }
        }
    }
}
```

**Output:**

```
Age  Name   Character Nemesis
---  -----  --------- -------
 27  Jonah  Jonah     Whales
 27  Jonah  Jonah     Spiders
 18  Alan   Alan      Ghosts
 28  Alan   Alan      Ghosts
 18  Alan   Alan      Zombies
 28  Alan   Alan      Zombies
 28  Glory  Glory     Buffy
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Hash join**](https://rosettacode.org/wiki/Hash_join) in Zen C.

*This article uses material from the Rosetta Code article **Hash join**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Hash_join?action=history).*
