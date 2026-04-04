# std/map

`Map<K, V>` é uma estrutura de dados de tabela hash genérica que associa chaves do tipo `K` a valores do tipo `V`. Utiliza encadeamento (chaining) para resolução de colisões e suporta redimensionamento automático.

## Visão Geral

- **Genérico**: Suporta qualquer tipo para chaves e valores.
- **Diferentes Implementações**: Fornece `StringMap<V>` otimizado para chaves de string e um `Map<K, V>` genérico.
- **Redimensionamento Automático**: Expande a capacidade conforme necessário para manter a eficiência.
- **RAII**: O trait `Drop` gerencia a libertação de memória de todos os elementos e da estrutura interna.

## Uso

```zc
import "std/map.zc"

fn main() {
    let m = StringMap<int>::new();
    
    // Inserir valores
    m.insert("tecla", 100);
    m.insert("outra", 200);
    
    // Recuperar valor (retorna Option<T>)
    match m.get("tecla") {
        Some(v) => println "Valor: {v}",
        None    => println "Chave não encontrada"
    }
} // m é libertado automaticamente aqui
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Map<K, V>::new() -> Map<K, V>` | Cria um novo mapa vazio. |

### Modificação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **insert** | `insert(self, key: K, val: V)` | Adiciona ou atualiza um par chave-valor. |
| **remove** | `remove(self, key: K) -> bool` | Remove a entrada da chave. Retorna true se existia. |
| **clear** | `clear(self)` | Remove todas as entradas do mapa. |

### Acesso & Consulta

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **get** | `get(self, key: K) -> Option<V>` | Retorna uma cópia do valor associado à chave. |
| **get_ref** | `get_ref(self, key: K) -> V*` | Retorna um ponteiro para o valor (evita cópias). |
| **contains**| `contains(self, key: K) -> bool` | Verifica se a chave existe no mapa. |
| **length** | `length(self) -> usize` | Retorna o número de entradas. |
| **is_empty** | `is_empty(self) -> bool` | Retorna true se o mapa estiver vazio. |

## Iteração

O Zen-C suporta a iteração sobre mapas no estilo chave-valor:

```zc
for k, v in m {
    println "Chave: {k}, Valor: {v}";
}
```

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **free** | `free(self)` | Liberta manualmente a memória interna. |
| **Trait** | `impl Drop for Map` | Chama automaticamente `free()`. |
走
