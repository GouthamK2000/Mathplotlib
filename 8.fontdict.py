
import matplotlib.pyplot as plt
import numpy as np

x=np.array([3,4,2])
y=np.array([7,6,1])
font1={'family':'seriff','color':'blue','size':'20'}
plt.xlabel("Time",fontdict=font1)
plt.plot(x,y)
plt.show()

#any number of such fonts can be declared  and any number can be used.....
#It can be only used inside  xlabel,ylabel,title...
#fontdict is a keyword and must be used..