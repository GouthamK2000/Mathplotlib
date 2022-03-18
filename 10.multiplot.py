#multiple graphs can be plotted in the same page

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,4,5])
y=np.array([4,1,3])
plt.subplot(1,2,1)  #contains 1 row, 2 columns and this is the first plot
plt.plot()
plt.title("sales")

x=np.array([7,8,4])
y=np.array([3,1,2])
plt.subplot(1,2,2) #contains 1 row, 2 columns and this is the 2nd plot
plt.plot()
plt.title("Working hours")

plt.suptitle("Effectiveness")  #over all title for both the graphs,for the entire figure
plt.show()

#3rd Value in the subplot is always in numeric order.
#First and the second values depend on the number of rows and coolumns in the entire graph diagram.