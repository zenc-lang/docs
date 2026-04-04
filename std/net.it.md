# std/net

Il modulo `std/net` fornisce uno stack di rete completo che include TCP, UDP, DNS e HTTP.

## Utilizzo

```zc
import "std/net/tcp.zc"  // TcpStream, TcpListener
import "std/net/udp.zc"  // UdpSocket
import "std/net/http.zc" // Client/Server HTTP
import "std/net/dns.zc"  // Risoluzione DNS
import "std/net/url.zc"  // Parsing URL
import "std/net/websocket.zc" // WebSocket
```

## WebSocket (`std/net/websocket.zc`)

### Tipo `WebSocket`

Fornisce l'handshake e il framing WebSocket lato server.

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **handshake** | `WebSocket::handshake(stream: TcpStream, key: String) -> Result<WebSocket>` | Esegue l'handshake lato server. |
| **recv** | `recv(self) -> Result<String>` | Riceve un frame di testo (gestisce l'unmasking). |
| **send** | `send(self, msg: String) -> Result<int>` | Invia un frame di testo. |

## Client e Server HTTP (`std/net/http.zc`)

### Tipo `Server`

Un semplice server HTTP con capacità multithread.

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Server::new(port: int, handler: fn(Request*, Response*)) -> Server` | Crea un nuovo server HTTP. |
| **start** | `start(self)` | Avvia il ciclo di ascolto del server. |

### Client `fetch`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **fetch** | `fetch(url: String) -> Response` | Esegue una richiesta GET. |

## Parsing URL (`std/net/url.zc`)

### Tipo `Url`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **parse** | `Url::parse(s: String) -> Option<Url>` | Esegue il parsing di una stringa URL. |

## TCP (`std/net/tcp.zc`)

### Tipo `TcpListener`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **bind** | `TcpListener::bind(host: char*, port: int) -> Result<TcpListener>` | Si associa a un indirizzo locale. |
| **accept** | `accept(self) -> Result<TcpStream>` | Accetta una nuova connessione. |

### Tipo `TcpStream`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **connect** | `TcpStream::connect(host: char*, port: int) -> Result<TcpStream>` | Si connette a un host remoto. |
| **read** | `read(self, buf: char*, len: usize) -> Result<usize>` | Legge dallo stream. |
| **write** | `write(self, buf: u8*, len: usize) -> Result<usize>` | Scrive sullo stream. |

## UDP (`std/net/udp.zc`)

### Tipo `UdpSocket`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **bind** | `UdpSocket::bind(host: char*, port: int) -> Result<UdpSocket>` | Si associa a un indirizzo locale. |
| **recv_from** | `recv_from(self, buf: char*, len: usize) -> Result<UdpRecvResult>` | Riceve dati e informazioni sul mittente. |
| **send_to** | `send_to(self, buf: char*, len: usize, host: char*, port: int) -> Result<usize>` | Invia dati a una destinazione specifica. |

## DNS (`std/net/dns.zc`)

### Tipo `Dns`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **resolve** | `Dns::resolve(host: char*) -> Result<String>` | Risolve un nome host in un indirizzo IP. |
