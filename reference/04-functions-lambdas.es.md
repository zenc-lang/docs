+++
title = "4. Funciones y Lambdas"
weight = 4
+++

# 4. Funciones y Lambdas {#4-funciones-y-lambdas}


#### Funciones
```zc
fn suma(a: int, b: int) -> int {
    return a + b;
}

// Argumentos con nombre soportados en las llamadas
suma(a: 10, b: 20);
```

{% alert(type="note") %}
Los argumentos con nombre deben seguir estrictamente el orden de los parámetros definidos. `suma(b: 20, a: 10)` es inválido.
{% end %}

#### Argumentos Const
Los argumentos de las funciones pueden marcarse como `const` para imponer una semántica de solo lectura. Este es un calificador de tipo, no una constante manifiesta.

```zc
fn print_val(v: const int) {
    // v = 10; // Error: No se puede asignar a una variable const
    println "{v}";
}
```

#### Argumentos por Defecto
Las funciones pueden definir valores por defecto para los argumentos finales. Estos pueden ser literales, expresiones o código válido de Zen C (como constructores de structs).
```zc
// Valor por defecto simple
fn incrementar(val: int, cantidad: int = 1) -> int {
    return val + cantidad;
}

// Valor por defecto por expresión (evaluado en el sitio de la llamada)
fn offset(val: int, pad: int = 10 * 2) -> int {
    return val + pad;
}

// Valor por defecto de tipo struct
struct Config { debug: bool; }
fn init(cfg: Config = Config { debug: true }) {
    if cfg.debug { println "Modo Debug"; }
}

fn main() {
    incrementar(10);    // 11
    offset(5);          // 25
    init();             // Imprime "Modo Debug"
}
```

#### Lambdas (Clausuras)
Funciones anónimas que pueden capturar su entorno.
```zc
let factor = 2;
let doble = x -> x * factor;  // Sintaxis de flecha
let completo = fn(x: int) -> int { return x * factor; }; // Sintaxis de bloque

// Captura por Referencia (Sintaxis de Bloque)
let val = 10;
let modificar = fn[&]() { val += 1; }; 
modificar(); // val ahora es 11

// Captura por Referencia (Sintaxis de Flecha)
let modificar_flecha = [&] x -> val += x;
modificar_flecha(5); // val ahora es 16

// Captura por Referencia (Sintaxis de Flecha con Múltiples Argumentos)
let sumar_en = [&] (a, b) -> val += (a + b);
sumar_en(2, 2); // val ahora es 20

// Captura por Valor (Por Defecto)
let original = 100;
let implicita = x -> original + x;      // Captura implícita por valor (sin corchetes)
let explicita = [=] x -> original + x;  // Captura explícita por valor
// let fallar = x -> original += x;     // Error: no se puede asignar a valor capturado

```

#### Punteros a Funciones Crudos
Zen C soporta punteros a funciones de C crudos usando la sintaxis `fn*`. Esto permite una interoperabilidad perfecta con bibliotecas de C que esperan punteros a funciones sin la sobrecarga de las clausuras.

```zc
// Función que recibe un puntero a función crudo
fn set_callback(cb: fn*(int)) {
    cb(42);
}

// Función que retorna un puntero a función crudo
fn get_callback() -> fn*(int) {
    return mi_manejador;
}

// Se soportan punteros a punteros de funciones (fn**)
let pptr: fn**(int) = &ptr;
```

#### Funciones Variádicas
Las funciones pueden aceptar un número variable de argumentos usando `...` y el tipo `va_list`.
```zc
fn log(lvl: int, fmt: char*, ...) {
    let ap: va_list;
    va_start(ap, fmt);
    vprintf(fmt, ap); // Usa stdio de C
    va_end(ap);
}
```
