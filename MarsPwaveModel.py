radiusVp = open("Documents\marspwave.txt").read() 

radiusVp = radiusVp.replace("\n",",")
radiusVp = radiusVp.replace("\t",",")
radiusVp = radiusVp.split(",")

radius_1 = np.array([])
vp = np.array([])

i = 0
while i < len(radiusVp) / 2: 
    radius_1 = np.append(radius_1,float(radiusVp[2 * i]))
    vp = np.append(vp,float(radiusVp[2 * i + 1]))
    i+=1
    
j = 0
while j < len(radius_1) - 1: 
    xvalues = [radius_1[j],radius_1[j+1]]
    yvalues = [vp[j],vp[j+1]]
    plt.plot(xvalues, yvalues)
    j+=1
    
plt.title("Martian P wave velocities")
plt.xlabel("Radius/km")
plt.ylabel("Velocity/km $s^-1$")
    
plt.show()
