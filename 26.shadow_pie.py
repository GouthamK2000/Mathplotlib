import matplotlib.pyplot as plt
import numpy as np

x=np.array([8,3,4])
mylabel=["apples","oranges","bananas"]
myexplode=[0.5,0.6,0.3]
plt.pie(x,labels=mylabel,explode=myexplode,shadow=True)
plt.show()

# Shadow is a keyword which allows us to provide shadow effects to the pie chart, even for parameters having explode functions.




