+++
title = "15. Sistema de Diagnóstico"
weight = 15
+++

# 15. Sistema de Diagnóstico


Zen C presenta un sistema de diagnóstico categorizado que proporciona un control granular sobre las advertencias del compilador. Esto ayuda a mantener altos estándares de calidad del código al tiempo que reduce la fricción al interactuar con código C externo.

#### Categorías de Diagnóstico

Las advertencias se agrupan en categorías lógicas. Cada categoría puede habilitarse o deshabilitarse globalmente mediante indicadores del compilador.

| Categoría | Descripción | Por defecto |
| :--- | :--- | :--- |
| **`INTEROP`** | Advertencias relacionadas con las importaciones de cabeceras C y funciones externas no definidas. | **OFF** |
| **`PEDANTIC`** | Comprobaciones extra rigurosas para problemas potenciales o calidad del código. | **OFF** |
| **`UNUSED`** | Advertencias para variables, parámetros o funciones definidos pero no utilizados. | **ON** |
| **`SAFETY`** | Advertencias críticas de seguridad como el acceso a punteros nulos o la división por cero. | **ON** |
| **`LOGIC`** | Advertencias relacionadas con la lógica, como código inalcanzable o comparaciones de constantes. | **ON** |
| **`CONVERSION`** | Advertencias para conversiones de tipo implícitas o restrictivas. | **ON** |
| **`STYLE`** | Advertencias sobre el estilo de codificación, como el sombreado de variables (shadowing). | **ON** |

#### Indicadores del Compilador

Puedes controlar los diagnósticos utilizando las flags `-W` (activar) y `-Wno-` (desactivar) seguidas del nombre de una categoría o de un ID de diagnóstico específico.

##### Indicadores de Categoría

- `-Winterop`: Activa todas las advertencias relacionadas con la interoperabilidad.
- `-Wno-unused`: Silencia específicamente las advertencias por variables/parámetros no utilizados.
- `-Wsafety`: Asegura que todas las comprobaciones de seguridad estén activas.
- `-Wall`: Activa todas las categorías de diagnóstico principales.
- `-Wextra`: Activa diagnósticos aún más rigurosos (equivalente a `-Wpedantic`).

##### Ejemplo de Uso

```bash
# Compilar con las advertencias de interoperabilidad C activadas
zc app.zc -Winterop

# Compilar con todas las advertencias activadas excepto para el código no utilizado
zc app.zc -Wall -Wno-unused
```

#### Fricción en la Interoperabilidad C

Por defecto, Zen C suprime las advertencias de "Función no definida" para las funciones que probablemente se encuentren en las bibliotecas estándar de C (la categoría `INTEROP` está **OFF**).

Si deseas que el compilador marque estrictamente cada función no definida (por ejemplo, para detectar errores tipográficos), activa la categoría interop:

```bash
zc main.zc -Winterop
```

Cuando está activada, el compilador proporcionará sugerencias útiles para las funciones comunes de C:
```text
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

#### Whitelisting

Si utilizas con frecuencia una biblioteca C específica y deseas mantener `-Winterop` activado sin que te molesten funciones específicas, puedes añadirlas a la `c_function_whitelist` en el archivo de configuración `zenc.json`.

## Further Reading

- **Language Server**: Consulte la [documentación LSP](LSP.md) para la integración con el editor.
- **MISRA Compliance**: Consulte [MISRA Rules](../reference/16-misra-rules) para la referencia completa de reglas.
- **Contributing**: Consulte [CONTRIBUTING_ES.md](../CONTRIBUTING_ES.md) para las pautas de contribución.
