+++
title = "5. Kontrollfluss"
weight = 5
+++

# 5. Kontrollfluss


#### Bedingte Anweisungen
```zc
if x > 10 {
    print "Groß";
} else if x > 5 {
    print "Mittel";
} else {
    print "Klein";
}

// Ternäroperator
let y = x > 10 ? 1 : 0;

// If-Ausdruck (für komplexe Bedingungen)
let kategorie = if (x > 100) { "riesig" } else if (x > 10) { "groß" } else { "klein" };
```

#### Pattern Matching
Leistungsfähige Alternative zu `switch`.

```zc
match wert {
    1         => { print "Eins" },
    2 || 3    => { print "Zwei oder Drei" },    // ODER mit ||
    4 or 5    => { print "Vier oder Fünf" },    // ODER mit 'or'
    6, 7, 8   => { print "Sechs bis Acht" },    // ODER mit Komma
    10 .. 15  => { print "10 bis 14" },         // Exklusiver Bereich (Legacy)
    10 ..< 15 => { print "10 bis 14" },         // Exklusiver Bereich (explizit)
    20 ..= 25 => { print "20 bis 25" },         // Inklusiver Bereich
    _         => { print "Andere" },
}

// Destrukturierung von Enums
match form {
    Form::Kreis(r)       => { println "Radius: {r}" },
    Form::Rechteck(w, h) => { println "Fläche: {w*h}" },
    Form::Point          => { println "Point" },
}
```

#### Referenzbindung
Um einen Wert ohne Ownership-Übernahme zu inspizieren (kein Move), nutze das Schlüsselwort `ref` im Pattern.  
Wichtig für Typen, die Move-Semantik implementieren (z. B. `Option`, `Result`, Non-Copy-Strukturen).

```zc
let opt = Some(NonCopyVal{...});
match opt {
    Some(ref x) => {
        // 'x' ist ein Zeiger auf den Wert innerhalb von 'opt'
        // 'opt' wird hier NICHT verschoben oder verbraucht
        println "{x.feld}"; 
    },
    None => {}
}
```

#### Schleifen
```zc
// Bereich
for i in 0..10 { ... }      // Exklusiv (0 bis 9)
for i in 0..<10 { ... }     // Exklusiv (explizit)
for i in 0..=10 { ... }     // Inklusiv (0 bis 10)
for i in 0..10 step 2 { ... }
for i in 10..0 step -1 { ... }  // Absteigende Schleife

// Iterator (Vec oder eigene Iterable)
for element in vec { ... }

// Enumeriert: Index und Wert
for i, wert in arr { ... }           // i = 0, 1, 2, ...
for i, wert in 0..10 step 2 { ... }  // i = 0, 1, 2, ...; wert = 0, 2, 4, ...

// Direkte Iteration über Arrays fester Größe
let arr: int[5] = [1, 2, 3, 4, 5];
for wert in arr {
    // wert ist int
    println "{wert}";
}

// While-Schleife
while x < 10 { ... }

// Do-While-Schleife
do { ... } while x < 10;

// Endlosschleife mit Label
äußerer: loop {
    if erledigt { break äußerer; }
}

// Wiederholung N-mal
for _ in 0..5 { ... }
```

#### Erweiterter Kontrollfluss
```zc
// Guard: else ausführen und zurückkehren, falls Bedingung falsch
guard ptr != NULL else { return; }

// Unless: Ausführen, falls Bedingung nicht wahr
unless ist_gueltig { return; }
```
