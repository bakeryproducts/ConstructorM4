def writepoints(points):
    f = open('RESULTS/poi.txt', 'w')
    for i, point in enumerate(points):
        f.write('P' + str(i + 1) + '=' + str(point) + '\n')
    f.close()


def writeplanes(faces, steq):
    f = open('RESULTS/gra.txt', 'w')
    for i, face in enumerate(faces):
        f.write('G' + str(i + 1) + ' = (' + str(face)[1:-1] + ') [' + str(steq) + ']\n')
    f.close()


def createtrg(points, faces, steq,filename,path):

    str1 = ':Цель агрегатная '+filename+'\n:броня Korpus\n:точки\n'
    str2 = ':грани 0\n'
    str3 = ':end'

    #f = open('C:/Users/User/Desktop/OOEF2017/InGEOBDS/'+filename+'.trg', 'w')
    # try:
    #     f = open(path + filename + '.trg', 'w')
    # except FileNotFoundError:
    #     print("File path error: .trg created in RESULTS")
    #     f = open('RESULTS/' + filename + '.trg', 'w')

    f = open(path + filename + '.trg', 'w')

    try:
        f.write(str1)
    except UnicodeEncodeError:
        f.write(str1.encode('cp1251').decode('latin1'))

    for i, point in enumerate(points):
        f.write('P' + str(i + 1) + '=' + str(point) + '\n')

    try:
        f.write(str2)
    except UnicodeEncodeError:
        f.write(str2.encode('cp1251').decode('latin1'))

    for i, face in enumerate(faces):
        f.write('G' + str(i + 1) + ' = (' + str(face)[1:-1] + ')[' + str(steq) + ']\n')
        # [' + str(steq) + ']
    try:
        f.write(str3)
    except UnicodeEncodeError:
        f.write(str3.encode('cp1251').decode('latin1'))

    f.close()
