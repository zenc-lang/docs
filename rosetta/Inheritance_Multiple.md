+++
title = "Inheritance/Multiple"
+++

# Inheritance/Multiple

Zen C does not have classes but does have structs which can implement methods.

The language doesn't have inheritance as such but instead uses composition to embed other structs. Any number of structs can be embedded in this way.

In the following code, the CameraPhone struct embeds both the Camera and Phone structs in a way which enables it to call their methods.

```zc
struct Camera {}

impl Camera {
    fn snap(self) { println "Taking a photo."; }
}

struct Phone {}

impl Phone {
    fn call(self) { println "Calling home."; }
}

struct CameraPhone {
    use camera : Camera;
    use phone  : Phone;
}

fn main() {
    let cp = CameraPhone{camera: Camera{}, phone: Phone{}};
    cp.camera.snap();
    cp.phone.call();
}
```

**Output:**

```
Taking a photo.
Calling home.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Inheritance/Multiple**](https://rosettacode.org/wiki/Inheritance/Multiple) in Zen C.

*This article uses material from the Rosetta Code article **Inheritance/Multiple**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Inheritance/Multiple?action=history).*
