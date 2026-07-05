+++
title = "7. Stampaggio e Interpolazione delle Stringhe"
weight = 7
+++

# 7. Stampaggio e Interpolazione delle Stringhe {#7-stampaggio-e-interpolazione-delle-stringhe}


Zen C fornisce opzioni versatili per stampare alla console, includendo keyword e scorciatoie coincise.

#### Keyword

| Keyword | Descrizione |
|:---|:---|
| `print "testo"` | Stampa a `stdout` senza aggiunzione di una newline automatica. |
| `println "testo"` | Stampa a `stdout` aggiungendo una newline automatica. |
| `eprint "testo"` | Stampa a `stderr` senza aggiunzione di una newline automatica. |
| `eprintln "testo"` | Stampa a `stderr` aggiungendo una newline automatica. |

#### Scorciatoie

Zen C ti permette di utilizzare stringhe letterali direttamente come istruzione di stampaggio veloce:

| Sintassi | Equivalente | Descrizione |
|:---|:---|:---|
| `"Ciao!"` | `println "Ciao!"` | Aggiunge una newline implicitamente. |
| `"Ciao!"..` | `print "Ciao!"` | Non aggiunge una newline. |
| `!"Errore"` | `eprintln "Errore"` | Output a stderr. |
| `!"Errore"..` | `eprint "Errore"` | Output a stderr, senza newline. |

#### Interpolazione delle Stringhe

Puoi incorporare espressioni direttamente all'interno di stringhe letterali utilizzando la sintassi `{}`. Questo funziona con tutti i metodi di stampaggio, incluse le scorciatoie.

L'interpolazione di stringhe in Zen C è **implicita**: se la tua stringa contiene `{...}`, verrà analizzata automaticamente come una stringa interpolata. Puoi anche usare esplicitamente il prefisso `f` (es. `f"..."`) per forzare la semantica di interpolazione.

```zc
let x = 42;
let nome = "Max";
println "Valore: {x}, Nome: {name}";
"Valore: {x}, Nome: {name}"; // scorciatoia per println
```

**Escape delle Parentesi Graffe**: Usa `{{` per produrre una parentesi graffa letterale `{` e `}}` per una `}` letterale:

```zc
let json = "JSON: {{\"chiave\": \"valore\"}}";
// Output: JSON: {"chiave": "valore"}
```

**Stringhe Grezze (Raw Strings)**: Per definire una stringa in cui le sequenze di interpolazione e di escape vengono completamente ignorate, inserici il prefisso `r` (es. `r"..."`):

```zc
let regex = r"\w+"; // Contiene esattamente \ w +
let raw_json = r'{"chiave": "valore"}'; // Non è necessario l'escape delle parentesi
```

#### Stringhe Multilinea

Zen C supporta blocchi di stringhe multilinea grezzi utilizzando il delimitatore `"""`. Questo è estremamente utile per la scrittura di linguaggi incorporati (GLSL, HTML) o per la generazione di codice C all'interno di blocchi `comptime` senza il bisogno di inserire manualmente l'escape a capo ed alle virgolette all'interno.

Come le stringhe standard, le stringhe multilinea supportano l'**interpolazione implicita**. Puoi aggiugere l'escape in maniera esplicita usando:
- `f"""..."""`: Contrassegna in modo esplicito un blocco di stringa interpolato.
- `r"""..."""`: Contrassegna in modo esplicito un blocco di stringa grezzo (nessuna interpolazione, nessuna sequenza di escape).

```zc
let prompt = """
  Per favore, inserisci il tuo nome:
  Digita "exit" per annullare.
""";

let mondo = "mondo";
let script = """
  fn ciao() {
      println "ciao, {mondo}!";
  }
""";

let pure_raw = r"""
  Qui le {parentesi} sono solo testo, e \n e' letteralmente barra ed n.
""";
```

#### Prompt di Input (`?`)

Zen C supporta una scorciatoia per richiedere input dall'utente utilizzando il prefisso `?`.

- `? "Inserisci il tuo nome"`: Stampa il prompt (senza newline) e aspetta per dell'input (legge una linea).
- `? "Inserisci la tua età: " (età)`: Stampa il prompt e memorizza l'input nella variabile `età`.
    - Gli specificatori del formato vengono automaticamente inferiti in base al tipo della variabile.

```zc
let età: int;
? "Inserisci la tua età: " (età);
println "Hai {età} anni.";
```
