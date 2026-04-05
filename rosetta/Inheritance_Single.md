+++
title = "Inheritance/Single"
+++

# Inheritance/Single

Zen C does not have classes but does have structs and traits.

Structs can implement methods and traits enable behavior to be shared between structs.

The language doesn't have inheritance as such but instead uses composition to embed other structs.

In the following code, the Dog and Cat structs both implement the Animal trait and the Lab and Collie structs embed the Dog struct in a way which enables them to call its methods.

```zc
trait Animal {
    fn make_noise(self);
}

struct Dog { name: string; }

impl Animal for Dog {
    fn make_noise(self) { println "{.name} says, woof!"; }
}

struct Cat { name: string; }

impl Animal for Cat {
    fn make_noise(self) { println "{.name} says, meow!" }
}

struct Lab { use dog: Dog; }

struct Collie { use dog: Dog; }

fn main() {
    let prince = Lab{dog: Dog{name: "Prince"}};
    prince.dog.make_noise();

    let lassie = Collie{dog: Dog{name: "Lassie"}};
    lassie.dog.make_noise();

    let fluffy = Cat{name: "Fluffy"};
    fluffy.make_noise();
}
```

**Output:**

```
Prince says, woof!
Lassie says, woof!
Fluffy says, meow!
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Inheritance/Single**](https://rosettacode.org/wiki/Inheritance/Single) in Zen C.

*This article uses material from the Rosetta Code article **Inheritance/Single**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Inheritance/Single?action=history).*
