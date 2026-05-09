+++
title = "14. Marco de Pruebas Unitarias"
weight = 14
+++

# 14. Marco de Pruebas Unitarias


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


#### Ejecutar pruebas

```bash
zc run mi_archivo.zc
```

La salida muestra cada prueba por nombre:
```
  TEST: nombre descriptivo ... OK
  TEST: otra prueba ... FALLIDA

1 test(s) failed
```

#### Aserciones

| Función | Comportamiento |
|:---|:---|
| `assert(cond, msg)` | Registra el fallo, continúa con la siguiente prueba |
| `expect(cond, msg)` | No fatal — registra el fallo pero continúa dentro de la misma prueba |

```zc
test "ejemplo" {
    expect(resultado != null, "el resultado no debería ser nulo");
    expect(codigo == 200, "el estado debería ser 200");
}
```

#### Código de salida

El binario termina con el número de pruebas fallidas (0 = todas aprobadas).
