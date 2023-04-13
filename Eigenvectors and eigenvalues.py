##eigenvalues and eigen vectors
import numpy as np
from numpy.linalg import eig
a=np.array([[3,2],[5,3]])
x=np.array([1,-1])
v,w=eig(a)
print(v)
print(w)
#1
import numpy as np
from numpy.linalg import qr
a = np.array([[0, 2], 
              [2, 3]])
q,r=qr(a)
print('Q:',q)
print('R:',r)
b=np.dot(q,r)
print('QR:', b)
#2
import numpy as np
from numpy.linalg import eig
f=np.array([[1,2,3],[5,6,7],[11,12,12]])
v,w=eig(f)
print("eigen vector",v)
print("eigenvalues",w)
#problems
#1
import numpy as np
from numpt.linalg import eig
g=np.array([[3,2],[5,3]])
v,w=eig(g)
print(v)
print(w)
#2
import numpy as np
x=np.array([[1,2],[2,3]])
g=np.array([[3,2],[5,3]])
if np.dot(g,x)==np.dot(v,x):
    print("varified")
else:
    print("not varified")
#3
import numpy as np
A=np.array([[2,1,2],[1,3,4],[2,1,1]])
x0=np.array([1,1,1])
num_iterations = 8
x=x0
for i in range(num_iterations):
    x=np.dot(A,x)
    x=x/np.linalg.norm(x)
lambd=np.dot(np.dot(A,x),x)
print("Largest eigenvalue:",lambd)
print("Eigenvector:",x)
#4
import numpy as np
A = np.array([[2,1,2],[1,3,4],[2,2,1]])
eigenvalues,eigenvectors = np.linalg.eig(A)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)


