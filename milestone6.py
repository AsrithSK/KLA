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


    return (header,polygons)

headerpoi,polygonspoi = parseFile('POI.txt')
headersrc,polygonssrc = parseFile('Source.txt')



def extractCoordinates(polygon):
    polygonl = polygon.split()
    polygonl = polygonl[2:]
    polygonl = [eval(i) for i in polygonl]
    
    return polygonl


def checkifequalsides(p1,p2):
    if(len(p1) != len(p2)):
        return False
    p1sides = []
    p2sides = []
    for i in range(0,len(p1)-2,2):
        p1sides.append(math.dist([p1[i],p1[i+1]],[p1[i+2],p1[i+3]]))
    for i in range(0,len(p2)-2,2):
        p2sides.append(math.dist([p2[i],p2[i+1]],[p2[i+2],p2[i+3]]))
    p1angles = []
    p2angles = []
    for i in range(0,len(p1)-2,2):
        p1angles.append(math.atan2(p1[i+1]-p1[i+3],p1[i]-p1[i+2]))
    for i in range(0,len(p2)-2,2):
        p2angles.append(math.atan2(p2[i+1]-p2[i+3],p2[i]-p2[i+2]))  

    r = p1sides[0]/p2sides[0]
    for i in range(0,len(p1sides)):
        if p1sides[i]/p2sides[i] != r:
            return False
    return True
    



matched_polygons = []

for p1 in polygonspoi:
    for p2 in polygonssrc:
        b1 = extractCoordinates(p1[3])
        b2 = extractCoordinates(p2[3])
        if checkifequalsides(b1,b2):
            matched_polygons.append(p2)


f = open("output.txt", "w")
for h in headerpoi:
    f.write(h)
    f.write("\n")

for polygon in matched_polygons:
    for p in polygon:
        f.write(p)
        f.write("\n") 

f.close()

