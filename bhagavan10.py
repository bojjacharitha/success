import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-3,3,50,endpoint=True)

def f(x):return x**3-3*x
for x in [1,2,0]:
 print(x,f(x))

P=f(X)
plt.legend(loc='best')
plt.plot(X,P)
plt.grid()

plt.show()
