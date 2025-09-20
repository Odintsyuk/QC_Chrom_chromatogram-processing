import math
from sympy.geometry import *
P1 = Point(1, 1) #
P2 = Point(2, 2) # 
P3 = Point(3, 1) #

t = Triangle(P1, P2, P3)
s = abs(float(t.area))
d = math.sqrt((P3[1]-P1[1])**2 + (P3[0]-P1[0])**2)
H = 2 * s / d
print(H)
print(s)
