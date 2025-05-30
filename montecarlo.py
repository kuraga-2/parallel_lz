import random

def monte_carlo(n):
    inside = 0
    for i in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside += 1
    return inside