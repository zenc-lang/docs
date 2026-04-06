+++
title = "5. Flujo de Control"
weight = 5
+++

# 5. Flujo de Control


#### Condicionales
```zc
if x > 10 {
    print "Grande";
} else if x > 5 {
    print "Mediano";
} else {
    print "Pequeño";
}

// Ternario
let y = x > 10 ? 1 : 0;

// If-Expression (para condiciones complejas)
let categoria = if (x > 100) { "enorme" } else if (x > 10) { "grande" } else { "pequeño" };
```

#### Coincidencia de Patrones (Pattern Matching)
Una alternativa potente al `switch`.
```zc
match val {
    1         => { print "Uno" },
    2 || 3    => { print "Dos o Tres" },      // OR con ||
    4 or 5    => { print "Cuatro o Cinco" },  // OR con 'or'
    6, 7, 8   => { print "Seis a Ocho" },     // OR con coma
    10 .. 15  => { print "10 a 14" },         // Rango exclusivo (Legado)
    10 ..< 15 => { print "10 a 14" },         // Rango exclusivo (Explícito)
    20 ..= 25 => { print "20 a 25" },         // Rango inclusivo
    _         => { print "Otro" },
}

// Desestructuración de Enums
match shape {
    Shape::Circle(r)   => { println "Radio: {r}" },
    Shape::Rect(w, h)  => { println "Área: {w*h}" },
    Shape::Point       => { println "Punto" },
}
```

#### Vinculación por Referencia (Reference Binding)
Para inspeccionar un valor sin tomar posesión de él (sin moverlo), usa la palabra clave `ref` en el patrón. Esto es esencial para tipos que implementan la Semántica de Movimiento (como `Option`, `Result`, structs que no son Copy).

```zc
let opt = Some(ValorNoCopy{...});
match opt {
    Some(ref x) => {
        // 'x' es un puntero al valor dentro de 'opt'
        // 'opt' NO se mueve ni se consume aquí
        println "{x.field}"; 
    },
    None => {}
}
```

#### Bucles
```zc
// Rango
for i in 0..10 { ... }      // Exclusivo (0 al 9)
for i in 0..<10 { ... }     // Exclusivo (Explícito)
for i in 0..=10 { ... }     // Inclusivo (0 al 10)
for i in 0..10 step 2 { ... }
for i in 10..0 step -1 { ... }  // Descending loop

// Iterador (Vec o Iterable personalizado)
for item in vec { ... }

// Enumerado: obtener índice y valor
for i, val in arr { ... }       // i = 0, 1, 2, ...
for i, val in 0..10 step 2 { ... } // i = 0, 1, 2, ...; val = 0, 2, 4, ...

// Iterar sobre arrays de tamaño fijo directamente
let arr: int[5] = [1, 2, 3, 4, 5];
for val in arr {
    // val es int
    println "{val}";
}

// While
while x < 10 { ... }

// Do-While
do { ... } while x < 10;

// Infinito con etiqueta
externo: loop {
    if terminado { break externo; }
}

// Repetir N veces
for _ in 0..5 { ... }
```

#### Control Avanzado
```zc
// Guard: Ejecuta else y retorna si la condición es falsa
guard ptr != NULL else { return; }

// Unless: Si no es verdadero
unless es_valido { return; }
```
