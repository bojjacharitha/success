# success
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
len = 10
xx, yy = np.meshgrid(range(len), range(len))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')

#defining point of intersection
P = np.array([1,6,-7])

#defining planes
n1 = np.array([1,2,1]).reshape((3,1))
c1 = 6
n2 = np.array([1,8,7]).reshape((3,1))
c2 = 0
n3 = np.array([9,2,3]).reshape((3,1))
c3 = 0
n4 = np.array([1,1,1]).reshape((3,1))
c4 = 0

#corresponding z for planes
z1 = ((c1-n1[0]*xx-n1[1]*yy)*1.0)/(n1[2])
z2 = ((c2-n2[0]*xx-n2[1]*yy)*1.0)/(n2[2])
z3 = ((c3-n3[0]*xx-n3[1]*yy)*1.0)/(n3[2])
z4 = ((c4-n4[0]*xx-n4[1]*yy)*1.0)/(n4[2])

#plotting planes
ax.plot_surface(xx, yy, z1, color='r',alpha=0.2)
ax.plot_surface(xx, yy, z2, color='b',alpha=0.2)
ax.plot_surface(xx, yy, z3, color='b',alpha=0.2)
ax.plot_surface(xx, yy, z4, color='b',alpha=0.2)

#plotting point
ax.scatter(P[0],P[1],P[2],'o',label="Point P")

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()

plt.show()
