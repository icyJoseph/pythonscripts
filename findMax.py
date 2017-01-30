import random
import timeit
import numpy as np

def generator():
    x = random.sample(range(30000),1000)
    print(x)
    y = np.asarray(x)
    return y

def find_max():
    x = generator()
    max_x = x[0]
    for i in range (0,x.size):
        if max_x <= x[i]:
            max_x = x[i]
    print (max_x)

if __name__ == '__main__':
    print("time: "+str(timeit.timeit("find_max()",
    setup="from __main__ import find_max",
    number=1))+" secs")
