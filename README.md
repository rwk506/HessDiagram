Hess
================================

<h3>A Python plotting tool for creating a Hess diagram out of a color-magnitude diagram.</h3>

<br />

<h4>Table of Contents</h4>

[Summary](#Summary)<br />
[Downloading and Installation](#Install)<br />
[Example of Use](#Use)<br />
[Documentation](#Doc)<br />
[Dependencies](#Deps)<br />
[Other Information](#Other)<br />
<br /><br />


<a name="Summary"/>
<h4>Summary</h4>

This repository houses a Python script that allows the user to easily plot a Hess diagram from stellar photometry. The Python script contains a function written to plot all a color-magnitude diagram (CMD) of stellar photometry and plot a contour on top showing the stellar point density across the CMD. This is especially useful for CMDs for galaxies or dense star clusters that have many thousands of points, making it easier to see variations in the density of stars along the main sequence, sub- or red-giant branches.


<br /> <br /><br />





<a name="Install"/>
<h4>Downloading and Installation</h4>

The source code and necessary data files may all be downloaded as a zip, forked, or cloned on a local machine from the [Hess](https://github.com/rwk506/HessDiagram) repository.

The primary Python script included is **HessCMD.py** The files included are:

- **HessCMD_withoptions.png**: Example output plot of code run
- **HessCMD.py**: Python code defining plotHess() function
- **HessExample.py**: Example code to run/edit for user's own implementation
- **photometry.txt**: File containing data to be used in example code


If the user has Python and the necessary packages installed, no further installation should be required to run the code. If scripted, code may be run from outside Python with the command-line call 'python example.py' (where example is the name of the script). If inside Python, the function HessCMD() may be called following importing the necessary packages and:

import HessCMD.py

Then the plotHess() function may be called as per the documentation and example provided.



<br /> <br /><br />

<a name="Use"/>
<h4>Example of Use</h4>

The HessCMD.py package houses the plotHess() function, which will plot the CMD with a contour plot of density. The function requires 1-D arrays color and magnitude. For those unfamiliar with python, an example of importing a photometry file (e.g. the included file photometry.txt) may be imported with the command:

mag1, mag2 = loadtxt('photometry.txt', unpack=True) # example photometry

Then, color can be calculated:

color = mag1 - mag2

The results can then be plotted using the defaults simply by:

HessCMD.plotHess(mag2, color)

Or additional options can be included, e.g.:

HessCMD.plotHess(mag2, color, levels=arange(25,225,25), cbarrtitle='Density', xlabel='F606W $-$ F814W (mag)', ylabel='F814W (mag)', saveas='HessCMD_withoptions.png', cbarr='Yes')

Other options are also available; full documentation is given in the function description.




<br /> <br /><br />

<a name="Docs"/>
<h4>Documentation</h4>

<h5>plotHess()</h5>

This is a function that will take arrays of color and magnitude from stellar photometry and create a Hess diagram.

plotHess(mag,color) is a function intended to create a contour plot of stellar density in the canonical Color-Magnitude Diagram (CMD). plotHess() plots all the stars in the CMD and then overplots a contour of their density.

mag = magnitudes of the stars
color = colors of the stars
mag and color are required to run plotHess() and need to be the same length arrays.


Optional keyword arguments:

**Keyword** &nbsp; &nbsp; &nbsp; &nbsp; **Description**<br />
*levels*: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; levels to be used for density contour; if 'None', the defaults are defined by the contour() function, which may not be optimal for the users dataset and may be changed if necessary.<br />
*ylims*: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; define the y-range of the plotted values; defaults will need to be changed to fit user's data.<br />
*xlims*: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; define the x-range of the plotted values; defaults will need to be changed to fit user's data.<br />
*colormap*: &nbsp; &nbsp; allows the user to choose a Python color map to use for the contour; the default is grayscale.<br />
*cbarr*: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 'None' means the colorbar will not be plot as a default. To change this, set cbarr='Yes'; in a true Hess diagram, the cbarr values represent the stellar point density in the CMD plot.<br />
*cbarrtitle*:  sets the title for the colorbar; should be string<br />
*xlabel*: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sets the xlabel for the plot; should be string<br />
*ylabel*: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; sets the ylabel for the plot; should be string<br />
*saveas*: &nbsp; &nbsp; &nbsp; &nbsp; pathway for saving the output plot. The default is to save in the same folder as "HessCMD.png"<br />

<br /> <br /><br />




<a name="Deps"/>
<h4>Dependencies</h4>

This Python code was written using Python 2.6 and Numpy 1.5.1, but should be compatible with many other versions (though not Python 3.0 or higher). The user may have to install the matplotlib and pylab packages.

Compatible with iPython Notebook (Use %run [name]).




<br /> <br /><br />

<a name="Other"/>
<h4>Other Information</h4>

Author: RWK <br />
License: None, free to use and edit as people wish. <br />
Contact: May be made through GitHub. <br />

