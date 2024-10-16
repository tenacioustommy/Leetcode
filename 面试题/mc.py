import random
import numpy as np
def simulate(input):
    n = 1000000
    count_A = 0
    count_B = 0
    for i in range(n):
        x=input
        while x <= 0.5 or x >= -0.5:
            x += random.uniform(0, 1)
            if x > 0.5:
                count_A += 1
                break
            x -= random.uniform(0, 1)
            if x < -0.5:
                count_B += 1
                break
        
    return count_A / n, count_B / n
print(simulate(-0.285))