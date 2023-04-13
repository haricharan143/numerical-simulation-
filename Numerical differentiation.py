##Numerical differentiation
##Finite Difference Approximating Derivatives
import numpy as np
import matplotlib.pyplot as plt
h=0.1
x=np.arange(0,2*np.pi,h) 
y=np.cos(x) 
forwarddiff=np.diff(y)/h 
xdiff = x[:-1:] 
exactsolution = -np.sin(xdiff) 
plt.figure(figsize = (12, 8))
plt.plot(xdiff, forwarddiff, '--', \
         label='Finite difference approximation')
plt.plot(xdiff, exactsolution, \
         label='Exact solution')
plt.legend()
plt.show()
max_error=max(abs(exactsolution-forwarddiff))
print(max_error)
##example
h=1
iterations = 20 
step_size=[] 
max_error=[] 
for i in range(iterations):
    h /= 2 
    step_size.append(h) 
    x=np.arange(0,2*np.pi,h) 
    y=np.cos(x) 
    forward_diff=np.diff(y)/h 
    x_diff = x[:-1] 
    exact_solution = -np.sin(x_diff) 
    max_error.append(\
            max(abs(exact_solution - forward_diff)))
plt.figure(figsize = (12, 8))
plt.loglog(step_size, max_error, 'v')
plt.show()
##Approximating of Higher Order Derivatives
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,2*np.pi,0.01) 
omega=100
epsilon=0.01
y=np.cos(x) 
y_noise=y+epsilon*np.sin(omega*x)
plt.figure(figsize=(12,8))
plt.plot(x, y_noise,'r-', \
         label='cos(x)+noise')
plt.plot(x, y,'b-', \
         label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
