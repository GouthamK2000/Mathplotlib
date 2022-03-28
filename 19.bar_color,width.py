from turtle import color
import matplotlib.pyplot as plt
import numpy as np

x=np.array([3,6,1])
y=np.array([9,3,5])
plt.bar(x,y,color='green',width=0.3)
plt.show()

# colors can be hexadecimal value or normal color
# colors and width can be declared simultaneously or at different places
# width of the bar must be betwwen 0 and 1.
# Default width = 0.8

