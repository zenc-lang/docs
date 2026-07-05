+++
title = "5. Controllo di Flusso"
weight = 5
+++

# 5. Controllo di Flusso {#5-controllo-di-flusso}


#### Condizionali
```zc
if x > 10 {
    print "Grande";
} else if x > 5 {
    print "Medio";
} else {
    print "Piccolo";
}

// Operatore ternario
let y = x > 10 ? 1 : 0; // Se x è maggiore di 10 y sarà uguale a 1, in ogni altro caso, y sarà uguale a 0

// If-Expression (per condizioni complesse)
let categoria = if (x > 100) { "enorme" } else if (x > 10) { "grande" } else { "piccolo" };
```

#### Pattern Matching
Alternativa potente agli `switch`.
```zc
match val {
    1         => { print "Uno" },
    2 || 3    => { print "Due o Tre" },           // OR logico con ||
    4 or 5    => { print "Quattro or Cinque" },   // OR logico con 'or'
    6, 7, 8   => { print "Da Sei a Otto" },       // OR logico con la virgola (,)
    10 .. 15  => { print "Da 10 a 14" },          // Range Esclusivo (Legacy)
    10 ..< 15 => { print "Da 10 a 14" },          // Range Esclusivo (Esplicito)
    20 ..= 25 => { print "Da 20 a 25" },          // Range Inclusivo
    _         => { print "Altro" },
}

// Destrutturazione degli Enums
match forma {
    Forma::Cerchio(r)        => { println "Raggio: {r}" },
    Forma::Rettangolo(w, h)  => { println "Area: {w*h}" },
    Forma::Punto             => { println "Punto" },
}
```

#### Associaione di riferiemnto
Per ispezionare un valore senza assumerne la proprietà (spostarlo) puoi usare la keyword `ref` nel pattern. Questo è essenziale per i tipi che implementano Semantiche di Movimento (come `Option`, `Result`, struct non-copiabile).

```zc
let opt = Qualche(ValoreNonCopiable{...});
match opt {
    Some(ref x) => {
        // 'x' è un puntatore che punta al valore contenuto in 'opt'
        // 'opt' NON viene né mosso né consumato qui
        println "{x.field}"; 
    },
    None => {}
}
```

#### Loops
```zc
// Range
for i in 0..10 { ... }      // Esclusivo (Da 0 a 9)
for i in 0..<10 { ... }     // Esclusivo (Esplicito)
for i in 0..=10 { ... }     // Inclusivo (Da 0 a 10)
for i in 0..10 step 2 { ... }
for i in 10..0 step -1 { ... }  // Descending loop

// Iteratore (Vec, Array, oppure un Iteratore personalizzato)
for item in collection { ... }

// Enumerato: ottieni indice e valore
for i, val in collection { ... }   // i = 0, 1, 2, ...
for i, val in 0..10 step 2 { ... } // i = 0, 1, 2, ...; val = 0, 2, 4, ...

// While (lett. mentre)
while x < 10 { ... }

// Do-While
do { ... } while x < 10;

// Infinito con etichetta
esterno: loop {
    if done { break esterno; }
}

// Ripeti N volte
for _ in 0..5 { ... }
```

#### Controllo Avanzato
```zc
// Guard (lett. 'guardia'): Esegue il caso 'else' e ritorna se la condizione è falsa
guard ptr != NULL else { return; }

// Unless (lett. 'a meno che'): Se non vero
unless è_valido { return; }
```
