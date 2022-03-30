import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(170,10,250) #-----> 1
plt.hist(x) #this keyword helps us to geneate a histogram.
plt.show()
print (x)

#1
# ther e should be 3 parameters inside the np.random.normal().
# first one is the number, around which we wish to generate random numbers.
#second number is the number , which states the standard deviation of the given number.
#third number is the number of random numbers we wish to generate.