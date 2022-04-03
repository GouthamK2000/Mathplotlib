import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,4,7,2])
mylables=("apple","orange","banana","grapes")
plt.pie(x,labels=mylabels,startangle=180) #startangle tells us where the pie chart starts
plt.show()

# angles are :

# +x=0 (default)
# +y=90
# -x=180
# -y=270
