import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3])
y=np.array([5,6,7])
plt.title("Watches")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.grid()   #use this to show a grid at the background
plt.plot()

#  grid(axis='y') -for lines perpendicular to y axis
#  grid(axis='x') -for lines perpendicular to x axis
#  grid(color="red",lw='3',ls='dashed') - any one or none can be used along with the above comment in one single comment or separately

