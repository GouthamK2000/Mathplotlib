#here only the points are shown

import matplotlib.pyplot as plt
import numpy as np

x=np.array([6,7,7,0])
y=np.array([3,5,1,2])
plt.plot(x,y,'o') #use o inbetween '' , 'o' to print only the points/nodes
plt.show()