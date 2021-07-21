from PIL import Image, ImageDraw
from mandelbrotfractal import mandelbrot, MAX_ITERATIONS
import dis

# Image size in pixels
WIDTH = 600
HEIGHT = 400

# Window size in pixels
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

# Iterate over the width pixels to conver coordinate of pixel into a complex number of the complex plane
for x in range(0, WIDTH): 
    for y in range(0, HEIGHT): 
        # Convert coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START), IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Compute number of iterations
        m = mandelbrot(c)
        # Color depends on the number of iterations
        # Adjust color by altering the hue
        hue = int(400 * m / MAX_ITERATIONS) # 255
        saturation = 400 # 255
        if m < MAX_ITERATIONS:
            value = 400 # 255
        else:
            value = 0
        # Plot
        draw.point([x, y], (hue, saturation, value))

im.convert('RGB').save('output.png', 'PNG')

