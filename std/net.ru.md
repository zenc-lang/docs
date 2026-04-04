# std/net

Модуль `std/net` предоставляет полный сетевой стек, включая TCP, UDP, DNS и HTTP.

## Использование

```zc
import "std/net/tcp.zc"  // TcpStream, TcpListener
import "std/net/udp.zc"  // UdpSocket
import "std/net/http.zc" // HTTP клиент/сервер
import "std/net/dns.zc"  // Разрешение DNS имен
import "std/net/url.zc"  // Парсинг URL
import "std/net/websocket.zc" // WebSocket
```

## WebSocket (`std/net/websocket.zc`)

### Тип `WebSocket`

Обеспечивает рукопожатие (handshake) и фрейминг WebSocket на стороне сервера.

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **handshake** | `WebSocket::handshake(stream: TcpStream, key: String) -> Result<WebSocket>` | Выполняет рукопожатие на стороне сервера. |
| **recv** | `recv(self) -> Result<String>` | Получает текстовый фрейм (с выполнением демаскирования). |
| **send** | `send(self, msg: String) -> Result<int>` | Отправляет текстовый фрейм. |

## HTTP клиент и сервер (`std/net/http.zc`)

### Тип `Server`

Простой HTTP-сервер с поддержкой многопоточности.

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **new** | `Server::new(port: int, handler: fn(Request*, Response*)) -> Server` | Создает новый HTTP-сервер. |
| **start** | `start(self)` | Запускает цикл прослушивания сервера. |

### Клиент `fetch`

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **fetch** | `fetch(url: String) -> Response` | Выполняет GET-запрос. |

## Парсинг URL (`std/net/url.zc`)

### Тип `Url`

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **parse** | `Url::parse(s: String) -> Option<Url>` | Разбирает строку URL. |

## TCP (`std/net/tcp.zc`)

### Тип `TcpListener`

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **bind** | `TcpListener::bind(host: char*, port: int) -> Result<TcpListener>` | Привязывается к локальному адресу. |
| **accept** | `accept(self) -> Result<TcpStream>` | Принимает новое соединение. |

### Тип `TcpStream`

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **connect** | `TcpStream::connect(host: char*, port: int) -> Result<TcpStream>` | Подключается к удаленному хосту. |
| **read** | `read(self, buf: char*, len: usize) -> Result<usize>` | Читает из потока. |
| **write** | `write(self, buf: u8*, len: usize) -> Result<usize>` | Записывает в поток. |

## UDP (`std/net/udp.zc`)

### Тип `UdpSocket`

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **bind** | `UdpSocket::bind(host: char*, port: int) -> Result<UdpSocket>` | Привязывается к локальному адресу. |
| **recv_from** | `recv_from(self, buf: char*, len: usize) -> Result<UdpRecvResult>` | Получает данные и информацию об отправителе. |
| **send_to** | `send_to(self, buf: char*, len: usize, host: char*, port: int) -> Result<usize>` | Отправляет данные по указанному адресу. |

## DNS (`std/net/dns.zc`)

### Тип `Dns`

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **resolve** | `Dns::resolve(host: char*) -> Result<String>` | Разрешает доменное имя в IP-адрес. |
走
走
走
走
走
走
走
走
走
走
