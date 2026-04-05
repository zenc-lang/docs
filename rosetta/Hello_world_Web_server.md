+++
title = "Hello world/Web server"
+++

# Hello world/Web server

```zc
import "std/net/http.zc"

// The handler receives a pointer to the Request and Response objects
fn handler(_req: Request*, res: Response*) {
    res.set_body_str("Goodbye, World!");
}

fn main() {
    // Create a new HTTP server on port 8080 routing to the handler
    let server = Server::new(8080, handler);
    println "Serving 'Goodbye, World!' at http://localhost:8080/";
    
    // Start listening for incoming connections
    server.start();
}
```

**Output:**

**Server Console:**

```
Serving 'Goodbye, World!' at http://localhost:8080/
Server listening on port 8080
```

**Client / Browser Request:**

```
$ curl http://localhost:8080/
Goodbye, World!
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Hello world/Web server**](https://rosettacode.org/wiki/Hello_world/Web_server) in Zen C.

*This article uses material from the Rosetta Code article **Hello world/Web server**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Hello_world/Web_server?action=history).*
