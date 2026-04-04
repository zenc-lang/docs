# std/process

El módulo `std/process` proporciona una API de alto nivel para generar procesos hijos, ejecutar comandos del sistema y capturar su salida.

## Resumen

- **Patrón Constructor**: La estructura `Command` utiliza un patrón constructor fluido para construir líneas de comandos.
- **Captura de Salida**: capture fácilmente la salida estándar y los códigos de salida de los procesos finalizados.
- **RAII**: Tanto `Command` como `Output` implementan el rasgo `Drop` para la limpieza automática de los búferes internos.
- **Interoperabilidad Estándar**: Envuelve sin problemas la manipulación de procesos a nivel de sistema subyacente.

## Uso

```zc
import "std/process.zc"

fn main() {
    // Ejecución básica de comandos
    let output = Command::new("echo")
        .arg("hola mundo")
        .output();
        
    if (output.exit_code == 0) {
        println "Capturado: {output.std_out}";
        // output.std_out es una String, se libera automáticamente
    } else {
        println "El comando falló con el código {output.exit_code}";
    }
}
```

## Definiciones de Estructura

### `Command`
Un constructor para configurar y generar un proceso.
```zc
struct Command {
    program: String;
    args: Vec<String>;
}
```

### `Output`
El resultado de una ejecución de proceso completada.
```zc
struct Output {
    std_out: String;
    exit_code: int;
}
```

## Métodos

### Métodos de `Command`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Command::new(program: char*) -> Command` | Crea un nuevo `Command` para el programa dado. |
| **arg** | `arg(self, arg: char*) -> Command*` | Añade un argumento y devuelve un puntero a sí mismo para encadenar. |
| **output** | `output(self) -> Output` | Ejecuta el comando y espera su finalización, capturando la salida estándar (stdout). |
| **status** | `status(self) -> int` | Ejecuta el comando y devuelve el código de estado de salida. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera manualmente los búferes de comando internos. |
| **Trait** | `impl Drop for Command` | Limpia automáticamente los búferes de comando. |
| **Trait** | `impl Drop for Output` | Libera automáticamente la cadena de salida capturada. |
