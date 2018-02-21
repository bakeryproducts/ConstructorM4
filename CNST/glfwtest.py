s = 'C:/Users/User/Documents/GitHub/ConstructorM4/CNST/GEO/cube100stl'
import re
n = re.split('\*|/',s)
n = re.sub('\.','',n[-1])
print(n)