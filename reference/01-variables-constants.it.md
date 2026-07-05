+++
title = "1. Variabili e Costanti"
weight = 1
+++

# 1. Variabili e Costanti {#1-variabili-e-costanti}


Zen C differenzia le costanti al tempo di compilazione e le variabili di esecuzione.

#### Costanti Manifesto (`def`)
Valori che esistono solo durante la compilazione (integrate nel codice). Utilizzale per le grandezze degli array, configurazioni fisse, e numeri magici.

```zc
def MAX_SIZE = 1024;
let buffer: char[MAX_SIZE]; // Grandezza valida per l'array
```

#### Variabili (`let`)
Locazioni di memoria. Possono essere mutabili o di sola lettura (`const`).

```zc
let x = 10;             // Mutabile
x = 20;                 // OK

let y: const int = 10;  // Sola lettura (Tipo qualificato)
// y = 20;              // Errore: impossibile assegnare un valore ad una variabile costante
```

{% alert(type="tip") %}
**Inferenza di tipo**: Zen C inferisce automaticamente il tipo per le variabili inizializzate. Compilando ciò alla keyword `auto` dello standard C23 nei compilatori supportati, oppure alla estensione GCC `__auto_type`.
{% end %}
