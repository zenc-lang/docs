+++
title = "Write language name in 3D ASCII"
+++

# Write language name in 3D ASCII

Uses the same source for the 3-d letters as the Wren example. 

```zc
import "std/string.zc"

def Z = """
  ____________           
  |\\           \\         
  | \\_______    \\        
  \\ |      /    /|       
   \\|_____/    / |       
         /    /_/______  
        |\\             \\ 
        | \\_____________\\
        \\ |             |
         \\|_____________|
""";

def E = """

    ___________      
   /   _____   \\     
  /   /_____\\   \\    
 |\\       _____/|    
 | \\     /|____|/    
 \\  \\    \\/_______/\\ 
  \\  \\_____________/|
   \\ |            | |
    \\|____________|/ 
""";

def N = """
 
 _____  _______       
 |\\__  \\/       \\      
 || |\\      __   \\    
 \\|_| \\    /| \\   \\   
    \\  \\   \\/\\ \\   \\  
     \\  \\   \\ \\ \\   \\ 
      \\  \\___\\ \\ \\___\\
       \\ |   |  \\|   |
        \\|___|   |___|
""";

def C = """

       ___________       
      /           \\     
     /      _______\\    
    |\\     /|______|    
    | \\    \\/           
    \\  \\    \\________/\\ 
     \\  \\_____________/|
      \\ |            | |
       \\|____________|/ 
""";

fn main() {
    let z  = String::from(Z);
    let zs = z.split('\n');
    let e  = String::from(E);
    let es = e.split('\n');
    let n  = String::from(N);
    let ns = n.split('\n');
    let c  = String::from(C);
    let cs = c.split('\n');
    for i in 0..12 {
        println "{zs[i]}{es[i]}{ns[i]} {cs[i]}";
    }
}
```

**Output:**

```
____________             
  |\           \             ___________       _____  _______               ___________       
  | \_______    \           /   _____   \      |\__  \/       \             /           \     
  \ |      /    /|         /   /_____\   \     || |\      __   \          /      _______\    
   \|_____/    / |        |\       _____/|     \|_| \    /| \   \        |\     /|______|    
         /    /_/______   | \     /|____|/        \  \   \/\ \   \       | \    \/           
        |\             \  \  \    \/_______/\      \  \   \ \ \   \      \  \    \________/\ 
        | \_____________\  \  \_____________/|      \  \___\ \ \___\      \  \_____________/|
        \ |             |   \ |            | |       \ |   |  \|   |       \ |            | |
         \|_____________|    \|____________|/         \|___|   |___|        \|____________|/
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Write language name in 3D ASCII**](https://rosettacode.org/wiki/Write_language_name_in_3D_ASCII) in Zen C.

*This article uses material from the Rosetta Code article **Write language name in 3D ASCII**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Write_language_name_in_3D_ASCII?action=history).*
