import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy.signal import savgol_filter
from PIL import Image
import time
y = np.array([1,2,3,4,5])
x = np.array([np.full((3,),j) for j in y])
print(x.flatten())