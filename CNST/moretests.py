import numpy as np
a = np.array([[0,0,0],[1,1,1],[2,2,2],[3,3,3]])
a = a.flatten()
print(a.shape)
a = a.reshape((-1,3))
print(list(a))