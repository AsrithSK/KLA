with open('Format_Source.txt') as f:
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

f = open("output.txt", "w")
for h in header:
    f.write(h)
    f.write("\n")

for polygon in polygons[:2]:
    for p in polygon:
        f.write(p)
        f.write("\n") 

f.close()


        

