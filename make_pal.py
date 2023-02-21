'''
Make ODV .pal colormap files from cmocean rgb files.
This reads in the colormap rgb from github directly, and it is stored
locally by np.genfromtxt.
'''

import numpy as np
import os
import cmocean


N = 256

# location of local rgb files
loc = 'https://raw.githubusercontent.com/matplotlib/cmocean/master/cmocean/rgb/'

if not os.path.exists('pal'):
    os.makedirs('pal')

# file name
# fname = File.split('/')[-1].split('-')[0]
f = open('colorscales.js', 'w')

f.write('export const colorscales = { \n')

# Loop through rgb files and make pal file
for name in cmocean.cm.cmapnames:

    # file import
    file = loc + name + '-rgb.txt'

    # read in rgb values
    rgb = np.genfromtxt(file)

    # convert to colormap
    cmap = cmocean.tools.cmap(rgb, N=N)

    # back to rgb, now correct number of levels
    rgb = cmocean.tools.print_colormaps([cmap], N=N)[0]

    f.write(name+': new Uint8Array([')

    for j in range(N):
        f.write('%.0f, %.0f, %.0f, 255,' % (rgb[j, 0]*255, rgb[j, 1]*255, rgb[j, 2]*255))

    f.write(']) ,\n')

    f.write(name+'_r : new Uint8Array([')

    for j in range(N):
        f.write('%.0f, %.0f, %.0f, 255,' % (rgb[255-j, 0]*255, rgb[255-j, 1]*255, rgb[255-j, 2]*255))

    f.write(']) ,\n')

f.write('}')

f.close()
