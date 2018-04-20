import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy.signal import savgol_filter
from PIL import Image
import time

a = [[1,0,2],[3,4,2]]
b = np.array(a)

print(b[:,0])