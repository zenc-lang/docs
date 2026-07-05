+++
title = "7. Printing and String Interpolation"
weight = 7
+++

# 7. Printing and String Interpolation {#7-printing-and-string-interpolation}


Zen C provides versatile options for printing to the console, including keywords and concise shorthands.

#### Keywords

| Keyword | Description |
|:---|:---|
| `print "..."` | Prints to `stdout` without a trailing newline. |
| `println "..."` | Prints to `stdout` **with** a trailing newline. |
| `eprint "..."` | Prints to `stderr` without a trailing newline. |
| `eprintln "..."` | Prints to `stderr` **with** a trailing newline. |

#### Shorthands

Zen C allows you to use string literals directly as statements for quick printing:

| Syntax | Equivalent | Description |
|:---|:---|:---|
| `"Hz"` | `println "Hz"` | Prints to `stdout` with newline. |
| `"Hz"..` | `print "Hz"` | Prints to `stdout` without newline. |
| `!"Err"` | `eprintln "Err"` | Prints to `stderr` with newline. |
| `!"Err"..` | `eprint "Err"` | Prints to `stderr` without newline. |

#### String Interpolation

You can embed expressions directly into string literals using `{}` syntax. This works with all printing methods and string shorthands.

String interpolation in Zen C is **implicit**: if your string contains `{...}`, it will automatically be parsed as an interpolated string. You can also explicitly prefix a string with `f` (e.g., `f"..."`) to force interpolation semantics.

```zc
let x = 42;
let name = "Zen";
println "Value: {x}, Name: {name}";
"Value: {x}, Name: {name}"; // shorthand println
```

**Escaping Braces**: Use `{{` to produce a literal `{` and `}}` for a literal `}`:

```zc
let json = "JSON: {{\"key\": \"value\"}}";
// Output: JSON: {"key": "value"}
```

**Raw Strings**: To define a string where interpolation and escape sequences are completely ignored, prefix it with `r` (e.g., `r"..."`):

```zc
let regex = r"\w+"; // Contains exactly \ w +
let raw_json = r'{"key": "value"}'; // No brace escaping needed
```

#### Multiline Strings

Zen C supports raw multiline string blocks using the `"""` delimiter. This is extremely useful for writing embedded languages (GLSL, HTML) or generating C-code in `comptime` blocks without manually escaping newlines and interior quotes.

Like standard strings, multiline strings support **implicit interpolation**. You can also explicitly prefix them:
- `f"""..."""`: Explicitly marks it as an interpolated string block.
- `r"""..."""`: Explicitly marks it as a raw string block (no interpolation, no escape sequences).

```zc
let prompt = """
  Please enter your name:
  Type "exit" to cancel.
""";

let world = "world";
let script = """
  fn hello() {
      println "hello, {world}!";
  }
""";

let pure_raw = r"""
  Here {braces} are just text, and \n is literally slash-n.
""";
```

#### Input Prompts (`?`)

Zen C supports a shorthand for prompting user input using the `?` prefix.

- `? "Prompt text"`: Prints the prompt (without newline) and waits for input (reads a line).
- `? "Enter age: " (age)`: Prints prompt and scans input into the variable `age`.
    - Format specifiers are automatically inferred based on variable type.

```zc
let age: int;
? "How old are you? " (age);
println "You are {age} years old.";
```
