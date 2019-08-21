import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linalg as LA


fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

len = 50

y2 = np.linspace(-10,10,len)
y1 = np.power(y2,2)/4
y = np.vstack((y1,y2))

x_par = y

P = np.array([2,2*np.sqrt(2)])
Q = np.array([8,-4*np.sqrt(2)])
O = np.array([0,0])
x_PQ=np.zeros((2,len))
lam=np.linspace(-1,2,len)
for i in range(len):
 temp1=P + lam[i]*(Q-P)
 x_PQ[:,i]=temp1.T

plt.plot(x_par[0,:],x_par[1,:],label='$Parabola$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.grid()
plt.legend()

plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1),P[1]*(1),'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1),Q[1]*(1),'Q')
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1),O[1]*(1),'O')

ax.plot()
plt.xlabel('https://github.com/gadepall/school/raw/master/linalg/2D/circle/jee_linalg_2d_circle.pdf$x$');plt.ylabel('$y$')
plt.axis('equal')
plt.show()
