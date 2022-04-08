import matplotlib.pyplot as plt
import numpy as np

x=np.array([4,2,7,9])
mylabels=["Grapes","Oranges","Apples","berries"]

plt.pie(x,labels=mylabels)
plt.legend(title="Fruits: ")  #In piechart,title inside the legend function will give the title for the map-key on the side
plt.show()