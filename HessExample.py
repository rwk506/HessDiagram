from pylab import *
from numpy import *
from random import *
from scipy import *
from matplotlib import *
rcdefaults()
matplotlib.rc('font',family='Bitstream Vera Serif')

import HessCMD

#########  Example  #########

### load in data and define color and magnitude
viall=loadtxt('photometry.txt') # example photometry
mag1=viall[:,0]  #606 (~V)
mag2=viall[:,1]  #814 (~I)
color=mag1-mag2  # F606W - F814W (~(V-I) color)


#### run plotHess() on magnitude and color:
# utilize options to: define levels, save as a particular file, include a colorbar, set labels, etc.
HessCMD.plotHess(mag2, color, levels=arange(25,225,25), cbarrtitle='Density', xlab='F606W $-$ F814W (mag)', ylab='F814W (mag)', saveas='HessCMD_withoptions.png', cbarr='Yes')

