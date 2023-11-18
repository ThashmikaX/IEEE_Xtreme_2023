import math
import numpy as np

def find_smallest_n(a):
    n = 1
    min_cos_arr = []
    while True:
        if a == 90 or a == 270:
            min_cos_arr.append(0)
        else:
            min_cos_arr.append(abs(np.cos(a * n * np.pi / 180. )))
            n+=1
        if (n * a) >= (a + 360):
            break

    min_index = min(range(len(min_cos_arr)), key=lambda i: min_cos_arr[i])

    return (min_index+1)+

angle = 27.# Replace with your desired angle
smallest_n = find_smallest_n(angle)
print(smallest_n)
