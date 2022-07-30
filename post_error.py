# -*-coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def frange(x,y,jump):
  while x <= y:
    x = round(x,2)
    yield x
    x += jump

steps = 800

start_nterm = 5
end_nterm = 11
d_nterm = 1
nterms = list(frange(start_nterm,end_nterm,d_nterm))

start_nump = 100
end_nump = 400
d_nump = 50
numps = list(frange(start_nump,end_nump,d_nump))

start_theta = 0.1
end_theta = 1.0
d_theta = 0.1
thetas = list(frange(start_theta,end_theta,d_theta))

print(numps,thetas)
#--------------------------------------------------------
#- Default
#--------------------------------------------------------
file_name = "./force/force_total_all.dat"
with open(file_name,'r') as infile:
  for i in range(steps): next(infile)
  s_line = infile.readline()
  data = s_line.split(" ")
  data = [x for x in data if x]

  cy0 = float(data[2])
#--------------------------------------------------------


cy = np.zeros([len(numps),len(thetas)])
for i,theta in enumerate(thetas):
  #for j,nump in enumerate(numps):
  for j,nterm in enumerate(nterms):
    #file_name = "./force/force_total_all_" + str(nump) + "_" + str(theta) + ".dat"
    file_name = "./force/force_total_all_" + str(nterm) + "_" + str(theta) + ".dat"
    with open(file_name,'r') as infile:
      for k in range(steps): next(infile)
      s_line = infile.readline()
      data = s_line.split(" ")
      data = [x for x in data if x]

      if(theta == 0.8):
       
       
       print((abs(float(data[2])-cy0)*100))


      cy[j][i] = (abs(float(data[2])-cy0)*100)


fig = plt.figure(figsize = (7, 8))
X, Y = np.meshgrid(thetas, nterms)
plt.subplots_adjust(left=0.15,bottom=0.0)

#ax = fig.add_subplot(111, projection="3d")
#ax.set_xlabel("theta")
#ax.set_zlabel("Error[%]")
#ax.set_ylabel("nterm")
#ax.set_zlim(0.0,np.max(cy)*1.2)
#ax.plot_surface(X, Y, cy, cmap = "summer")
#ax.scatter(X, Y, cy, s=10)

fontsize = 24
plt.title("Error[%]",fontsize=fontsize)
plt.contourf(X, Y, cy,levels=300,cmap='jet')
plt.xlabel("theta [-]",fontsize=fontsize)
plt.ylabel("nterm",fontsize=fontsize)
plt.tick_params(labelsize=fontsize)

cbar = plt.colorbar(orientation="horizontal",ticks=[0.0,0.005,0.01,0.015,0.02,0.025,0.03,0.04])
cbar.ax.tick_params(labelsize=fontsize)
cbar.mappable.set_clim(0.0,0.04)

plt.show()
