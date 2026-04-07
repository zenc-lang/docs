+++
title = "15. Sistema de Diagnóstico"
weight = 15
+++

# 15. Sistema de Diagnóstico

Zen C cuenta con un sistema de diagnóstico categorizado que proporciona un control granular sobre las advertencias del compilador. Esto le permite mantener altos estándares de calidad de código mientras reduce la fricción al interactuar con código C externo.

## Categorías de Diagnóstico

Las advertencias se agrupan en categorías lógicas. Cada categoría se puede activar o desactivar globalmente mediante indicadores (flags) del compilador.

| Categoría | Descripción | Por defecto |
| :--- | :--- | :--- |
| **`INTEROP`** | Advertencias relacionadas con la importación de encabezados C y funciones externas no definidas. | **OFF** |
| **`PEDANTIC`** | Comprobaciones extra estrictas para posibles problemas o calidad del código. | **OFF** |
| **`UNUSED`** | Advertencias para variables, parámetros o funciones definidos pero no utilizados. | **ON** |
| **`SAFETY`** | Advertencias de seguridad críticas, como acceso a punteros nulos o división por cero. | **ON** |
| **`LOGIC`** | Advertencias relacionadas con la lógica, como código inalcanzable o comparaciones de constantes. | **ON** |
| **`CONVERSION`** | Advertencias para conversiones de tipo implícitas o de reducción. | **ON** |
| **`STYLE`** | Advertencias de estilo de codificación, como el sombreado de variables (shadowing). | **ON** |

## Indicadores del Compilador

Puede controlar los diagnósticos utilizando los indicadores `-W` (activar) y `-Wno-` (desactivar) seguidos del nombre de una categoría o un ID de diagnóstico específico.

### Indicadores de Categoría

- `-Winterop`: Activa todas las advertencias relacionadas con la interoperabilidad.
- `-Wno-unused`: Silencia específicamente las advertencias de variables/parámetros no utilizados.
- `-Wsafety`: Asegura que todas las comprobaciones de seguridad estén activas.
- `-Wall`: Activa todas las categorías de diagnóstico principales.
- `-Wextra`: Activa diagnósticos aún más estrictos (equivalente a `-Wpedantic`).

### Ejemplo de Uso

```bash
# Compilar con las advertencias de interoperabilidad de C activadas
zc app.zc -Winterop

# Compilar con todas las advertencias activadas excepto las de código no utilizado
zc app.zc -Wall -Wno-unused
```

## Fricción de Interoperabilidad con C

Por defecto, Zen C suprime las advertencias de "Función no definida" para funciones que probablemente se encuentren en las bibliotecas estándar de C (la categoría `INTEROP` está **OFF**).

Si desea que el compilador informe estrictamente sobre cada función no definida (por ejemplo, para detectar errores tipográficos), active la categoría de interoperabilidad:

```bash
zc main.zc -Winterop
```

Cuando está activada, el compilador proporcionará sugerencias útiles para funciones C comunes:
```text
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

## Lista Blanca (Whitelisting)

Si utiliza una biblioteca C específica con frecuencia y desea mantener `-Winterop` activado sin que le molesten funciones específicas, puede añadirlas a la `c_function_whitelist` en su archivo de configuración `zenc.json`.
