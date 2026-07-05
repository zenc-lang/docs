+++
title = "15. Unit-Testing-Framework"
weight = 15
+++

# 15. Unit-Testing-Framework {#15-unit-testing-framework}



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
Um alle Tests einer Datei auszuführen, nutze den `run`-Befehl. Der Compiler erkennt automatisch alle top-level `test`-Blöcke.

```bash
zc run my_file.zc
```

#### Assertions
Verwende die eingebaute Funktion `assert(condition, message)` zur Überprüfung von Erwartungen. Wenn die Bedingung falsch ist, schlägt der Test fehl und die Nachricht wird ausgegeben.

---
