# std/option

`Option<T>` representa um valor opcional: cada `Option` é `Some` e contém um valor, ou `None`. É comummente utilizado para lidar com a ausência de um valor sem recorrer a ponteiros nulos.

## Visão Geral

- **Seguro**: Incentiva o tratamento explícito do caso `None`.
- **Genérico**: Pode envolver qualquer tipo `T`.
- **Custo Zero**: Compila para uma estrutura simples com um marcador booleano.
- **Conveniente**: Fornece muitos métodos utilitários para extrair e transformar valores.

## Uso

```zc
import "std/option.zc"

fn main() {
    let val = Option<int>::Some(10);
    
    if (val.is_some()) {
        println "O valor é {val.unwrap()}";
    }
    
    let vazio = Option<int>::None();
    let x = vazio.unwrap_or(0);
}
```

## Definição da Estrutura

```zc
struct Option<T> {
    is_some: bool;
    val: T;
}
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **Some** | `Option<T>::Some(v: T) -> Option<T>` | Cria uma opção `Some` contendo `v`. |
| **None** | `Option<T>::None() -> Option<T>` | Cria uma opção `None`. |

### Consulta

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **is_some** | `is_some(self) -> bool` | Retorna `true` se a opção for `Some`. |
| **is_none** | `is_none(self) -> bool` | Retorna `true` se a opção for `None`. |

### Extração

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **unwrap** | `unwrap(self) -> T` | Retorna o valor contido. Entra em pânico se for `None`. |
| **unwrap_ref** | `unwrap_ref(self) -> T*` | Retorna um ponteiro para o valor contido. Entra em pânico se for `None`. |
| **unwrap_or** | `unwrap_or(self, def: T) -> T` | Retorna o valor contido ou `def`. |
| **expect** | `expect(self, msg: char*) -> T` | Retorna o valor ou entra em pânico com `msg`. |
| **or_else** | `or_else(self, other: Option<T>) -> Option<T>` | Retorna a opção se for `Some`, caso contrário retorna `other`. |

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **forget** | `forget(self)` | Limpa o valor interno sem chamar destruidores ou libertar memória. |
走
