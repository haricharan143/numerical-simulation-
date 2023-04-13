##root finding
##biection method
import numpy as np
def my_bijection(f,a,b,tol):
    if np.sign(f(a))==np.sign(f(b)):
        return "invalid"
    m=(a+b)/2
    if np.abs(f(m))<tol:
        return m
    elif np.sign(f(a))==np.sign(f(m)):
        return my_bijection(f, m, b, tol)
    elif np.sign(f(b))==np.sign(f(m)):
        return my_bijection(f, a, m, tol)
def f(x):
    return x**3 - 3*x + 1
root = my_bijection(f, 0, 1)
print(root)
##Newton-Raphson Method
import numpy as np
f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
newton_raphson = 1.4 - (f(1.4))/(f_prime(1.4))
print("newton_raphson =", newton_raphson)
print("sqrt(2) =", np.sqrt(2))
def my_newton(f,df,x0,tol):
    if abs(f(x0))<tol:
        return x0
    else:
        return my_newton(f, df, x0-f(x0)/df(x0), tol)
estimate = my_newton(f, f_prime, 1.5, 1e-6)
print("estimate =", estimate)
print("sqrt(2) =", np.sqrt(2))
