from math import log, log2

# Return iterations needed to reach mod > 2
MAX_ITERATIONS = 80
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITERATIONS:
        z = z * z + c
        n += 1
    if n == MAX_ITERATIONS:
        return MAX_ITERATIONS

    return n + 1 - log(log2(abs(z)))

if __name__ == "__main__":
    for a in range(-10, 10, 5):
        for b in range(-10, 10, 5):
            c = complex(a / 10, b / 10)
            print(c, mandelbrot(c))


