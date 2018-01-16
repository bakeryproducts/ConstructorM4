ray = mth.Vector((-100,-60,-300))
    orig = mth.Vector((100,60,300))
    line = (list(ray),list(orig))
    inters = []
line = getline(mpos)
                    geocor=mv
                    inters = getinters(geocor,modelg,line)
                    print(line,inters)

def getinters(geocor,model,line):

    orgpoints,faces = model

    points=[]
    for point in orgpoints:
        ipoint = np.matmul(geocor,(*point,1))
        points.append(ipoint[:3])
    #points=orgpoints

    mpoints = []
    for point in points:
        mpoints.append(mth.Vector(point))

    checkinters = []
    for face in faces:
        v3, v2, v1 = [mpoints[i - 1] for i in face]
        ray = mth.Vector(line[0])
        org = mth.Vector(line[1])
        ci = mth.geometry.intersect_ray_tri(v1,v2,v3,ray,org)
        if ci!=None and ci not in checkinters:
            checkinters.append(tuple(ci))
    #inters = [tuple(inter) for inter in checkinters if inter != None]

    return checkinters


def getintersold(geocor,model,line):

    orgpoints,faces = model

    # points=[]
    # for point in orgpoints:
    #     ipoint = np.matmul(geocor,(*point,1))
    #     points.append(ipoint[:3])
    points=orgpoints

    line_a = mth.Vector(line[0])
    line_b = mth.Vector(line[1])


    checkinters = []
    for face in faces:
        v3, v2, v1 = [points[i - 1] for i in face]
        plane_co = mth.Vector(v1)
        a = np.array(v3) - np.array(v1)
        b = np.array(v2) - np.array(v1)
        plane_no = mth.Vector(np.cross(a,b))
        ci = mth.geometry.intersect_line_plane(line_a, line_b, plane_co, plane_no)
        if ci!=None and ci not in checkinters:
            checkinters.append(tuple(ci))
    #inters = [tuple(inter) for inter in checkinters if inter != None]

    return checkinters
