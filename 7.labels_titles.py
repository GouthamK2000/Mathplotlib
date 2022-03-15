import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,4])
y=np.array([6,3,8])
plt.title("Average Grades",loc="left")  #plt.title helps us giving the title for the pictorial representation we have
plt.xlabel("Year")                      #plt.xlabel/ylabel provides the component in x,y axis respectively
plt.ylabel("Grades")        
plt.plot()

#loc helps us to 'move' the headings around.It can be used both with titles and labels
# Use left,right,top and bottom keywords to move accordingly.