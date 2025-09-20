import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

x = np.array([0,1,2,3,4])
x2 = np.array([0, 1, 2, 3, 4])

y = np.array([1,2,3,2,1])
y2 = np.array([1, 1, 2, 1, 1])

f1 = InterpolatedUnivariateSpline(x, y, k=1)
f2 = InterpolatedUnivariateSpline(x2, y2, k=1)
sup = f1.integral(0, 4)
sdown = f2.integral(0,4)
print(sup, sdown, (sup - sdown))
