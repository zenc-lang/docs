+++
title = "Echo server"
+++

# Echo server

```zc
import "std/net/tcp.zc"
import "std/thread.zc"
import "std/string.zc"

fn handle_client(stream_ptr: TcpStream*) {
    // Ensure cleanup happens automatically upon exiting scope
    defer stream_ptr.close();
    defer free(stream_ptr);
    
    println "[Thread] Client connected!";
    
    let buffer = String::from("");
    defer buffer.free();
    let read_buf: char[1024];
    
    while true {
        let res = stream_ptr.read(read_buf, 1023);
        if res.is_err() {
            eprintln "[Thread] Error reading from stream: {res.err}";
            break;
        }
        
        let n: usize = res.unwrap();
        if n == 0 {
            println "[Thread] Client disconnected normally.";
            break;
        }
        
        read_buf[n] = 0;
        buffer.append_c(read_buf);
        
        // Check for complete lines terminated by CRLF
        let idx = buffer.find_str("\r\n");
        while idx.is_some() {
            let limit = idx.unwrap() + 2;
            let line = buffer.substring(0, limit);
            
            // Echo the line back to the client
            let write_res = stream_ptr.write((u8*)line.c_str(), line.length());
            if write_res.is_err() {
                eprintln "[Thread] Failed to write back.";
                break;
            }
            
            // Update the buffer to hold only the remaining unparsed data
            let remaining = buffer.substring(limit, buffer.length() - limit);
            buffer.free();
            buffer = remaining;
            
            idx = buffer.find_str("\r\n");
        }
    }
    
    println "[Thread] Connection closed.";
}

fn main() {
    println "Starting Concurrent Echo Server on 127.0.0.1:12321...";
    
    let listener_res = TcpListener::bind("127.0.0.1", 12321);
    if listener_res.is_err() {
        eprintln "Failed to bind: {listener_res.err}";
        return 0;
    }
    
    let listener = listener_res.unwrap();
    println "Listening for incoming connections...";
    
    loop {
        let client_res = listener.accept();
        if client_res.is_err() {
            eprintln "Accept failed: {client_res.err}";
            continue;
        }
        
        // Allocate the stream on the heap so the thread can safely take ownership
        let stream_ptr = (TcpStream*)malloc(sizeof(TcpStream));
        *stream_ptr = client_res.unwrap();
        
        // Spawn a new thread to handle the client concurrently
        let thread_res = Thread::spawn(fn() {
            handle_client(stream_ptr);
        });
        
        if thread_res.is_err() {
            eprintln "Failed to spawn thread: {thread_res.err}";
            stream_ptr.close(); // Zen C auto-dereferences the pointer
            free(stream_ptr);
        } else {
            let t = thread_res.unwrap();
            t.detach(); // Detach so the thread cleans itself up upon completion
        }
    }
}
```

**Output:**

```
Starting Concurrent Echo Server on 127.0.0.1:12321...
Listening for incoming connections...
[Thread] Client connected!
[Thread] Client disconnected normally.
[Thread] Connection closed.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Echo server**](https://rosettacode.org/wiki/Echo_server) in Zen C.

*This article uses material from the Rosetta Code article **Echo server**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Echo_server?action=history).*
