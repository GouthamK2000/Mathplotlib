import matplotlib.pyplot as plt
import numpy as np

x=np.array(["a","b","c","d"])
y=np.array([1,2,3,4])

plt.barh(x,y,height=0.2)
plt.show()

#height parameter is used in barh, for determing the  WIDTH of the bar.
#height values range between 0 and 1, like width in bar.