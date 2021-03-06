import os
import vtk
import pycaster
import timeit

caster = pycaster.rayCaster.fromSTL("GEO/cube100.stl", scale=1)

def foo():
    pSource = [-500.0, -500.0, -500.0]
    pTarget = [500.0, 500.0, 500.0]
    pointsIntersection = caster.castRay(pSource, pTarget)
    return pointsIntersection

t = timeit.timeit(foo,number=30000)
print(t)

#print(foo())