+++
title = "3. Tipi Aggregati"
weight = 3
+++

# 3. Tipi Aggregati


#### Array
Array a lunghezza fissa con valori arbitrari.
```zc
def GRANDEZZA = 5;
let interi: int[GRANDEZZA] = [1, 2, 3, 4, 5];
let zeri: [int; GRANDEZZA]; // Inizializzato a zero
```



#### Tuple

Raggruppa più valori in un unico valore composto. Le tuple supportano
arità arbitrarie (2, 3, 4, … fino a 10+), composizione annidata, mutazione
di singoli campi e destrutturazione.

**Uso base**

```zc
let pair = (1, "hello");          // 2-tuple, types inferred
let triple = (1, "hello", 3.14);  // 3-tuple
let five = (1, 2, 3, 4, 5);      // 5-tuple
let typed: (int, string, f64) = (1, "two", 3.0);  // explicit annotation
```

**Accesso ai campi**

Gli elementi sono accessibili posizionalmente con `.0`, `.1`, `.2`, ecc., o tramite
i nomi di campo `.v0`, `.v1`:

```zc
let t = (1, "hello", 3.14);
assert(t.0 == 1);       // positional
assert(t.v1 == "hello"); // raw field name
```

**Valori di ritorno multipli**

Functions can return tuples to provide multiple results:

```zc
fn stats(data: int) -> (int, int) {
    return (data * 2, data + 1);
}

let r = stats(5);
assert(r.0 == 10);
assert(r.1 == 6);
```

**Destrutturazione**

```zc
let (sum, diff) = add_and_subtract(3, 2);
// sum = 5, diff = 1

let (a: string, b: u8) = ("hello", 42);  // typed destructuring
let (x, y: i32) = (1, 2);                // mixed: x inferred, y explicit
```

**Tuple annidate**

```zc
let nested = ((1, 2), (3, 4));
let inner = nested.v0;
assert(inner.v0 == 1);
assert(inner.v1 == 2);
```

**Mutazione**

I singoli campi possono essere riassegnati:

```zc
let t = (1, 2);
t.v0 = 99;
assert(t.v0 == 99);
```

**Confronto di stringhe**

Le tuple con campi `string` devono usare `strcmp()` per il confronto,
non `==` (che confronta i puntatori su `char*`):

```zc
let t = (1, "hello");
assert(strcmp(t.1, "hello") == 0);
```

**Payload di tuple negli enum**

Le varianti enum possono trasportare dati di tupla:

```zc
enum Shape {
    Point,
    Line(int, int),
    Labeled(int, string, f64),
}

match shape {
    Shape::Line(x, y) => { … }
    Shape::Labeled(id, name, val) => { … }
}
```

#### Structs
Strutture dati con campi di bit opzionali.
```zc
struct Punto {
    x: int;
    y: int;
}

// Inizializzazione struct
let p = Punto { x: 10, y: 20 };

// Campi di bit
struct Flags {
    valido: U8 : 1;
    modalità:  U8 : 3;
}
```

{% alert(type="note") %}
Gli struct usano le [Semantiche di Spostamento](@/tour/08-memory-management.it.md#semantiche-delle-risorse-move-by-default) di default. I campi di uno struct possono essere acceduti via `.` anche sui puntatori (Dereferenza-Automatica).
{% end %}

#### Struct Opachi
Puoi definire uno struct come `opaque` (lett. _opaco_) per restringere l'accesso ai suoi campi al modulo che lo ha definito, permettendo comunque l'allocazione sullo stack dello struct (la grandezza è data).

```zc
// In utente.zc
opaque struct Utente {
    id: int;
    nome: string;
}

fn nuovo_utente(nome: string) -> Utente {
    return Utente{id: 1, nome: nome}; // OK: Dentro il modulo
}

// In main.zc
import "utente.zc";

fn main() {
    let u = nuovo_utente("Alice");
    // let id = u.id; // Error: Impossibile accedere al campo privato 'id'
}
```

#### Enum
Unioni taggate (tipi somma) capaci di contenere dati.
```zc
enum Forma {
    Cerchio(float),           // Contiene il raggio
    Rettangolo(float, float), // Contiene la larghezza e l'altezza
    Punto                     // Non contiene dati
}
```

#### Unioni
Unioni standard C (accesso non sicuro).
```zc
union Dati {
    i: int;
    f: float;
}
```

#### Vettori SIMD
Tipi di vettore SIMD nativi utilizzando le estensioni vettoriali di GCC/Clang. Annota uno struct con `@vector(N)` per definire un vettore di N elementi.
```zc
import "std/simd.zc";

fn main() {
    let a = f32x4{v: 1.0};              // Broadcast: {1.0, 1.0, 1.0, 1.0}
    let b = f32x4{1.0, 2.0, 3.0, 4.0};  // Inizializzazione per elemento
    let c = a + b;                       // Addizione per elemento
    let x = c[0];                        // Accesso all'elemento (float)
}
```
Gli operatori aritmetici (`+`, `-`, `*`, `/`) e bitwise (`&`, `|`, `^`) funzionano per elemento. Vedi [`std/simd.zc`](../std/simd.zc) per i tipi predefiniti.

#### Alias del tipo
Crea un alias per un tipo già esistente.
```zc
alias ID = int;
alias PuntoDellaMappa = Mappa<string, Punto>
alias OpFunc = fn(int, int) -> int
```
> **Nota:** Il punto e virgola finale è opzionale per gli alias di tipo.

#### Alias del tipo opachi
Puoi definire un alias del tipo come `opaque` (lett. _opaco_) per creare un nuovo tipo che si distingue dal suo tipo sottostante al di fuori del modulo che l'ha definito. Questo permette una forte incapsulamento e sicurezza dei tipi senza overhead extra durante l'esecuzione di un wrapper struct.

```zc
// In libreria.zc
opaque alias Handle = int;

fn crea_handle(v: int) -> Handle {
    return v; // Conversione implicita consentita all'interno del modulo
}

// In main.zc
import "libreria.zc";

fn main() {
    let h: Handle = crea_handle(42);
    // let i: int = h; // Errore: Validazione del tipo fallita
    // let h2: Handle = 10; // Errore: Validazione del tipo fallita
}
```
