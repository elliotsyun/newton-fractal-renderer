import numpy as np
import colorsys
from PIL import Image

# setting up the image
WIDTH = 1024
HEIGHT = 768

# setting up the polynomial z^3 - 1
coeff = [1, 0, 0, -1]
poly = np.poly1d(coeff)

# calculate the roots of the polynomial
roots = np.roots(coeff)
tolerance = 1e-6

# set up the image
img = Image.new("RGB", (WIDTH, HEIGHT))
pixels = img.load()


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


def point_to_rgb(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))


print("This is the polynomial we are using", poly)
print("These are the roots of the polynomial: ", roots)

real_range = (-2, 2)
imag_range = (-1.5, 1.5)

for x in range(WIDTH):
    print("%.2f %%" % (x / WIDTH * 100.0))
    for y in range(HEIGHT):

        pixels[x, y] = newton(
            (x - (0.75 * WIDTH)) / (WIDTH / 4), (y - (WIDTH / 4)) / (WIDTH / 4)
        )

img.show()
