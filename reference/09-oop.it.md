+++
title = "9. Programmazione Orientata a Oggetti"
weight = 9
+++

# 9. Programmazione Orientata a Oggetti


#### Metodi
Definisci metodi sui tipi utilizziando `impl`.
```zc
impl Punto {
    // Metodo statico (convenzione del costruttore)
    fn nuovo(x: int, y: int) -> Self {
        return Point{x: x, y: y};
    }

    // Metodo d'instanza
    fn dist(self) -> float {
        return sqrt(self.x * self.x + self.y * self.y);
    }
}
```

**Scorciatoia di Self**: Nei metodi con un parametro `self`, puoi usare `.campo` come abbreviazione per `self.campo`:
```zc
impl Point {
    fn dist(self) -> float {
        return sqrt(.x * .x + .y * .y);  // Equivalente a self.x, self.y
    }
}
```

#### Métodos primitivos
Zen C permette di definire metodi su tipi primitivi (come `int`, `bool`, etc.) usando la stessa sintassi `impl`.

```zc
impl int {
    fn abs(self) -> int {
        return *self < 0 ? -(*self) : *self;
    }
}

let x = -10;
let y = x.abs(); // 10
let z = (-5).abs(); // 5 (Literals supported)
```

#### Tratti
Definisci un comportamento condiviso.
```zc
struct Cerchio { raggio: f32; }

trait Disegnabile {
    fn disegna(self);
}

impl Disegna for Cerchio {
    fn disegna(self) { ... }
}

let cerchio = Cerchio{};
let disegnabile: Disegnabile = &cerchio;
```

#### Tratti Standard
Zen C include dei tratti standard che si integrano con la sintassi del linguaggio.

**Iterable** (lett. _Iterabile_)

Implementa `Iterable<T>` per abilitare loop `for-in` (lett. _per in_) nei tuoi tipi personalizzati.

```zc
import "std/iter.zc"

// Definisci un Iteratore
struct MioIteratore {
    curr: int;
    stop: int;
}

impl MioIteratore {
    fn next(self) -> Option<int> {
        if self.curr < self.stop {
            self.curr += 1;
            return Option<int>::Some(self.curr - 1);
        }
        return Option<int>::None();
    }
}

// Implementa Iterable
impl MioRange {
    fn iterator(self) -> MioIteratore {
        return MioIteratore{curr: self.start, stop: self.end};
    }
}

// Usalo in un loop
for i in mio_range {
    println "{i}";
}
```

**Drop** (lett. _rilascia_)

Implementa `Drop` per definire un distruttore che esegue quando l'oggetto va fuori ambito (RAII).

```zc
import "std/mem.zc"

struct Risorsa {
    ptr: void*;
}

impl Drop for Risorsa {
    fn drop(self) {
        if self.ptr != NULL {
            free(self.ptr);
        }
    }
}
```

{% alert(type="note") %}
Se una variabile viene spostata, `drop` NON verrà chiamato sulla variabile originale. Aderisce alle [Semantiche delle Risorse](@/tour/08-memory-management.it.md#semantiche-delle-risorse-move-by-default)
{% end %}

**Copy** (lett. _copia_)

Tratto marcatore opt-in per il comportamento `Copy` (duplicazione implicita) al posto delle semantiche Move. Utilizzato tramite `@derive(Copy)`

> **Regola:** I tipi che implementano `Copy` non dovrà definire un distruttore (`Drop`).

```zc
@derive(Copy)
struct Punto { x: int; y: int; }

fn main() {
    let p1 = Punto{x: 1, y: 2};
    let p2 = p1; // Copiato! p1 rimane valido.
}
```

**Clone** (lett. _clona_)

Implementa `Clone` per permettere la duplicazione esplicita di tipi che posseggono risorse.

```zc
import "std/mem.zc"

struct Scatola { val: int; }

impl Clone for Scatola {
    fn clone(self) -> Scatola {
        return Scatola{val: self.val};
    }
}

fn main() {
    let b1 = Scatola{val: 42};
    let b2 = b1.clone(); // Explicit copy
}
```

#### Composizione
Usa `use` per incorporare altri struct. Puoi mischiarli (campi piatti) o nominarli (campi nidificato).

```zc
struct Entità { id: int; }

struct Giocatore {
    // Mischiati (Non nominati): Campi piatti
    use Entità;  // Aggiunge 'id' a 'Giocatore' direttamente
    nome: string;
}

struct Partita {
    // Composizione (Nominati): Campi nidificati
    use p1: Giocatore; // Vi si accede tramite partita.p1
    use p2: Giocatore; // Vi si accede tramite partita.p2
}
```
