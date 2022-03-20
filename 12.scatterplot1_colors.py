from gettext import npgettext
import matplotlib.pylot as plt
import numpy as np

x=np.array([1,2,3])
y=np.array([6,5,4])

colors=np.array(["blue","green","red"])

plt.scatter(x,y,c=colors)
plt.show()