##linear algebra and system of linear algebra
#1
import numpy as np
from np.linalg import norm
from numpy import arccos, dot
v=np.array([[10,9,3]])
w=np.array([[2,5,12]])
theta =arccos(dot(v, w.T)/(norm(v)*norm(w)))
print(theta)
v=np.array([[0,2,0]])
w=np.array([[3,0,0]])
print(np.cross(v,w))
P=np.array([[1,7],[2,3],[5,0]])
Q=np.array([[2,6,3,1],[1,2,3,4]])
print(P)
print(Q)
print(np.dot(P,Q))
np.dot(Q,P)
#1
import numpy as np
s=np.array([[1,1,2],[2,4,5],[7,8,10]])
f=np.array([1,2,3])
print(np.dot(s,f))
x=np.linalg.solve(s,f)
print(x)
#2
import numpy as np
def my_is_orthogonal(v1, v2, tol):
    dot_product = np.dot(v1, v2)
    norm_product = np.linalg.norm(v1) * np.linalg.norm(v2)
    cos_theta = dot_product / norm_product
    theta = np.arccos(cos_theta)
    return 1 if abs(np.pi/2 - theta) < tol else 0
a = np.array([[1], [0.001]])
b = np.array([[0.001], [1]])
my_is_orthogonal(a,b, 0.01)
