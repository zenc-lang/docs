+++
title = "8. Speicherverwaltung"
weight = 8
+++

# 8. Speicherverwaltung


Zen C erlaubt manuelles Speichermanagement mit ergonomischen Hilfen.

#### Defer
Führt Code aus, wenn der aktuelle Scope verlassen wird. Defer-Statements werden in LIFO-Reihenfolge (Last-In, First-Out) ausgeführt.

```zc
let f = fopen("file.txt", "r");
defer fclose(f);
```

{% alert(type="warning") %}
Um undefiniertes Verhalten zu vermeiden, sind Kontrollfluss-Anweisungen (`return`, `break`, `continue`, `goto`) **nicht erlaubt** innerhalb eines `defer`-Blocks.
{% end %}

#### Autofree
Gibt die Variable automatisch frei, wenn der Scope endet.

```zc
autofree let types = malloc(1024);
```

#### Ressourcen-Semantik (Move by Default)
Zen C behandelt Typen mit Destruktoren (wie `File`, `Vec` oder malloc'd Pointer) als **Ressourcen**.  
Um Double-Free-Fehler zu vermeiden, können Ressourcen nicht implizit dupliziert werden.

- **Move by Default**: Zuweisung einer Ressourcen-Variable überträgt die Eigentümerschaft. Die ursprüngliche Variable wird ungültig (Moved).  
- **Copy-Typen**: Typen ohne Destruktor können sich für `Copy` entscheiden, wodurch Zuweisung eine Kopie erzeugt.

**Diagnose & Philosophie**:  
Fehlermeldung „Use of moved value“ bedeutet: *„Dieser Typ besitzt eine Ressource (z. B. Speicher oder Handle) und blindes Kopieren ist unsicher.“*

{% alert(type="note") %}
**Im Unterschied zu C/C++** dupliziert Zen C Ressourcen-Werte nicht automatisch.
{% end %}

**Funktionsargumente**:  
Werte, die an Funktionen übergeben werden, folgen denselben Regeln wie Zuweisung: Ressourcen werden bewegt, sofern sie nicht per Referenz übergeben werden.

```zc
fn process(r: Resource) { ... } // 'r' wird in die Funktion verschoben
fn peek(r: Resource*) { ... }   // 'r' wird geliehen (Referenz)
```

**Explizites Klonen**:  
Falls du *tatsächlich* zwei Kopien einer Ressource benötigst, gebe dies explizit an:

```zc
let b = a.clone(); // Ruft die 'clone'-Methode des Clone-Traits auf
```

**Opt-in Copy (Value Types)**: Für kleine Typen ohne Destruktor:

```zc
struct Point { x: int; y: int; }
impl Copy for Point {} // Erlaubt implizite Duplikation

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = p1; // Kopiert. p1 bleibt gültig.
}
```

#### RAII / Drop Trait

Implement `Drop` to run cleanup logic automatically when a value goes out of scope.

```zc
impl Drop for MyStruct {
    fn drop(self) {
        self.free();
    }
}
```

**Umhüllen eines RAII-Typs.** Wenn dein Struct ein Feld enthält, das bereits `Drop` implementiert (wie `Vec` oder `String`), kümmert sich der Compiler automatisch um die Bereinigung. Du musst kein `impl Drop` für das äußere Struct schreiben.

```zc
struct MyVecWrapper {
    inner: Vec<int>;  // Vec::drop() called automatically
}
```

{% alert(type="note") %}
**Beispiel:** `String` ist als `struct String { vec: Vec<char>; }` definiert -- es benötigt keine explizite `Drop`-Implementierung, da `Vec<char>` den gesamten Speicher verwaltet. `Set<T>` hingegen verwendet rohe `T*`-Zeiger und benötigt explizites `Drop`.
{% end %}

**Faustregel:**
- Felder vom Typ `Vec<T>`, `String` oder andere RAII-Typen → automatisches Drop
- Felder vom Typ `T*`, `malloc`-Zeiger oder Dateihandles → explizites Drop erforderlich
