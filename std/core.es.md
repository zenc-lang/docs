# std/core

El módulo `std/core` proporciona las definiciones más fundamentales y las primitivas de manejo de errores para los programas Zen-C. Es requerido implícitamente por la mayoría de las otras bibliotecas estándar.

## Resumen

- **Cabeceras Estándar**: Incluye cabeceras C críticas como `stdlib.h`, `stdio.h`, y `stdbool.h`.
- **Mecanismo de Panic**: Proporciona la macro `panic` para el informe de errores fatales.
- **Control de Procesos**: Incluye funciones básicas de control de procesos como `exit`.

## Métodos

### Manejo de Errores

| Método/Macro | Firma | Descripción |
| :--- | :--- | :--- |
| **panic** | `panic(msg: char*)` | Imprime un mensaje de error formateado que incluye el archivo, la línea y la función, y luego termina el proceso. |

### Control de Procesos

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **exit** | `exit(code: int)` | Termina inmediatamente el proceso con el código de retorno dado. |
