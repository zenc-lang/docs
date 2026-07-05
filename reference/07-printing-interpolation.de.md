+++
title = "7. Ausgabe und String-Interpolation"
weight = 7
+++

# 7. Ausgabe und String-Interpolation {#7-ausgabe-und-string-interpolation}


Zen C bietet vielseitige Optionen zur Konsolenausgabe, einschließlich Schlüsselwörtern und kurzen Schreibweisen.

#### Schlüsselwörter

| Schlüsselwort | Beschreibung |
|:---|:---|
| `print "..."` | Gibt auf `stdout` aus ohne nachgestellten Zeilenumbruch. |
| `println "..."` | Gibt auf `stdout` aus **mit** nachgestelltem Zeilenumbruch. |
| `eprint "..."` | Gibt auf `stderr` aus ohne nachgestellten Zeilenumbruch. |
| `eprintln "..."` | Gibt auf `stderr` aus **mit** nachgestelltem Zeilenumbruch. |

#### Kurze Schreibweisen

Zen C erlaubt, String-Literale direkt als Anweisungen zu verwenden:

| Syntax | Entspricht | Beschreibung |
|:---|:---|:---|
| `"Hz"` | `println "Hz"` | Gibt auf `stdout` aus, mit Zeilenumbruch. |
| `"Hz"..` | `print "Hz"` | Gibt auf `stdout` aus, ohne Zeilenumbruch. |
| `!"Err"` | `eprintln "Err"` | Gibt auf `stderr` aus, mit Zeilenumbruch. |
| `!"Err"..` | `eprint "Err"` | Gibt auf `stderr` aus, ohne Zeilenumbruch. |

#### String-Interpolation

Ausdrücke können direkt in String-Literalen mit `{}` eingebettet werden.  
Dies funktioniert für alle Druckmethoden und String-Kurzschreibweisen.

Die Interpolation in Zen C ist **implizit**: enthält ein String `{...}`, wird es automatisch als interpolierter String geparst. Du kannst auch explizit mit `f` prefixen (z. B. `f"..."`), um Interpolation zu erzwingen.

```zc
let x = 42;
let name = "Zen";
println "Wert: {x}, Name: {name}";
"Wert: {x}, Name: {name}"; // Kurzschreibweise für println
```

**Escape für geschweifte Klammern**:  `{{` erzeugt `{`, `}}` erzeugt `}`:

```zc
let json = "JSON: {{\"key\": \"value\"}}";
// Ausgabe: JSON: {"key": "value"}
```

**Raw-Strings**: Strings, bei denen Interpolation und Escape-Sequenzen komplett ignoriert werden, werden mit `r` prefixiert (z. B. `r"..."`):

```zc
let regex = r"\w+"; // Enthält exakt \ w +
let raw_json = r'{"key": "value"}'; // Kein Escapen von Klammern nötig
```

#### Mehrzeilige Strings

Zen C unterstützt rohe mehrzeilige Strings mit `"""`-Delimiter. Sehr nützlich für eingebettete Sprachen (GLSL, HTML) oder zum Generieren von C-Code in `comptime`-Blöcken ohne manuelles Escapen.

Wie normale Strings unterstützen mehrzeilige Strings **implizite Interpolation**. Man kann auch explizit prefixen:  
- `f"""..."""`: explizit interpolierter Stringblock  
- `r"""..."""`: explizit roher Stringblock (keine Interpolation, keine Escape-Sequenzen)

```zc
let prompt = """
  Bitte geben Sie Ihren Namen ein:
  Tippen Sie "exit", um abzubrechen.
""";

let welt = "Welt";
let script = """
  fn hallo() {
      println "Hallo, {welt}!";
  }
""";

let nur_raw = r"""
  Hier sind {klammern} einfach Text, und \n ist buchstäblich Slash-n.
""";
```

#### Eingabeaufforderungen (`?`)

Zen C unterstützt eine Kurzschreibweise für Benutzereingaben mit dem `?`-Präfix.

- `? "Prompt-Text"`: Gibt die Eingabeaufforderung aus (ohne Zeilenumbruch) und wartet auf Eingabe (liest eine Zeile).  
- `? "Alter eingeben: " (alter)`: Gibt Prompt aus und speichert die Eingabe in der Variablen `alter`.  
    - Format-Spezifizierer werden automatisch anhand des Variablentyps bestimmt.

```zc
let alter: int;
? "Wie alt bist du? " (alter);
println "Du bist {alter} Jahre alt.";
```
