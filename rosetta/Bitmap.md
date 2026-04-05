+++
title = "Bitmap"
+++

# Bitmap

Zen C handles basic raster image storage by allocating a contiguous, 1-dimensional array of pixels on the heap. Accessing a 2-dimensional coordinate (x, y) is done using the standard row-major order formula: <code>y * width + x</code>.

Zen C supports Resource Acquisition Is Initialization (RAII) via the <code>Drop</code> trait. When the <code>Image</code> struct goes out of scope, the compiler automatically injects the <code>drop</code> method, guaranteeing that the dynamically allocated pixel buffer is safely freed without requiring manual <code>free()</code> calls in the main application logic.

```zc
import "std/mem.zc"
import "std/core.zc"

struct Color {
    r: u8;
    g: u8;
    b: u8;
}

struct Image {
    width: usize;
    height: usize;
    pixels: Color*;
}

impl Image {
    fn new(width: usize, height: usize) -> Self {
        return Self {
            width: width,
            height: height,
            pixels: alloc_n<Color>(width * height)
        };
    }

    fn fill(self, color: Color) {
        for let i: usize = 0; i < self.width * self.height; i++ {
            self.pixels[i] = color;
        }
    }

    fn set_pixel(self, x: usize, y: usize, color: Color) {
        if x < self.width && y < self.height {
            self.pixels[y * self.width + x] = color;
        }
    }

    fn get_pixel(self, x: usize, y: usize) -> Color {
        if x < self.width && y < self.height {
            return self.pixels[y * self.width + x];
        }
        return Color { r: 0, g: 0, b: 0 };
    }
}

// RAII: Automatically free memory when the struct goes out of scope
impl Drop for Image {
    fn drop(self) {
        if self.pixels != NULL {
            println "[RAII] Freeing image buffer ({self.width}x{self.height})";
            free(self.pixels);
        }
    }
}

fn main() {
    let img = Image::new(3, 3);
    println "Created {img.width}x{img.height} image.";

    // Fill image with blue
    let blue = Color { r: 0, g: 0, b: 255 };
    img.fill(blue);
    println "Image filled with blue (0, 0, 255).";

    // Set center pixel to red
    let red = Color { r: 255, g: 0, b: 0 };
    img.set_pixel(1, 1, red);
    println "Set pixel at (1, 1) to red (255, 0, 0).";

    // Get colors and verify
    let c11 = img.get_pixel(1, 1);
    let c00 = img.get_pixel(0, 0);

    println "Pixel (1, 1): R={c11.r}, G={c11.g}, B={c11.b}";
    println "Pixel (0, 0): R={c00.r}, G={c00.g}, B={c00.b}";

    assert(c11.r == 255 && c11.g == 0 && c11.b == 0, "Pixel (1,1) should be red");
    assert(c00.r == 0 && c00.g == 0 && c00.b == 255, "Pixel (0,0) should be blue");

    println "Verification successful!";
}
```

**Output:**

```
Created 3x3 image.
Image filled with blue (0, 0, 255).
Set pixel at (1, 1) to red (255, 0, 0).
Pixel (1, 1): R=255, G=0, B=0
Pixel (0, 0): R=0, G=0, B=255
Verification successful!
[RAII] Freeing image buffer (3x3)
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Bitmap**](https://rosettacode.org/wiki/Bitmap) in Zen C.

*This article uses material from the Rosetta Code article **Bitmap**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Bitmap?action=history).*
