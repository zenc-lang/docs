+++
title = "14. Framework di Test Unitari"
weight = 14
+++

# 14. Framework di Test Unitari


Zen C include un framework di test integrato con **isolamento per-test**, **output nominativo**, e **asserzioni non-fatali**.

#### Sintassi
Un blocco `test` contiene un nome descrittivo e un corpo di codice da eseguire.

```zc
test "nome descrittivo" {
    let a = 3;
    assert(a > 0, "a dovrebbe essere positivo");
}
```

#### Esecuzione dei Test
```bash
zc run mio_file.zc
```

L'output mostra ogni test per nome:
```
  TEST: nome descrittivo ... OK
  TEST: altro test ... FALLITO

1 test(s) failed
```

#### Asserzioni

| Funzione | Comportamento |
|:---|:---|
| `assert(cond, msg)` | Registra il fallimento, continua al test successivo |
| `expect(cond, msg)` | Non-fatale — registra il fallimento ma continua nello stesso test |

```zc
test "esempio" {
    expect(risultato != null, "il risultato non dovrebbe essere nullo");
    expect(codice == 200, "lo stato dovrebbe essere 200");
}
```

#### Codice di uscita
Il binario termina con il numero di test falliti (0 = tutti superati).
