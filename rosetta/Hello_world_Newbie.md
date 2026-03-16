+++
title = "Hello world/Newbie"
+++

# Hello world/Newbie

Zen C is a modern systems programming language that compiles to human-readable GNU C/C.<br>
Docs and the like can be found on it's [https://github.com/zenc-lang/zenc github] page. <br>

### Supported Platforms and Backends

The Zen C compiler, <code>zc</code>, has support for Windows, macOS and Linux. As it is a transpiler (a source-to-source compiler), it acts as a front-end, requiring a back-end. Some of the available backends are <code>gcc</code>, <code>clang</code>, <code>tcc</code>, <code>zig cc</code>. The list is not exhaustive. By default, <code>gcc</code> will be used, but you can specify the back-end with the <code>--cc</code> flag.

### Installation

#### Compile from source

```zc
git clone https://github.com/zenc-lang/zenc.git
cd Zen-C
make clean # remove old build files
make
sudo make install
```

If you are on Windows you can build using the provided batch script, <code>build.bat</code>.

### Example

```zc
fn main() {
    // In Zen C, I/O is not handled like in C. While 'printf' or 'puts'
    // among others are still available, Zen C also has special keywords,
    // like 'println' or 'print' (stdout) and 'eprintln' or 'eprint' (stderr).
    // Each one of these keywords also has an implicit form.
    // -> "..." is the same as println "..."
    // -> "...".. is the same as print "..."
    // -> !"..." is the same as eprintln "..."
    // -> !"...".. is the same as eprint "..."
    "Hello, World!"
}
```

And to compile use <code>zc</code>.

```
zc hello.zc && ./hello # or use ./zc if you haven't installed it.
```

You can also run it directly like this:

```
zc run hello.zc
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Hello world/Newbie**](https://rosettacode.org/wiki/Hello_world/Newbie) in Zen C.

*This article uses material from the Rosetta Code article **Hello world/Newbie**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Hello_world/Newbie?action=history).*
