##numerical integration
#Riemanns Integral
import numpy as np
a=0
b=np.pi
n=11
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
f=np.sin(x)
I_r=h* sum(f[:n-1])
err_r=2-I_r
I_R=h*sum(f[1::])
err_R=2-I_R
I_mid=h*sum(np.sin((x[:n-1]+x[1:])/2))
err_mid=2-I_mid
print(I_r)
print(err_r)
print(I_R)
print(err_R)
print(I_mid)
print(err_mid)
##Trapezoid Rule
import numpy as np
a=0
b=np.pi
n=11
h=(b-a)/(n-1)
x=np.linspace(a, b, n)
f=np.sin(x)
I_trap=(h/2)*(f[0]+2*sum(f[1:n-1])+f[n-1])
err_trap=2-I_trap
print(I_trap)
print(err_trap)
##Simpson’s Rule
import numpy as np
a=0
b=np.pi
n=11
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
f=np.sin(x)
I_simp=(h/3)*(f[0]+2*sum(f[:n-2:2])+4*sum(f[1:n-1:2])+f[n-1])
err_simp=2-I_simp
print(I_simp)
print(err_simp)
##Computing Integrals in Python
import numpy as np
from scipy.integrate import trapz
a= 0
b=np.pi
n=11
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
f=np.sin(x)
I_trapz=trapz(f,x)
I_trap=(h/2)*(f[0]+2*sum(f[1:n-1])+f[n-1])
print(I_trapz)
print(I_trap)
