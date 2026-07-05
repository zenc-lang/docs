+++
title = "15. Marco de Pruebas Unitarias"
weight = 15
+++

# 15. Marco de Pruebas Unitarias {#15-marco-de-pruebas-unitarias}


Zen C incluye un marco de pruebas integrado que permite escribir pruebas unitarias directamente en los archivos fuente utilizando la palabra clave `test`.

#### Sintaxis
Un bloque `test` contiene un nombre descriptivo y un cuerpo de código para ejecutar. Las pruebas no requieren una función `main` para ejecutarse.

```zc
test "unittest1" {
    "Esta es una prueba unitaria";

    let a = 3;
    assert(a > 0, "a debería ser un entero positivo");

    "unittest1 pasado.";
}
```

#### Ejecución de Pruebas
Para ejecutar todas las pruebas en un archivo, usa el comando `run`. El compilador detectará y ejecutará automáticamente todos los bloques `test` de nivel superior.

```bash
zc run mi_archivo.zc
```

#### Aserciones
Usa la función integrada `assert(condición, mensaje)` para verificar las expectativas. Si la condición es falsa, la prueba fallará y se imprimirá el mensaje proporcionado.

---
