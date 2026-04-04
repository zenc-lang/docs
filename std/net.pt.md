# std/net

O módulo `std/net` fornece uma stack completa de rede, incluindo TCP, UDP, DNS e HTTP.

## Uso

```zc
import "std/net/tcp.zc"  // TcpStream, TcpListener
import "std/net/udp.zc"  // UdpSocket
import "std/net/http.zc" // Cliente/Servidor HTTP
import "std/net/dns.zc"  // Resolução DNS
import "std/net/url.zc"  // Parsing de URL
import "std/net/websocket.zc" // WebSocket
```

## WebSocket (`std/net/websocket.zc`)

### Tipo `WebSocket`

Fornece aperto de mão (handshake) e enquadramento (framing) de WebSocket do lado do servidor.

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **handshake** | `WebSocket::handshake(stream: TcpStream, key: String) -> Result<WebSocket>` | Realiza o handshake do lado do servidor. |
| **recv** | `recv(self) -> Result<String>` | Recebe um frame de texto (gera o unmasking). |
| **send** | `send(self, msg: String) -> Result<int>` | Envia um frame de texto. |

## Cliente e Servidor HTTP (`std/net/http.zc`)

### Tipo `Server`

Um servidor HTTP simples com capacidade multithread.

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Server::new(port: int, handler: fn(Request*, Response*)) -> Server` | Cria um novo servidor HTTP. |
| **start** | `start(self)` | Inicia o ciclo de escuta do servidor. |

### Cliente `fetch`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **fetch** | `fetch(url: String) -> Response` | Realiza uma requisição GET. |

## Parsing de URL (`std/net/url.zc`)

### Tipo `Url`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **parse** | `Url::parse(s: String) -> Option<Url>` | Processa uma string de URL. |

## TCP (`std/net/tcp.zc`)

### Tipo `TcpListener`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **bind** | `TcpListener::bind(host: char*, port: int) -> Result<TcpListener>` | Associa-se a um endereço local. |
| **accept** | `accept(self) -> Result<TcpStream>` | Aceita uma nova conexão. |

### Tipo `TcpStream`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **connect** | `TcpStream::connect(host: char*, port: int) -> Result<TcpStream>` | Conecta-se a um host remoto. |
| **read** | `read(self, buf: char*, len: usize) -> Result<usize>` | Lê do fluxo (stream). |
| **write** | `write(self, buf: u8*, len: usize) -> Result<usize>` | Escreve no fluxo (stream). |

## UDP (`std/net/udp.zc`)

### Tipo `UdpSocket`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **bind** | `UdpSocket::bind(host: char*, port: int) -> Result<UdpSocket>` | Associa-se a um endereço local. |
| **recv_from** | `recv_from(self, buf: char*, len: usize) -> Result<UdpRecvResult>` | Recebe dados e informações do remetente. |
| **send_to** | `send_to(self, buf: char*, len: usize, host: char*, port: int) -> Result<usize>` | Envia dados para um destino específico. |

## DNS (`std/net/dns.zc`)

### Tipo `Dns`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **resolve** | `Dns::resolve(host: char*) -> Result<String>` | Resolve um nome de host para um endereço IP. |
走
