import os
import vtk
import pycaster
import timeit

def foo():
    caster = pycaster.rayCaster.fromSTL("GEO/apache.stl", scale=1)
    pSource = [-50.0, 0.0, 0.0]
    pTarget = [50.0, 0.0, 0.0]
    pointsIntersection = caster.castRay(pSource, pTarget)

t = timeit.timeit(foo,number=1000)
print(t)
