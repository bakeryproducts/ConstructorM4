import numpy as np

def seekp(l, commonelems):
    cl = 2#len(commonelems)
    while l[:cl] != commonelems and l[:cl] != commonelems[::-1] :
        l = list(rotate(l, 1))
    return l

def rotate(l, n):
    return np.append(l[-n:], l[:-n], axis=0)


a,b = [125, 139, 120] ,[174, 139, 125, 124, 123, 122, 121, 120, 131, 132, 129, 173]
#a,b = [113, 95, 84],[95, 113, 177, 178, 179]
common = list(set(b).intersection(a))
print(common)
# print(seekp(a,common))
# print(seekp(b,common))
