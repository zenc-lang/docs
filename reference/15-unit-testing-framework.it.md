+++
title = "15. Framework di Test Unitari"
weight = 15
+++

# 15. Framework di Test Unitari {#15-framework-di-test-unitari}


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
