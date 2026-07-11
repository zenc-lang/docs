+++
title = "Composition"
weight = 20
+++

# Composition with `use`

Mixin composition (unnamed, fields flattened) and named composition
(nested field access).

## Zen C

```zc
import "std/io.zc"

struct Position {
    x: int;
    y: int;
}

struct Health {
    hp: int;
    max_hp: int;
}

struct Player {
    use Position;
    use stats: Health;
    name: string;
}

fn main() {
    let p = Player {
        x: 10, y: 20,
        stats: Health { hp: 80, max_hp: 100 },
        name: "Zen",
    };

    println "position: ({p.x}, {p.y})";
    println "hp: {p.stats.hp}/{p.stats.max_hp}";
    println "name: {p.name}";
}
```

## C

```c
#include <stdio.h>

typedef struct {
    int x;
    int y;
} Position;

typedef struct {
    int hp;
    int max_hp;
} Health;

typedef struct {
    Position pos;
    Health stats;
    const char* name;
} Player;

int main(void) {
    Player p = {
        {10, 20},
        {80, 100},
        "C"
    };

    printf("position: (%d, %d)\n", p.pos.x, p.pos.y);
    printf("hp: %d/%d\n", p.stats.hp, p.stats.max_hp);
    printf("name: %s\n", p.name);
    return 0;
}
```

## Key Differences

- Mixin composition: `use Position` flattens fields (access `p.x` directly)
- Named composition: `use stats: Health` nests (access `p.stats.hp`)
- C only supports nested structs with named field access
- Mixin avoids `p.pos.x` for deeply nested types
- Both approaches compile to the same C struct layout

## Output

position: (10, 20)
hp: 80/100
name: Zen
