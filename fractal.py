import numpy as np
import colorsys
import sympy as sp
from PIL import Image

# setting up the image
WIDTH = 1024
HEIGHT = 768

# setting up the polynomial
z = sp.symbols("z")
poly = z**3 - 1
print("This is the polynomial we are using" + poly)

# calculate the roots of the polynomial
roots_dict = sp.roots(poly, z)


# function applying newton-raphson formula (ENDED HERE)


def newton(x, y):
    zn = complex(x, y)  # starting number/current guess
    zn1 = zn - (poly/sp.Derivative(poly))
    return None


# function returning a tuple of rgb colors


def to_rgb(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))


# function that takes each pixel in the image and uses the NR formula to
# calculate fractal

img = Image.new("RGB", (WIDTH, HEIGHT))
pixels = img.load

# each pixel = point in the fractal, putting newton's formula on each pixel
for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixels[x, y] = newton(x, y)
