import matplotlib.pyplot as plt
import numpy as np

x=np.array([4,5])
y=np.array([7,2])

plt.plot(x,marker='1',mec='r',mfc='b') # we can separately specify mec,marker and mfc
plt.plot(y,marker='^',mec='b',mfc='g')#Same s above
plt.show()

# mec -- marker edge colour
#mfc -- marker face color