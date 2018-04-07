import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy.signal import savgol_filter
from PIL import Image

t = "[208.566001983316, 214.62222287854306, 209.85227343055266, 215.06804815883893, 189.42162535338827, 221.0993700629549, 204.01958549098421, 217.5478881233004]"
l = np.array(eval(t))
r = savgol_filter(l,7,2)
print(r-l)
