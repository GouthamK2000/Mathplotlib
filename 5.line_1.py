#line properties

import matplotlib.pyplot as plt
import numpy as np

x=np.array([9,5])
y=np.array([4,5])
z=np.array([6,3])
plt.plot(x,color="pink")  
plt.plot(y,linewidth="15")
plt.plot(z,linestyle='dashed')  # we can use -- ,-.  etc here.
plt.show()

#hexadecimal color values can be used in place of color (or), we can also use the short for of color names
#color and linewidth can be used separately or together.
#shortforms: 1.linestyle -- ls , 2.linewidth -- lw , 3.color -- c