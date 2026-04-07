+++
title = "14. Framework di Test Unitari"
weight = 14
+++

# 14. Framework di Test Unitari


Zen C include un framework di test integrato che consente di scrivere test unitari direttamente nei file sorgente utilizzando la parola chiave `test`.

#### Sintassi
Un blocco `test` contiene un nome descrittivo e un corpo di codice da eseguire. I test non richiedono una funzione `main` per essere eseguiti.

```zc
test "unittest1" {
    "Questo è un test unitario";

    let a = 3;
    assert(a > 0, "a dovrebbe essere un intero positivo");

    "unittest1 superato.";
}
```

#### Esecuzione dei Test
Per eseguire tutti i test in un file, usa il comando `run`. Il compilatore rileverà ed eseguirà automaticamente tutti i blocchi `test` di alto livello.

```bash
zc run mio_file.zc
```

#### Asserzioni
Usa la funzione integrata `assert(condizione, messaggio)` per verificare le aspettative. Se la condizione è falsa, il test fallirà e stamperà il messaggio fornito.

---

## Libreria Standard

Zen C include una libreria standard (`std`) che ricopre funzionalità essenziali.

[Scopri la documentazione della Libreria Standard](../docs/std/README.md)

### Moduli Chiave

<details>
<summary>Clicca per vedere tutti i moduli della Libreria Standard</summary>

| Modulo | Descrizione | Documentazione |
| :--- | :--- | :--- |
| **`std/bigfloat.zc`** | Aritmetica in virgola mobile a precisione arbitraria. | [Docs](../docs/std/bigfloat.md) |
| **`std/bigint.zc`** | Intero a precisione arbitraria `BigInt`. | [Docs](../docs/std/bigint.md) |
| **`std/bits.zc`** | Operazioni bit a bit a basso livello (`rotl`, `rotr`, ecc.). | [Docs](../docs/std/bits.md) |
| **`std/complex.zc`** | Aritmetica dei numeri complessi `Complex`. | [Docs](../docs/std/complex.md) |
| **`std/vec.zc`** | Array dinamico espandibile `Vec<T>`. | [Docs](../docs/std/vec.md) |
| **`std/string.zc`** | Tipo `String` allocato sull'Heap con supporto UTF-8. | [Docs](../docs/std/string.md) |
| **`std/queue.zc`** | Coda FIFO (Buffer Circolare). | [Docs](../docs/std/queue.md) |
| **`std/map.zc`** | Hash Map Generica `Map<V>`. | [Docs](../docs/std/map.md) |
| **`std/fs.zc`** | Operazioni del File System. | [Docs](../docs/std/fs.md) |
| **`std/io.zc`** | Standard Input/Output (`print`/`println`). | [Docs](../docs/std/io.md) |
| **`std/option.zc`** | Valori opzionali (`Some`/`None`). | [Docs](../docs/std/option.md) |
| **`std/result.zc`** | Gestione degli errori (`Ok`/`Err`). | [Docs](../docs/std/result.md) |
| **`std/path.zc`** | Manipolazione dei percorsi Cross-platform. | [Docs](../docs/std/path.md) |
| **`std/env.zc`** | Variabili d'ambiente del processo. | [Docs](../docs/std/env.md) |
| **`std/net/`** | TCP, UDP, HTTP, DNS, URL. | [Docs](../docs/std/net.md) |
| **`std/thread.zc`** | Thread e Sincronizzazione. | [Docs](../docs/std/thread.md) |
| **`std/time.zc`** | Misuramenti di tempo e `sleep`. | [Docs](../docs/std/time.md) |
| **`std/json.zc`** | Parsing JSON e serializzazione. | [Docs](../docs/std/json.md) |
| **`std/stack.zc`** | Stack LIFO `Stack<T>`. | [Docs](../docs/std/stack.md) |
| **`std/set.zc`** | Hash Set Generico `Set<T>`. | [Docs](../docs/std/set.md) |
| **`std/process.zc`** | Esecuzione e gestione di processi. | [Docs](../docs/std/process.md) |
| **`std/regex.zc`** | Espressioni Regolari (basato su TRE). | [Docs](../docs/std/regex.md) |
| **`std/simd.zc`** | Tipi di vettore SIMD nativi. | [Docs](../docs/std/simd.md) |

</details>

---

## Tooling

Zen C fornisce un Language Server (LSP) e un REPL per migliorare l'esperienza degli sviluppatori.

### Language Server (LSP)

Il server del linguaggio (LSP) di Zen C supporta le feature standard per l'integrazione con gli editor, esso fornisce:

