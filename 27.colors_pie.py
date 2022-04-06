import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,5,3])
mylabels=["BMW","Audi","Jaguar"]
mycolors=["pink","k","red"]
plt.pie(x,labels=mylabels,shadow=True,colors=mycolors)
plt.show()

#colors should be declared like displaying data in any other formats.
#colors can be declared in hexadecimal values, or by color names or by single alphabet codes.A combination of all of these can be used as well, in the same pie chart.