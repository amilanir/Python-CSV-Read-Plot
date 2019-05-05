# -*- coding: utf-8 -*-
"""
Created on Sun May  1 11:47:35 2016

@author: Amila Perera
"""
import pylab
import numpy as np
import matplotlib.pyplot as plt
import os

from matplotlib.pyplot import cm
import matplotlib.pyplot as plt

##os.chdir('D:')
#for i in range(10,100):
#
#        
#    datafile = open('data'+str(i)+'.csv','r')
#    XAccel = []
#    Time =[]
#    dataLines = datafile.readlines()
#    interesting = False
#    for line in dataLines[2:]:
#        entries =  line.split(',')
#        Time.append(int(entries[0]))        
#        XAccel.append(int(entries[1]))
#        if XAccel[-1]>33000 or XAccel[-1]<31000:
#            interesting=True
#    if interesting:
#        print('data'+str(i)+'.csv is interesting.')
#        fig = plt.figure(figsize=(9,9))
#        plt.scatter(Time,XAccel, s=20, label='Measurement', c='k')
#        plt.show()
        
datafile = open('data2.csv','r')        
XAccel = []
Time =[]
dataLines = datafile.readlines()
for line in dataLines[2:]:
    entries =  line.split(',')
    Time.append(float(entries[0]))        
    XAccel.append(float(entries[1]))

fig = plt.figure(figsize=(9,9))
plt.plot(Time,XAccel)
#plt.xlim(6.75e8,6.86e8)
plt.show()        



x, y = np.meshgrid(np.arange(0, 20), np.arange(0, 200))

pylab.close('all')
pylab.ion()
#pylab.figure(figsize=[20, 8])
#pylab.contour(x, y, psi, 20, colors='k', linestyles='-', linewidth=1.0)
pylab.quiver(Time, XAccel, Time, XAccel, angles='uv', scale_units='xy', scale=60)

#ax = pylab.axes()
#ax.set_aspect(1.)

import numpy as np
import matplotlib.pyplot as plt
soa =np.array( [ [0,0,3,2], [0,0,1,1],[0,0,9,9]]) 
X,Y,U,V = zip(*soa)
plt.figure()
ax = plt.gca()
ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)
ax.set_xlim([-1,10])
ax.set_ylim([-1,10])
plt.draw()
plt.show()

Y, X = np.mgrid[-3:3:15j, -3:3:15j]
U = -1 - np.cos(X**2 + Y)
V = 1 + X - Y
speed = np.sqrt(U**2 + V**2)
UN = U/speed
VN = V/speed

plot1 = plt.figure()
plt.quiver(X, Y, UN, VN,        # data
           U,                   # colour the arrows based on this array
           cmap=cm.seismic,     # colour map
           headlength=7)        # length of the arrows

plt.colorbar()                  # adds the colour bar

plt.title('Quive Plot, Dynamic Colours')
plt.show(plot1)                 # display the plot