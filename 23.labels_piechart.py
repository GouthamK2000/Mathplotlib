import matplotlib.pyplot as plt
import numpy as np

x=np.array([3,2,5,6])
mylabels=(["Apple","orange","grapes","banana"])
plt.pie(x,labels=mylabels) #labels should be declared as an array earlier
plt.show()