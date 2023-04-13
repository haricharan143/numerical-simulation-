##interpolation
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
x=[11,1,2]
y=[1,43,112]
f=interp1d(x,y)
y_h=f(1.5)
print(y_h)
plt.figure(figsize = (10,8))
plt.plot(x,y,'-ob')
plt.plot(1.5,y_h,'ro')
plt.title('Linear Interpolation at x = 1.5')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
##cubic spline interpolation
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
x=[0,1,2]
y=[1,3,2]
f=CubicSpline(x,y,bc_type='natural')
x_new=np.linspace(0, 2, 100)
y_new=f(x_new)
plt.figure(figsize = (10,8))
plt.plot(x_new, y_new, 'b')
plt.plot(x, y, 'ro')
plt.title('Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
##Lagrange Polynomial Interpolation
import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
x=[0,1,2]
y=[1,3,2]
P1coeff=[1,-1.5,.5]
P2coeff=[0,2,-1]
P3coeff=[0,-.5,.5]
P1=poly.Polynomial(P1coeff)
P2=poly.Polynomial(P2coeff)
P3=poly.Polynomial(P3coeff)
xnew = np.arange(-1.0, 3.1, 0.1)
fig=plt.figure(figsize = (10,8))
plt.plot(xnew,P1(xnew),'b',label='P1')
plt.plot(xnew,P2(xnew),'r',label='P2')
plt.plot(xnew,P3(xnew),'g',label='P3')
plt.plot(x,np.ones(len(x)),'ko',x, np.zeros(len(x)),'ko')
plt.title('Lagrange Basis Polynomials')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()
##Newton’s Polynomial Interpolation
import numpy as np
import matplotlib.pyplot as plt
def divided_diff(x,y):
    n=len(y)
    coef=np.zeros([n,n])
    coef[:,0]=y    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1]-coef[i][j-1])/(x[i+j]-x[i])            
    return coef
def newton_poly(coef, x_data,x):
    n=len(x_data)-1 
    p=coef[n]
    for k in range(1,n+1):
        p=coef[n-k]+(x -x_data[n-k])*p
    return p
x = np.array([-5,-1,0,2])
y = np.array([-2,6,1,3])
a_s = divided_diff(x, y)[0,:]
x_new = np.arange(-5, 2.1, .1)
y_new = newton_poly(a_s, x, x_new)
plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)