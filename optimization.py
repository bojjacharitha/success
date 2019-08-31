from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import*
import numpy as np

len=1000
x,y=np.meshgrid(np.linspace(-5,5,len),np.linspace(-5,5,len))
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
z=x*y
ax.plot_surface(x,y,z,color='g',alpha=1)
plt.show()
