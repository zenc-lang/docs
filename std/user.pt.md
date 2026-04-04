# std/sys/user

O módulo `std/sys/user` fornece acesso a informações de identificação de utilizador e grupo, envolvendo o `unistd.h` do POSIX.

## Visão Geral

- **Identidade de Utilizador**: Recupere IDs de utilizador (UID) e IDs de grupo (GID) reais e efetivos.
- **Contexto de Processo**: Útil para verificação de privilégios e gerenciamento de permissões em utilitários de sistema.

## Uso

```zc
import "std/sys/user.zc"
import "std/io.zc"

fn main() {
    println "UID atual: {User::get_uid()}";
    println "GID atual: {User::get_gid()}";
    
    if (User::get_euid() == 0) {
        println "A executar com privilégios de root.";
    }
}
```

## Definição da Estrutura

```zc
struct User {}
```

## Métodos

### Métodos de `User`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **get_uid** | `User::get_uid() -> u32` | Retorna o ID de utilizador real do processo atual. |
| **get_gid** | `User::get_gid() -> u32` | Retorna o ID de grupo real do processo atual. |
| **get_euid** | `User::get_euid() -> u32` | Retorna o ID de utilizador efetivo. |
| **get_egid** | `User::get_egid() -> u32` | Retorna o ID de grupo efetivo. |
走
