##Least Squares Regression 
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
x=np.linspace(0,1,101)
y=1+x+x*np.random.random(len(x))
A=np.vstack([x,np.ones(len(x))]).T
y=y[:,np.newaxis]
alpha=np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
print(alpha)
plt.figure(figsize=(10,8))
plt.plot(x,y,'b.')
plt.plot(x,alpha[0]*x+alpha[1],'g')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#1
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
x=np.linspace(0,10,101)
y=0.1*np.exp(0.3*x)+0.1*np.random.random(len(x))
plt.figure(figsize=(10,8))
plt.plot(x, y,'g.')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#3
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
A = np.vstack([x, np.ones(len(x))]).T
beta, log_alpha = np.linalg.lstsq(A, np.log(y), rcond = None)[0]
alpha = np.exp(log_alpha) 
plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha*np.exp(beta*x), 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
