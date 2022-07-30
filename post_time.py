# -*-coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def frange(x,y,jump):
  while x <= y:
    x = round(x,2)
    yield x
    x += jump

steps = 1000-2

start_nterm = 5
end_nterm = 11
d_nterm = 1
nterms = range(start_nterm,end_nterm+1,d_nterm)

start_nump = 100
end_nump = 400
d_nump = 50
numps = range(start_nump,end_nump+1,d_nump)

start_theta = 0.1
end_theta = 1.0
d_theta = 0.1
thetas = list(frange(start_theta,end_theta,d_theta))

#--------------------------------------------------------
#- Default
#--------------------------------------------------------
file_name = "./time/check_elapsed_time.dat"
with open(file_name,'r') as infile:
  for i in range(steps): next(infile)
  s_line = infile.readline()
  data = s_line.split(" ")
  data = [x for x in data if x]
  cy0 = float(data[4])
#--------------------------------------------------------


cy = np.zeros([len(numps),len(thetas)])
for i,theta in enumerate(thetas):
  #for j,nump in enumerate(numps):
  for j,nterm in enumerate(nterms):
    #file_name = "./time/check_elapsed_time_" + str(nump) + "_" + str(theta) + ".dat"
    file_name = "./time/check_elapsed_time_" + str(nterm) + "_" + str(theta) + ".dat"
    with open(file_name,'r') as infile:
      for k in range(steps): next(infile)
      s_line = infile.readline()
      data = s_line.split(" ")
      data = [x for x in data if x]

      cy[j][i] = (float(data[4]))
      if(cy[j][i]<0.1): cy[j][i] = 0.1


#cy[0][0] = 0.4
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
plt.title("CPU Time[s]",fontsize=fontsize)
plt.contourf(X, Y, cy,levels=300,cmap='jet')
plt.xlabel("theta [-]",fontsize=fontsize)
plt.ylabel("nterm",fontsize=fontsize)
plt.tick_params(labelsize=fontsize)

cbar = plt.colorbar(orientation="horizontal",ticks=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7])
cbar.mappable.set_clim(0.1,0.4)
cbar.ax.tick_params(labelsize=fontsize)

plt.show()

