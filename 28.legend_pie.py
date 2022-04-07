import matplotlib.pypot as plt
import numpy as np

x=np.array([3,4,3])
mylabels=["apple","banana","guava"]
mycolors=["red","k","white"]
plt.pie(x,labels=mylabels,colors=mycolors)

plt.legend()  #this function helpus us create the key. (Like scale in map,helps us which color points to what parameter)
plt.show()