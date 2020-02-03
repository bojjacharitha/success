from sklearn.datasets import make_regression
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import Ridge

X, y, coefficients = make_regression(
    n_samples=50,
    n_features=1,
    n_informative=1,
    n_targets=1,
    noise=5,
    coef=True,
    random_state=1
)
alpha = 100

n, m = X.shape
I = np.identity(m)
w = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X) + alpha * I), X.T), y)
print(w)
print(coefficients)

plt.scatter(X, y)

plt.plot(X, w*X, c='red')
plt.title('')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

