+++
title = "14. Interoperabilità C"
weight = 14
+++

# 14. Interoperabilità C {#14-interoperabilita-c}


Zen C offre due modi per interagire con il codice C: **Import Trusted** (Conveniente) e **FFI Esplicita** (Sicuro/Preciso).

#### Metodo 1: Import Trusted (Conveniente)
Puoi importare un header C direttamente usando la parola chiave `import` con l'estensione `.h`. Questo tratta l'header come un modulo e assume che tutti i simboli acceduti esistano.

```zc
//> link: -lm
import "math.h" as c_math;

fn main() {
    // Il compilatore si fida della correttezza; emette 'cos(...)' direttamente
    let x = c_math::cos(3.14159);
}
```

> **Pro**: Zero boilerplate. Accesso immediato a tutto nell'header.
> **Contro**: Nessuna sicurezza dei tipi da Zen C (errori catturati dal compilatore C dopo).

#### Metodo 2: FFI Esplicita (Sicuro)
Per un controllo rigoroso dei tipi o quando non vuoi includere il testo di un header, usa `extern fn`.

```zc
include <stdio.h> // Emette #include <stdio.h> nel C generato
// Definisci firma rigorosa
extern fn printf(fmt: char*, ...) -> c_int;

fn main() {
    printf("Ciao FFI: %d\n", 42); // Controllato nei tipi da Zen C
}
```

> **Pro**: Zen C assicura che i tipi corrispondano.
> **Contro**: Richiede dichiarazione manuale delle funzioni.

#### `import` vs `include`

- **`import "file.h"`**: Registra l'header come un modulo con nome. Abilita l'accesso implicito ai simboli (es. `file::function()`).
- **`include <file.h>`**: Emette puramente `#include <file.h>` nel codice C generato. Non introduce alcun simbolo nel compilatore Zen C; devi usare `extern fn` per accedervi.
