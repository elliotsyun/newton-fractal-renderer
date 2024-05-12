from PIL import Image
import numpy as np
import colorsys

width = 1024

# using polynomial z^3 - 1
poly = np.poly1d([1, 0, 0, -1])

print(poly)
