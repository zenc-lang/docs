+++
title = "7. Impresión e Interpolación de Cadenas"
weight = 7
+++

# 7. Impresión e Interpolación de Cadenas {#7-impresion-e-interpolacion-de-cadenas}


Zen C proporciona opciones versátiles para imprimir en la consola, incluyendo palabras clave y abreviaturas concisas.

#### Palabras Clave

| Palabra Clave | Descripción |
|:---|:---|
| `print "texto"` | Imprime en `stdout` sin un salto de línea al final. |
| `println "texto"` | Imprime en `stdout` **con** un salto de línea al final. |
| `eprint "texto"` | Imprime en `stderr` sin un salto de línea al final. |
| `eprintln "texto"` | Imprime en `stderr` **con** un salto de línea al final. |

#### Abreviaturas

Zen C permite usar literales de cadena directamente como sentencias para una impresión rápida:

| Sintaxis | Equivalente | Descripción |
|:---|:---|:---|
| `"Hz"` | `println "Hz"` | Imprime en `stdout` con salto de línea. |
| `"Hz"..` | `print "Hz"` | Imprime en `stdout` sin salto de línea. |
| `!"Err"` | `eprintln "Err"` | Imprime en `stderr` con salto de línea. |
| `!"Err"..` | `eprint "Err"` | Imprime en `stderr` sin salto de línea. |

#### Interpolación de Cadenas

Puedes embeber expresiones directamente dentro de literales de cadena usando la sintaxis `{}`. Esto funciona con todos los métodos de impresión y abreviaturas de cadena.

La interpolación de cadenas en Zen C es **implícita**: si tu cadena contiene `{...}`, se analizará automáticamente como una cadena interpolada. También puedes usar explícitamente el prefijo `f` (ej. `f"..."`) para forzar la semántica de interpolación.

```zc
let x = 42;
let nombre = "Zen";
println "Valor: {x}, Nombre: {nombre}";
"Valor: {x}, Nombre: {nombre}"; // abreviatura println
```

**Escapando Llaves**: Usa `{{` para producir una llave literal `{` y `}}` para una `}` literal:

```zc
let json = "JSON: {{\"clave\": \"valor\"}}";
// Salida: JSON: {"clave": "valor"}
```

**Cadenas Crudas (Raw Strings)**: Para definir una cadena donde la interpolación y las secuencias de escape se ignoran por completo, usa el prefijo `r` (ej. `r"..."`):

```zc
let regex = r"\w+"; // Contiene exactamente \ w +
let raw_json = r'{"clave": "valor"}'; // No es necesario escapar llaves
```

#### Cadenas Multilínea

Zen C soporta bloques de cadenas multilínea crudas usando el delimitador `"""`. Esto es extremadamente útil para escribir lenguajes embebidos (GLSL, HTML) o para generar código C en bloques `comptime` sin tener que escapar manualmente los saltos de línea y las comillas internas.

Al igual que las cadenas estándar, las cadenas multilínea soportan **interpolación implícita**. También puedes prefijarlas explícitamente:
- `f"""..."""`: Marca explícitamente como un bloque de cadena interpolada.
- `r"""..."""`: Marca explícitamente como un bloque de cadena cruda (sin interpolación, sin secuencias de escape).

```zc
let prompt = """
  Por favor, introduzca su nombre:
  Escribe "exit" para cancelar.
""";

let mundo = "mundo";
let script = """
  fn hola() {
      println "hola, {mundo}!";
  }
""";

let pure_raw = r"""
  Aquí las {llaves} son solo texto, y \n es literalmente una barra y una n.
""";
```

#### Prompts de Entrada (`?`)

Zen C soporta una abreviatura para solicitar entrada al usuario usando el prefijo `?`.

- `? "Texto del prompt"`: Imprime el prompt (sin salto de línea) y espera la entrada (lee una línea).
- `? "Ingresa la edad: " (edad)`: Imprime el prompt y escanea la entrada en la variable `edad`.
    - Los especificadores de formato se infieren automáticamente según el tipo de variable.

```zc
let edad: int;
? "¿Cuántos años tienes? " (edad);
println "Tienes {edad} años.";
```