*   **Vai alla definizione**
*   **Trova riferimenti**
*   **Informazioni sull'hover**
*   **Completamenti automatici** (Nomi di funzioni/struct, Completamento dal punto per i methods/campi)
*   **Simboli dei documenti** (Outline)
*   **Aiuto con le signature delle funzioni**
*   **Diagnostiche** (Errori sintattici/semantici)

Per avviare il server del linguaggio (tipicamente configurato nelle impostazioni LSP del tuo editor):

```bash
zc lsp
```

Il server comunica via lo Standard I/o (JSON-RPC 2.0).

### REPL

Il Read-Eval-Print-Loop (REPL, lett. _Leggi-Esegui-Stampa-Ripeti_) ti permette ti sperimentare con il codice Zen C in maniera interattiva.

```bash
zc repl
```

#### Funzionalità

*   **Coding interattivo**: Scrivi espressioni o istruzioni per una esecuzione immediata.
*   **Storia persistente**: I comandi vengono salvati in `~/.zprep_history`.
*   **Script di avvio**: I comandi di avvio (auto-load) sono salvati in `~/.zprep_init.zc`.

#### Comandi

| Comande | Descrizione |
|:---|:---|
| `:help` | Mostra i comandi disponibili. |
| `:reset` | Cancella la storia della sessione corrente (variabili/funzioni). |
| `:vars` | Mostra le variabili attive. |
| `:funcs` | Mostra le funzioni definite dall'utente. |
| `:structs` | Mostra gli struct definiti dall'utente. |
| `:imports` | Mostra gli 'import' attivi. |
| `:history` | Mostra la storia dell'input della sessione. |
| `:type <expr>` | Mostra il tipo di un espressione. |
| `:c <stmt>` | Mostra il codice C generato per un istruzione. |
| `:time <expr>` | Esegui un benchmark per l'espressione data. (Esegue 1000 iterazioni). |
| `:edit [n]` | Modifica il comando `n` (default: l'ultimo comando) in `$EDITOR`. |
| `:save <file>` | Salva la sessione corrente in un file `.zc`. |
| `:load <file>` | Carica ed esegui un file `.zc` nella sessione corrente. |
| `:watch <expr>` | Watch (lett. _guarda_) un espressione (rieseguita dopo ogni entry). |
| `:unwatch <n>` | Rimuovi un watch. |
| `:undo` | Rimuovi l'ultimo comando dalla sessione. |
| `:delete <n>` | Rimuovi il comando all'indice `n`. |
| `:clear` | Pulisce lo schermo. |
| `:quit` | Esce dal REPL. |
| `! <cmd>` | Esegue un comando sulla shell (e.g. `!ls`). |

---

### Protocollo Server di Linguaggio (LSP)

Zen C include un Server di Linguaggio integrato per l'integrazione con gli editor.

- **[Guida all'Installazione e Configurazione](translations/LSP_IT.md)**
- **Editor Supportati**: VS Code, Neovim, Vim, Zed, e qualsiasi editor compatibile con LSP.

Usa `zc lsp` per avviare il server.

### Debugging Zen C

I programmi Zen C possono essere sottoposti a debug utilizzando i debugger C standard come **LLDB** o **GDB**.

#### Visual Studio Code

Per la migliore esperienza in VS Code, installa l'[estensione ufficiale Zen C](https://marketplace.visualstudio.com/items?itemName=Z-libs.zenc). Per il debugging, puoi utilizzare l'estensione **C/C++** (di Microsoft) o **CodeLLDB**.

Aggiungi queste configurazioni alla tua directory `.vscode` per abilitare il debugging con un clic:

**`tasks.json`** (Attività di compilazione):
```json
{
    "label": "Zen C: Build Debug",
    "type": "shell",
    "command": "zc",
    "args": [ "${file}", "-g", "-o", "${fileDirname}/app", "-O0" ],
    "group": { "kind": "build", "isDefault": true }
}
```

**`launch.json`** (Debugger):
```json
{
    "name": "Zen C: Debug (LLDB)",
    "type": "lldb",
    "request": "launch",
    "program": "${fileDirname}/app",
    "preLaunchTask": "Zen C: Build Debug"
}
```

## Supporto del Compilatore e Compatibilità

Zen C è stato creato in modo tale da poter funzionare con la maggior parte dei compilatori C11. Alcune funzionalità potrebbero affidarsi ad estensioni GNU C,  ma spesso queste funzionano anche su altri compilatori. Utilizza la flag `--cc` per modificare il backend.

```bash
zc run app.zc --cc clang
zc run app.zc --cc zig
```

### Stato della suite di test

<details>
<summary>Clicca per vedere i dettagli del supporto del compilatore</summary>

| Compilatore | Percentuale di Superamento | Funzionalità Supportate | Limitazioni Nota |
|:---|:---:|:---|:---|
| **GCC** | **100% (Completo)** | Tutte le funzionalità | Nessuna. |
| **Clang** | **100% (Completo)** | Tutte le funzionalità | Nessuna. |
| **Zig** | **100% (Completo)** | Tutte le funzionalità | Nessuna. Usa `zig cc` come compilatore C. |
| **TCC** | **98% (Alto)** | Strutture, Generici, Tratti, Pattern Matching | Niente ASM Intel, Niente `__attribute__((constructor))`. |

</details>

{% alert(type="warning") %}
**AVVISO DI COMPILAZIONE:** Sebbene **Zig CC** funzioni ottimamente come backend per i tuoi programmi Zen C, compilare il *compilatore Zen C stesso* con esso potrebbe verificare ma produrre un binario instabile che fallisce i test. Consigliamo di compilare il compilatore con **GCC** o **Clang** e usare Zig solo come backend per il tuo codice operativo.
{% end %}

{% alert(type="tip") %}
### Buildare con Zig
{% end %}

Il comando `zig cc` di Zig fornisce un rimpiazzamento drop-in per GCC/Clang con eccellente supporto per la cross-compilation. Per usare Zig:

```bash
# Compila ed esegui un programma Zen C con Zig
zc run app.zc --cc zig

# Puoi compilare persino il compilatore Zen C stesso con Zig
make zig
```

### Interop C++

Zen C può generare codice compatibile con C++ utilizzando l'opzione `--cpp`, permettendo una integrazione fluida con le librerie C++.

```bash
# Compilazione diretta con g++
zc app.zc --cpp

# O traspila per le build manuali
zc transpile app.zc --cpp
g++ out.c my_cpp_lib.o -o app
```

#### Usare C++ in Zen C

Includi header C++ e usa blocchi grezzi per codice C++:

```zc
include <vector>
include <iostream>

raw {
    std::vector<int> crea_vettore(int a, int b) {
        return {a, b};
    }
}

fn main() {
    let v = crea_vettore(1, 2);
    raw { std::cout << "Dimensione: " << v.size() << std::endl; }
}
```

> **Nota:** L'opzione `--cpp` rende il backend `g++` ed emette codice valido per C++ (utilizza `auto` al posto di `__auto_type`, overload delle funzioni al posto di `_Generic` e i cast espliciti per `void*`)

#### Interop CUDA

Zen C supporta la programmazione GPU traspilando a **CUDA C++**. Questo ti permette di utilizzare potenti funzionalità C++ (template, `constexpr`) all'interno dei tuoi kernel mantenendo la sintassi ergonomica di Zen C.

```bash
# Compilazione diretta con nvcc
zc run app.zc --cuda

# O traspila per le build manuali
zc transpile app.zc --cuda -o app.cu
nvcc app.cu -o app
```

#### Attributi specifici CUDA

| Attributo | Equivalente CUDA | Descrizione |
|:---|:---|:---|
| `@global` | `__global__` | Function Kernel (esegue sulla GPU, chiamato dall'host) |
| `@device` | `__device__` | Funzione Device (esegue sulla GPU, chiamato dalla GPU) |
| `@host` | `__host__` | Funzione Host (Solo CPU esplicita) |

#### Kernel Launch Syntax

Zen C fornisce un'istruzione chiara `launch` per richiamare kernel CUDA:

```zc
launch kernel_name(args) with {
    grid: num_blocks,
    block: threads_per_block,
    shared_mem: 1024,  // Opzionale
    stream: my_stream   // Opzionale
};
```

Questo traspila a: `kernel_name<<<grid, block, shared, stream>>>(args);` 

#### Scrivere kernel CUDA

Utilizza la sintassi delle funzioni Zen C con `@global` e l'istruzione `launch`:

```zc
import "std/cuda.zc"

@global
fn aggiungi_kernel(a: float*, b: float*, c: float*, n: int) {
    let i = thread_id();
    if i < n {
        c[i] = a[i] + b[i];
    }
}

fn main() {
    def N = 1024;
    let d_a = cuda_alloc<float>(N);
    let d_b = cuda_alloc<float>(N); 
    let d_c = cuda_alloc<float>(N);
    defer cuda_free(d_a);
    defer cuda_free(d_b);
    defer cuda_free(d_c);

    // ... init data ...
    
    launch aggiungi_kernel(d_a, d_b, d_c, N) with {
        grid: (N + 255) / 256,
        block: 256
    };
    
    cuda_sync();
}
```

#### Libreria Standard (`std/cuda.zc`)
Zen C fornisce una libreria standard per delle operazioni comuni in CUDA per ridurre la mole di blocchi `raw` (grezzi):

```zc
import "std/cuda.zc"

// Gestione della memoria
let d_ptr = cuda_alloc<float>(1024);
cuda_copy_to_device(d_ptr, h_ptr, 1024 * sizeof(float));
defer cuda_free(d_ptr);

// Sincronizzazione
cuda_sync();

// Indicizzazione dei thread (usa all'interno del kernel)
let i = thread_id(); // Indice globale
let bid = block_id();
let tid = local_id();
```

{% alert(type="note") %}
**Nota:** La flag `--cuda` imposta `nvcc` come compilatore e implica la modalità `--cpp`. Richiede l'installazione dell'NVIDIA CUDA Toolkit.
{% end %}

### Supporto C23

Zen C supporta le funzionalità moderne dello standard C23 quando si usa un backend compatibile (GCC 14+, Clang 14+, _TCC_ (_parziale_)).

- **`auto`**: Zen C mappa automaticamente l'inferenza del tipo alla keyword `auto` di C23 (se `__STDC_VERSION__ >= 202300L`).
- **`_BitInt(N)`**: Usa i tipi `iN` e `uN` (e.g., `i256`, `u12`, `i24`) per accedere agli interi di lunghezza arbitraria di C23.

### Interop Objective-C

Zen C può compilare a Objective-C (`.m`) utilizzando la flag `--objc`, permettendoti di utilizzare i framework (come Cocoa/Foundation) e la sintassi Obj-C

```bash
# Compila con clang (o gcc/gnustep)
zc app.zc --objc --cc clang
```

#### Usando l'Objective-C in Zen C

Utilizza `include` per gli header e i blocchi `raw` per la sintassi Obj-C (`@interface`, `[...]`, `@""`).

```zc
//> macos: framework: Foundation
//> linux: cflags: -fconstant-string-class=NSConstantString -D_NATIVE_OBJC_EXCEPTIONS
//> linux: link: -lgnustep-base -lobjc

include <Foundation/Foundation.h>

fn main() {
    raw {
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        NSLog(@"Ciao da Objective-C!");
        [pool drain];
    }
    println "Funziona anche Zen C!";
}
```

{% alert(type="note") %}
**Nota:** L'interpolazione delle stringhe di Zen C funziona con gli oggetti dell'Objective-C (`id`) chiamando `debugDescription` oppure `description`.
{% end %}

---

## Contribuisci

Qui accogliamo tutti i contributi! Che siano fix di bug, miglioramenti alla documentazione, o la proposta di nuove funzionalità.

Per favore, consulta [CONTRIBUTING_IT.md](CONTRIBUTING_IT.md) per le linee guida dettagliate su come contribuire, eseguire i test e inviare pull request.

---

## Sicurezza

Per istruzioni sulla segnalazione di vulnerabilità, vedi [SECURITY_IT.md](SECURITY_IT.md).

---

## Attribuzioni

Questo progetto utilizza librerie esterne. I testi di licenza completi possono essere trovati nella directory `LICENSES/`.

* **[cJSON](https://github.com/DaveGamble/cJSON)** (Licenza MIT): Usato per il parsing e la generazione di JSON nel Language Server.
* **[zc-ape](https://github.com/OEvgeny/zc-ape)** (Licenza MIT): La versione originale di Actually Portable Executable di Zen-C, realizzata da [Eugene Olonov](https://github.com/OEvgeny).
* **[Cosmopolitan Libc](https://github.com/jart/cosmopolitan)** (Licenza ISC): La libreria fondamentale che rende possibile APE.
* **[TRE](https://github.com/laurikari/tre)** (Licenza BSD): Usato per il motore di espressioni regolari nella libreria standard.
* **[zenc.vim](https://github.com/zenc-lang/zenc.vim)** (Licenza MIT): Il plugin ufficiale per Vim/Neovim, scritto principalmente da **[davidscholberg](https://github.com/davidscholberg)**.

---

<div align="center">
  <p>
    Copyright © 2026 Zen C Programming Language.<br>
    Inizia il tuo viaggio oggi.
  </p>
  <p>
    <a href="https://discord.com/invite/q6wEsCmkJP">Discord</a> •
    <a href="https://github.com/zenc-lang/zenc">GitHub</a> •
    <a href="https://github.com/zenc-lang/docs">Documentazione</a> •
    <a href="https://github.com/zenc-lang/awesome-zenc">Esempi</a> •
    <a href="https://github.com/zenc-lang/rfcs">RFC</a> •
    <a href="CONTRIBUTING_IT.md">Contribuisci</a>
  </p>
</div>

