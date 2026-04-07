+++
title = "15. Sistema di Diagnostica"
weight = 15
+++

# 15. Sistema di Diagnostica

Zen C presenta un sistema di diagnostica categorizzato che fornisce un controllo granulare sugli avvisi (warning) del compilatore. Ciò consente di mantenere elevati standard di qualità del codice riducendo al contempo l'attrito durante l'interazione con il codice C esterno.

## Categorie di Diagnostica

Gli avvisi sono raggruppati in categorie logiche. Ogni categoria può essere abilitata o disabilitata globalmente utilizzando i flag del compilatore.

| Categoria | Descrizione | Default |
| :--- | :--- | :--- |
| **`INTEROP`** | Avvisi relativi all'importazione di header C e funzioni esterne non definite. | **OFF** |
| **`PEDANTIC`** | Controlli extra rigorosi per potenziali problemi o qualità del codice. | **OFF** |
| **`UNUSED`** | Avvisi per variabili, parametri o funzioni definiti ma non utilizzati. | **ON** |
| **`SAFETY`** | Avvisi critici sulla sicurezza come l'accesso a puntatori nulli o la divisione per zero. | **ON** |
| **`LOGIC`** | Avvisi relativi alla logica come codice irraggiungibile o confronti tra costanti. | **ON** |
| **`CONVERSION`** | Avvisi per conversioni di tipo implicite o restrittive. | **ON** |
| **`STYLE`** | Avvisi sullo stile di codifica come l'oscuramento delle variabili (shadowing). | **ON** |

## Flag del Compilatore

È possibile controllare la diagnostica utilizzando i flag `-W` (abilita) e `-Wno-` (disabilita) seguiti dal nome di una categoria o da un ID diagnostico specifico.

### Flag di Categoria

- `-Winterop`: Abilita tutti gli avvisi relativi all'interoperabilità.
- `-Wno-unused`: Silenzia specificamente gli avvisi per variabili/parametri non utilizzati.
- `-Wsafety`: Assicura che tutti i controlli di sicurezza siano attivi.
- `-Wall`: Abilita tutte le principali categorie diagnostiche.
- `-Wextra`: Abilita diagnostiche ancora più rigorose (equivalente a `-Wpedantic`).

### Esempio di Utilizzo

```bash
# Compila con gli avvisi di interoperabilità C abilitati
zc app.zc -Winterop

# Compila con tutti gli avvisi abilitati tranne quelli per il codice non utilizzato
zc app.zc -Wall -Wno-unused
```

## Attrito nell'Interoperabilità C

Per impostazione predefinita, Zen C sopprime gli avvisi di "Funzione non definita" per le funzioni che probabilmente si trovano nelle librerie standard C (la categoria `INTEROP` è **OFF**).

Se si desidera che il compilatore segnali rigorosamente ogni funzione non definita (ad esempio, per individuare refusi), abilitare la categoria interop:

```bash
zc main.zc -Winterop
```

Quando abilitata, il compilatore fornirà suggerimenti utili per le comuni funzioni C:
```text
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

## Whitelisting

Se si utilizza frequentemente una specifica libreria C e si desidera mantenere `-Winterop` abilitato senza essere disturbati da funzioni specifiche, è possibile aggiungerle alla `c_function_whitelist` nel file di configurazione `zenc.json`.
