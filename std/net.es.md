# std/net

El módulo `std/net` proporciona una pila de red completa que incluye TCP, UDP, DNS y HTTP.

## Uso

```zc
import "std/net/tcp.zc"  // TcpStream, TcpListener
import "std/net/udp.zc"  // UdpSocket
import "std/net/http.zc" // Cliente/Servidor HTTP
import "std/net/dns.zc"  // Resolución DNS
import "std/net/url.zc"  // Análisis de URL
import "std/net/websocket.zc" // WebSocket
```

## WebSocket (`std/net/websocket.zc`)

### Tipo `WebSocket`

Proporciona el protocolo de enlace (handshake) y el entramado (framing) de WebSocket en el lado del servidor.

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **handshake** | `WebSocket::handshake(stream: TcpStream, key: String) -> Result<WebSocket>` | Realiza el protocolo de enlace en el lado del servidor. |
| **recv** | `recv(self) -> Result<String>` | Recibe un marco de texto (maneja el desenmascaramiento). |
| **send** | `send(self, msg: String) -> Result<int>` | Envía un marco de texto. |

## Cliente y Servidor HTTP (`std/net/http.zc`)

### Tipo `Server`

Un servidor HTTP sencillo con capacidad multihilo.

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Server::new(port: int, handler: fn(Request*, Response*)) -> Server` | Crea un nuevo servidor HTTP. |
| **start** | `start(self)` | Inicia el bucle de escucha del servidor. |

### Cliente `fetch`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **fetch** | `fetch(url: String) -> Response` | Realiza una petición GET. |

## Análisis de URL (`std/net/url.zc`)

### Tipo `Url`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **parse** | `Url::parse(s: String) -> Option<Url>` | Analiza una cadena de URL. |

## TCP (`std/net/tcp.zc`)

### Tipo `TcpListener`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **bind** | `TcpListener::bind(host: char*, port: int) -> Result<TcpListener>` | Se vincula a una dirección local. |
| **accept** | `accept(self) -> Result<TcpStream>` | Acepta una nueva conexión. |

### Tipo `TcpStream`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **connect** | `TcpStream::connect(host: char*, port: int) -> Result<TcpStream>` | Se conecta a un host remoto. |
| **read** | `read(self, buf: char*, len: usize) -> Result<usize>` | Lee del flujo (stream). |
| **write** | `write(self, buf: u8*, len: usize) -> Result<usize>` | Escribe en el flujo (stream). |

## UDP (`std/net/udp.zc`)

### Tipo `UdpSocket`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **bind** | `UdpSocket::bind(host: char*, port: int) -> Result<UdpSocket>` | Se vincula a una dirección local. |
| **recv_from** | `recv_from(self, buf: char*, len: usize) -> Result<UdpRecvResult>` | Recibe datos e información del remitente. |
| **send_to** | `send_to(self, buf: char*, len: usize, host: char*, port: int) -> Result<usize>` | Envía datos a un destino específico. |

## DNS (`std/net/dns.zc`)

### Tipo `Dns`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **resolve** | `Dns::resolve(host: char*) -> Result<String>` | Resuelve un nombre de host a una dirección IP. |
