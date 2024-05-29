## Newton's Fractal for \( z^3 - 1 = 0 \)

### Introduction

This project generates a Newton fractal for the polynomial \( z^3 - 1 \). A Newton fractal is a visualization of the behavior of Newton's method applied to a complex polynomial. The fractal divides the complex plane into regions corresponding to the roots of the polynomial.

### Prerequisites

To run this project, you need the following Python packages:

- `numpy`
- `Pillow`

You can install these packages using `pip`:

```sh
pip install numpy pillow
```

### Project Structure

- `newton_fractal.py`: The main script that generates the Newton fractal.

### Code Explanation

#### Imports

```python
import numpy as np
import colorsys
from PIL import Image
```

We import the necessary libraries: `numpy` for numerical operations, `colorsys` for color space conversions, and `PIL` (Pillow) for image creation and manipulation.

#### Constants

```python
WIDTH = 1024
HEIGHT = 768
```

These constants define the dimensions of the generated image.

#### Polynomial Setup

```python
coeff = [1, 0, 0, -1]
poly = np.poly1d(coeff)

roots = np.roots(coeff)
tolerance = 1e-6
```

We define the polynomial \( z^3 - 1 \) using its coefficients and compute its roots. The `tolerance` variable is used to determine the convergence criteria for Newton's method.

#### Image Setup

```python
img = Image.new("RGB", (WIDTH, HEIGHT))
pixels = img.load()
```

We create a new RGB image with the specified dimensions and prepare to manipulate its pixels.

#### Newton's Method

```python
def newton(x, y):
    z = complex(x, y)
    for iter in range(100):
        polyz = poly(z)
        polyderiv = poly.deriv()(z)

        if polyderiv == 0:
            break

        z -= polyz / polyderiv

        for root in roots:
            if abs(root - z) < tolerance:
                return point_to_rgb(iter)

    return (0, 0, 0)
```

The `newton` function applies Newton's method to a complex number \( z \) derived from the pixel coordinates. It iteratively refines \( z \) to find a root of the polynomial. The function returns a color based on the number of iterations required to converge to a root.

#### Color Mapping

```python
def point_to_rgb(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))
```

The `point_to_rgb` function converts an iteration count to an RGB color using the HSV color space.

#### Image Generation

```python
real_range = (-2, 2)
imag_range = (-1.5, 1.5)

for x in range(WIDTH):
    print("%.2f %%" % (x / WIDTH * 100.0))
    for y in range(HEIGHT):
        pixels[x, y] = newton((x - (0.75 * WIDTH)) / (WIDTH / 4), (y - (WIDTH / 4)) / (WIDTH / 4))
```

We iterate over each pixel in the image, map it to a point in the complex plane, and apply Newton's method to determine the color of the pixel.

#### Displaying the Image

```python
img.show()
```

The generated image is displayed.

### Usage

To run the script and generate the Newton fractal, simply execute:

```sh
python newton_fractal.py
```

The script will generate an image representing the Newton fractal for the polynomial \( z^3 - 1 \) and display it.

### Acknowledgements

This project uses the Newton-Raphson method for finding roots of the polynomial and visualizes the fractal nature of the solutions in the complex plane. The coloring is based on the number of iterations required for convergence.
