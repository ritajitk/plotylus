import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from pylab import rcParams
rcParams['figure.figsize'] = 9, 9
import matplotlib.tri as mtri

## 3D surface_plot
fig = plt.figure()
axes = fig.gca(projection='3d')

data = np.loadtxt('2D-data.txt')
x = data[:,0]
y = data[:,1]
z = data[:,2]

tri = mtri.Triangulation(x,y)
axes.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral,linewidth=0.2, antialiased=True)

axes.set_xlabel('$x$',fontsize=15)
axes.set_ylabel('$y$',fontsize=15)
axes.set_zlabel('$z$',fontsize=15)
plt.tight_layout()
fig.savefig('surface.pdf',format='pdf', dpi=1200)
plt.show()