from sys import exit
from stl import mesh


def stlredo(filename, scale):
    try:
        mymesh = mesh.Mesh.from_file("GEO/" + filename)
    except FileNotFoundError as e:
        print("No such file in \GEOMETRY\ : "+filename)
        exit(0)
    except:
        print("Error opening .stl geometry")
        exit(0)

    points = []
    a = mymesh.v0
    b = mymesh.v1
    c = mymesh.v2
    abc = []

    for t in [a, b, c]:
        allmeshp = []
        for point in t:
            ipoint = []
            for cd in point:
                t = round(scale * float(cd), 2)
                ipoint.append(t)
            allmeshp.append(ipoint)
        abc.append(allmeshp)

    numpoints=[]
    for t in abc:
        for point in t:
            if repr(list(point)) not in points:
                points.append(repr(list(point)))
                numpoints.append(list(point))

    values = range(1, 1 + len(points))
    keys = [point for point in points]
    rules = dict(zip(keys, values))

    faces = []

    for i in range(len(a)):
        p1 = rules[repr(list(abc[0][i]))]
        p2 = rules[repr(list(abc[1][i]))]
        p3 = rules[repr(list(abc[2][i]))]
        faces.append([p1, p2, p3])

    return (numpoints, faces)
