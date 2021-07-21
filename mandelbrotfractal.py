"""
Mandelbrot fractal computations
"""

from math import log, log2

class MdFractal:
    """Represents the handling of the construction of a Mandelbrot fractal"""

    def __init__(self):
        pass

    MAX_ITERATIONS: int = 100

    def mandelbrot(self, c) -> float:
        """Determines the iterations needed to reach mod > 2"""
        z: int = 0
        n: int = 0
        while abs(z) <= 2 and n < self.MAX_ITERATIONS:
            z = z * z + c
            n += 1
        if n == self.MAX_ITERATIONS:
            return self.MAX_ITERATIONS
        return n + 1 - log(log2(abs(z)))

if __name__ == "__main__":
    for a in range(-10, 10, 5):
        for b in range(-10, 10, 5):
            c = complex(a / 10, b / 10)
            print(c, MdFractal().mandelbrot(c))

