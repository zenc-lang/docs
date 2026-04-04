# std/json

O módulo `std/json` fornece uma interface poderosa e fácil de usar para trabalhar com dados no formato JSON (JavaScript Object Notation). Suporta parsing, geração e manipulação de tipos JSON através de uma API estruturada.

## Visão Geral

- **Parsing**: Converte uma string JSON numa árvore de objetos `JsonValue`.
- **Geração**: Converte objetos `JsonValue` de volta para strings JSON.
- **Tipagem Segura**: Suporte para todos os tipos JSON (String, Number, Object, Array, Boolean, Null).
- **RAII**: Gerencia automaticamente a memória de toda a árvore JSON através do trait `Drop`.

## Uso

```zc
import "std/json.zc"

fn main() {
    let raw = "{\"id\": 1, \"name\": \"Zen\", \"tags\": [\"lang\", \"c\"]}";
    
    // Parsing
    match Json::parse(raw) {
        Ok(v) => {
            println "ID: {v.get(\"id\").as_int()}";
            println "Nome: {v.get(\"name\").as_string().c_str()}";
        }
        Err(e) => println "Erro no parsing: {e}"
    }
} // A árvore JSON é libertada automaticamente aqui
```

## Tipo `JsonValue`

O tipo central que representa qualquer valor JSON.

### Extração de Valores

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **as_int** | `as_int(self) -> int` | Retorna o valor como inteiro. |
| **as_string** | `as_string(self) -> String` | Retorna o valor como uma `String`. |
| **as_bool** | `as_bool(self) -> bool` | Retorna o valor como booleano. |
| **at** | `at(self, index: usize) -> JsonValue*` | Acede a um elemento de um array por índice. |
| **get** | `get(self, key: char*) -> JsonValue*` | Acede a um valor de um objeto por chave. |

### Verificação de Tipos

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **is_object** | `is_object(self) -> bool` | Retorna true se for um Objeto. |
| **is_array** | `is_array(self) -> bool` | Retorna true se for um Array. |
| **is_null** | `is_null(self) -> bool` | Retorna true se for Null. |

## Métodos de `Json` (Geração e Parsing)

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **parse** | `Json::parse(s: char*) -> Result<JsonValue>` | Faz o parsing de uma string JSON. |
| **stringify**| `Json::stringify(v: JsonValue*) -> String` | Converte um `JsonValue` para uma string. |

## Construção Programática

```zc
let obj = JsonValue::new_object();
obj.set("servidor", JsonValue::new_string("ativo"));
obj.set("porta", JsonValue::new_int(8080));
```

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **free** | `free(self)` | Liberta manualmente a memória de um `JsonValue` e de todos os seus filhos. |
| **Trait** | `impl Drop for JsonValue` | Chama automaticamente `free()` quando o objeto sai do escopo. |
走
