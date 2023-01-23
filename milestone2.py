import math
def parseFile(filename):
    with open(filename) as f:
        lines = f.readlines()


    header = []
    for line in lines:
        if line.strip() == "boundary":
            break
        header.append(line.strip())


    polygons = []
    polygon = []
    flag = 0
    for line in lines:
        if line.strip() == "boundary":
            flag = 1
        if flag == 1:
            polygon.append(line.strip())
        if line.strip() == "endel":
            flag = 0
            polygons.append(polygon)
            polygon=[]

    # f = open("output.txt", "w")
    # for h in header:
    #     f.write(h)
    #     f.write("\n")

    # for polygon in polygons:
    #     for p in polygon:
    #         f.write(p)
    #         f.write("\n") 

    # f.close()
    return (header,polygons)

headerpoi,polygonspoi = parseFile('POI.txt')
headersrc,polygonssrc = parseFile('Source.txt')

# def bringToOrigin(polygon):
#     polygonl = polygon.split()
#     polygonl = polygonl[2:]
#     polygonl = [eval(i) for i in polygonl]
#     minimum_valuex = min(polygonl[0::2])
#     minimum_valuey = min(polygonl[1::2])
#     for i,p in enumerate(polygonl):
#         if i%2 == 0:
#             polygonl[i] = p - minimum_valuex
#         else:
#             polygonl[i] = p - minimum_valuey
#     return polygonl

def extractCoordinates(polygon):
    polygonl = polygon.split()
    polygonl = polygonl[2:]
    polygonl = [eval(i) for i in polygonl]
    
    return polygonl

def checkifequal(b1,b2):
    if len(b1) != len(b2):
        return False
    # for i in range(0..len(b1)):
    #     if(b1[i] != b2[i]):
    #         return False
    x = [b1[i:i + 2] for i in range(0, len(b1), 2)]
    y = [b2[i:i + 2] for i in range(0, len(b2), 2)]
    for i in x:
        if i not in y:
            return False
    return True

def checkifequalsides(p1,p2):
    if len(p1) != len(p2):
        return False
    p1sides = []
    p2sides = []
    for i in range(0,len(p1)-2,2):
        p1sides.append(math.dist([p1[i],p1[i+1]],[p1[i+2],p1[i+3]]))
        p2sides.append(math.dist([p2[i],p2[i+1]],[p2[i+2],p2[i+3]]))
    print(p1sides)
    print(p2sides)
    for i in p1sides:
        if i not in p2sides:
            return False
    return True

matched_polygons = []

for p1 in polygonspoi:
    for p2 in polygonssrc:
        b1 = extractCoordinates(p1[3])
        b2 = extractCoordinates(p2[3])
#         # if checkifequal(b1,b2):
#         #     matched_polygons.append(p2)
        if checkifequalsides(b1,b2):
            matched_polygons.append(p2)
# b1 = extractCoordinates(polygonspoi[0][3])
# b2 = extractCoordinates(polygonssrc[0][3])
# if checkifequalsides(b1,b2):
#     print(b1)
#     print(b2)

f = open("output.txt", "w")
for h in headerpoi:
    f.write(h)
    f.write("\n")

for polygon in matched_polygons:
    for p in polygon:
        f.write(p)
        f.write("\n") 

f.close()

