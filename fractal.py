import numpy as np
import colorsys
from PIL import Image

# setting up the image
WIDTH = 1024
HEIGHT = 768

# setting up the polynomial
coeff = [1, 0, 0, -1]
poly = np.poly1d(coeff)
print("This is the polynomial we are using", poly)

# calculate the roots of the polynomial
roots = np.roots(coeff)
print("These are the roots of the polynomial: ", roots)

# set up the image
img = Image.new("RGB", (WIDTH, HEIGHT))
pixels = img.load


# newton-raphson method
def newton(x, y):
    zn = complex(x, y)

    zn = complex(x, y)  # make pixel into complex number with x and y val
    zn = zn - (poly / sp.Derivative(poly))

    for key in roots_dict:
        if roots_dict[key] - zn < 0.1:
            key + 1
            return to_rgb(zn)
    return (0, 0, 0)  # default color


def to_rgb(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))


for x in range(img.size[0]):  # iterate for every pixel on the image
    for y in range(img.size[1]):
        pixels[x, y] = newton(x, y)


img.show()
