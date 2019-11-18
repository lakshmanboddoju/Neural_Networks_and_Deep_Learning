#! python3

import numpy as np, time

a = np.array([1,2,3,4])
print(a)

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print(c)
print("Vectorized version: " + str(1000*(toc-tic))+"ms")

d = 0
tic = time.time()
for i in range(1000000):
    d += a[i]*b[i]
toc = time.time()

print(d)
print("For loop version: " + str(1000*(toc-tic))+"ms")
