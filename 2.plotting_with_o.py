import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,5,2,9])
y=np.array([5,9,0,3])
plt.plot(x,marker='o',ms='20',mec='b',mfc='m')
plt.plot(y,marker='D',ms='10',mec='g',mfc='b')
plt.show()