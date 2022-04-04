import matplotlib.pyplot as plt
import numpy  as np

x=np.array([1,2,3,4])
mylabels=["bananas","guava","apples","oranges"]
myexplode=[0.2,1,0]
plt.pie(x,labels=mylabels,explode=myexplode)
plt.show()

#explode should be first initialised as an array.
# value of explode is somewhere between 0 and 1.
# explode basically means the distance from the centre point
