##Visualization and plotting
#1
import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4])
y=np.array([2,3,4,5])
plt.plot(x,y)
plt.show()
#2
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-11, 11,200)
plt.plot(x,x**3)
plt.plot()
#3
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-11, 11,200)
plt.plot(x,x**6,"bo")
plt.plot()
#4
x = np.linspace(-5,5,20)
plt.plot(x, x**2, 'ko')
plt.plot(x, x**3, 'r*')
plt.show()
#5
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
x=np.linspace(0,1,101)
y = 1 + x + x * np.random.random(len(x))
A=np.vstack([x,np.ones(len(x))]).T
y=y[:,np.newaxis]
beta=np.dot(np.dot(np.linalg.inv(np.dot(A.T,A)),A.T),y)
print(beta)
plt.figure(figsize = (10,8))
plt.plot(x, y, 'g.')
plt.plot(x, beta[0]*x + beta[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#6
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')
plt.show()
