import matplotlib.pyplot as plt
import numpy as np

x=np.arr([1,2,3,4])
y=np.array([5,6,7,8])

colors=np.arr([10,20,30,40])               #locations on the color map
plt.scatter(x,y,c=colors,cmap="virdis")   # cmap is the keyword to access the color map 'virdis'
plt.show()