import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm    
from pylab import rcParams
rcParams['figure.figsize'] = 9, 9
from scipy.interpolate import griddata


## 3D surface_plot
fig = plt.figure()
axes = fig.add_subplot(111, projection='3d') #gca = get current axis

data = np.loadtxt('2D-data.txt')
x = data[:,0]
y = data[:,1]
z = data[:,2]

xi = np.unique(x)
yi = np.unique(y)
xv, yv = np.meshgrid(xi,yi)

Z = griddata((x, y) , z , (xv, yv), method='cubic')

# surface_plot with color grading and color bar
p = axes.plot_surface(xv,yv,Z, rstride=4, cstride=4, cmap=cm.RdBu, 
    linewidth=0, antialiased=False)
fig.colorbar(p, shrink=0.5)
axes.set_xlabel('$x$',fontsize=15)
axes.set_ylabel('$y$',fontsize=15)
axes.set_zlabel('$z$',fontsize=15)
plt.tight_layout()
fig.savefig("surface.pdf")
plt.show()
