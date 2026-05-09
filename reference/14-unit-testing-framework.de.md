+++
title = "14. Unit-Testing-Framework"
weight = 14
+++

# 14. Unit-Testing-Framework



Zen C bietet ein eingebautes Test-Framework, um Unit-Tests direkt in den Quellcode-Dateien zu schreiben, mittels des `test`-Schlüsselworts.

#### Syntax
Ein `test`-Block enthält einen beschreibenden Namen und einen Codeblock, der ausgeführt wird. Es wird keine `main`-Funktion benötigt.

```zc
test "unittest1" {
    "Dies ist ein Unit-Test";

    let a = 3;
    assert(a > 0, "a sollte eine positive Zahl sein");

    "unittest1 erfolgreich.";
}
```


#### Tests ausführen

```bash
zc run meine_datei.zc
```

Die Ausgabe zeigt jeden Test mit Namen:
```
  TEST: beschreibender Name ... OK
  TEST: weiterer Test ... FEHLGESCHLAGEN

1 test(s) failed
```

#### Assertions

| Funktion | Verhalten |
|:---|:---|
| `assert(cond, msg)` | Zeichnet Fehler auf, fährt mit nächstem Test fort |
| `expect(cond, msg)` | Nicht-fatale Assertion — zeichnet Fehler auf, fährt im selben Test fort |

```zc
test "beispiel" {
    expect(ergebnis != null, "ergebnis sollte nicht null sein");
    expect(code == 200, "status sollte 200 sein");
}
```

#### Exit-Code

Das Binary beendet sich mit der Anzahl fehlgeschlagener Tests (0 = alle bestanden).
