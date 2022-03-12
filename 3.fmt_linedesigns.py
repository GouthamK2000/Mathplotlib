# basic syntax: marker-line design-color

import matplotlib.pyplot as plt
import numpy as np
x=np.array([9,6,3])
y=np.array([1,2,3])
plt.plot(x,y,'2-.w')  # this is the place where we specify marker-line-color, without any space
plt.show()

# all lines available for plotting

# Line     Syntax	Description
# '-'	     Solid line	
# ':'  	Dotted line	
# '--'	Dashed line	
# '-.'	Dashed/dotted line