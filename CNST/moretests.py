import numpy as np

a = np.array([5,4,9,6,1,5,7])
b = np.array([2,6,5,7,8,5,6])

print(a>5)
print(b<7)
l = (a>5)*(b<7)
print(np.sum(l))