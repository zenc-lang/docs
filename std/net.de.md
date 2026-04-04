# std/net

Das Modul `std/net` bietet einen umfassenden Netzwerk-Stack einschließlich TCP, UDP, DNS und HTTP.

## Verwendung

```zc
import "std/net/tcp.zc"  // TcpStream, TcpListener
import "std/net/udp.zc"  // UdpSocket
import "std/net/http.zc" // HTTP Client/Server
import "std/net/dns.zc"  // DNS-Auflösung
import "std/net/url.zc"  // URL-Parsing
import "std/net/websocket.zc" // WebSocket
```

## WebSocket (`std/net/websocket.zc`)

### Typ `WebSocket`

Bietet serverseitigen WebSocket-Handshake und Framing.

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **handshake** | `WebSocket::handshake(stream: TcpStream, key: String) -> Result<WebSocket>` | Führt den serverseitigen Handshake durch. |
| **recv** | `recv(self) -> Result<String>` | Empfängt einen Text-Frame (behandelt Unmasking). |
| **send** | `send(self, msg: String) -> Result<int>` | Sendet einen Text-Frame. |

## HTTP Client & Server (`std/net/http.zc`)

### Typ `Server`

Ein einfacher, multithreading-fähiger HTTP-Server.

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Server::new(port: int, handler: fn(Request*, Response*)) -> Server` | Erstellt einen neuen HTTP-Server. |
| **start** | `start(self)` | Startet die Server-Listening-Schleife. |

### Client `fetch`

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **fetch** | `fetch(url: String) -> Response` | Führt eine GET-Anfrage aus. |

## URL-Parsing (`std/net/url.zc`)

### Typ `Url`

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **parse** | `Url::parse(s: String) -> Option<Url>` | Parst einen URL-String. |

## TCP (`std/net/tcp.zc`)

### Typ `TcpListener`

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **bind** | `TcpListener::bind(host: char*, port: int) -> Result<TcpListener>` | Bindet an eine lokale Adresse. |
| **accept** | `accept(self) -> Result<TcpStream>` | Akzeptiert eine neue Verbindung. |

### Typ `TcpStream`

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **connect** | `TcpStream::connect(host: char*, port: int) -> Result<TcpStream>` | Verbindet zu einem entfernten Host. |
| **read** | `read(self, buf: char*, len: usize) -> Result<usize>` | Liest aus dem Stream. |
| **write** | `write(self, buf: u8*, len: usize) -> Result<usize>` | Schreibt in den Stream. |

## UDP (`std/net/udp.zc`)

### Typ `UdpSocket`

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **bind** | `UdpSocket::bind(host: char*, port: int) -> Result<UdpSocket>` | Bindet an eine lokale Adresse. |
| **recv_from** | `recv_from(self, buf: char*, len: usize) -> Result<UdpRecvResult>` | Empfängt Daten und Absenderinformationen. |
| **send_to** | `send_to(self, buf: char*, len: usize, host: char*, port: int) -> Result<usize>` | Sendet Daten an ein bestimmtes Ziel. |

## DNS (`std/net/dns.zc`)

### Typ `Dns`

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **resolve** | `Dns::resolve(host: char*) -> Result<String>` | Löst einen Hostnamen in eine IP-Adresse auf. |
