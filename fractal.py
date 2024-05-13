import numpy as np
import colorsys
import sympy as sp
from PIL import Image


# width of the image will be 1024
WIDTH = 1024

# using polynomial x^3 - 1
x = sp.symbols("x")
f = x**3 - 1
print("The polynomial formula we are using is: " + f)

# converting integer to an rgb value as a tuple of colors


def convert_rgb(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))


# newton raphson formula


def newton():
    for _ in range(10):
        guess = guess - (f / sp.Derivative(f, x))
