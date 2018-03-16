import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from PIL import Image




heatmap = np.array(range(64)).reshape((8,8))
al = np.array(range(64))

alds = ndimage.uniform_filter(heatmap, size=5, mode='constant')

print(heatmap)
print(alds)
# img = Image.fromarray(np.uint8(ds), 'RGBA')
# img.save('RESULTS\\heatmap.png', 'PNG')
