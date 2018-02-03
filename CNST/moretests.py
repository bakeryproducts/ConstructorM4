import numpy as np

cross = [np.array([     0.,      0.,  13750.]), np.array([    0.,     0., -2500.]), np.array([    0.        ,     0.        , -2761.80328369]), np.array([    -0.       ,     -0.       , -33141.6394043]), np.array([    0.,     0., -1200.]), np.array([   0.,    0., -550.])]

for i, v in enumerate(cross[1:]):
    print(v,cross[0],' = ',end='')
    print(np.dot(v, cross[0]))
