import numpy as np 
import matplotlib.pyplot as plt

radiusRho = open("Documents\marsdensity.txt").read()

radiusRho = radiusRho.replace("\n",",")
radiusRho = radiusRho.replace("\t",",")
radiusRho = radiusRho.split(",")

dataSet_0 = np.array([])

for i in radiusRho: 
    dataSet_0 = np.append(dataSet_0,float(i))

radius_0 = np.array([])
rho = np.array([])
i = 0
while i < len(dataSet_0) / 2: 
    radius_0 = np.append(radius_0,dataSet_0[2 * i])
    rho = np.append(rho,dataSet_0[2 * i + 1])
    i+=1
    
j = 0
while j < len(radius_0) - 1: 
    xvalues = [radius_0[j],radius_0[j+1]]
    yvalues = [rho[j],rho[j+1]]
    plt.plot(xvalues,yvalues)
    j+=1
    
plt.title("Density distribution of Mars")
plt.xlabel("Radius/km")
plt.ylabel("Density/g $cm^-3$")
    
plt.show()
