"""
Draws the Mandelbrot fractal as an image
"""

from PIL import Image, ImageDraw
from mandelbrotfractal import MdFractal

WIDTH: int = 600
HEIGHT: int = 400

RE_START: int = -2
RE_END: int = 1
IM_START: int = -1
IM_END: int = 1

# Iterate over the width pixels to conver coordinate of pixel into a complex number of the complex plane
#def composeImage():
im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH): 
    for y in range(0, HEIGHT): 

        # Convert coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START), IM_START + (y / HEIGHT) * (IM_END - IM_START))

        # Compute number of iterations
        m = MdFractal().mandelbrot(c)

        # Color depends on the number of iterations
        # Adjust color by altering the hue
        hue = int(400 * m / MdFractal().MAX_ITERATIONS) 
        saturation = 400 
        if m < MdFractal().MAX_ITERATIONS:
            value = 400 
        else:
            value = 0

        # Plot
        draw.point([x, y], (hue, saturation, value))

im.convert('RGB').save('fractal.png', 'PNG')