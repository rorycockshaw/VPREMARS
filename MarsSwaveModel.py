radiusVs = open("Documents\marsswave.txt").read() 

radiusVs = radiusVs.replace("\n",",")
radiusVs = radiusVs.replace("\t",",")
radiusVs = radiusVs.split(",")

radius_2 = np.array([])
vs = np.array([])

i = 0
while i < len(radiusVs) / 2: 
    radius_2 = np.append(radius_2,float(radiusVs[2 * i]))
    vs = np.append(vs,float(radiusVs[2 * i + 1]))
    i+=1
    
j = 0
while j < len(radius_2) - 1: 
    xvalues = [radius_2[j],radius_2[j+1]]
    yvalues = [vs[j],vs[j+1]]
    plt.plot(xvalues, yvalues)
    j+=1
    
plt.title("Martian S wave velocities")
plt.xlabel("Radius/km")
plt.ylabel("Velocity/km $s^-1$")
    
plt.show()
