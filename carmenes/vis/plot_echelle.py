import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import CCD_vis
import pylab as p
file = open('echelle_orders_main.txt','r')
#file0 = open('echelle_orders_shifted.txt','r')
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
wav = []
x = []
y = []
z = []

wav1 = []
x1 = []
y1 = []
z1 = []

dwav = []
dx1 = []
dy1 = []
dz1 = []


for line in file:
    linea = line.split()
    wav.append(float(linea[1]))
    x.append(float(linea[2]))
    y.append(float(linea[3]))
    z.append(float(linea[4]))
    
'''
for line in file0:
    linea = line.split()
    wav1.append(float(linea[1]))
    x1.append(float(linea[2]))
    y1.append(float(linea[3]))
    z1.append(float(linea[4]))
    

    
ccd_x = 4240
ccd_y = 4190
decx = 2730
decy = 23600
x_ccd, y_ccd = CCD_vis.mmtopix(x,y, decx, decy)
x1_ccd, y1_ccd = CCD_vis.mmtopix(x1,y1, decx, decy)
print len(x_ccd),len(x1_ccd)

for i in range(len(x_ccd)):
    dx1.append(x_ccd[i]-x1_ccd[i])
    dy1.append(y_ccd[i]-y1_ccd[i])
    dz1.append(z[i]-z1[i])
    dwav.append(wav[i] - wav1[i])


#for k in range(len(x)):
    #plt.arrow(x_ccd[k], y_ccd[k], dx1[k], dy1[k],fc="k", ec="k",head_width=55, head_length=100)

#fig = plt.figure()
#for k in range(len(z)):
    #plt.arrow(wav[k], z[k], 0, dz1[k],fc="k", ec="k",width = 0.0001, head_width=0.0009, head_length=0.1)





plt.xlim(0, ccd_x)
plt.ylim(0, ccd_y)
plt.plot(x_ccd, y_ccd, 'b.')
'''
plt.plot(x,y,'b.')
plt.xlabel('Echelle dispersion axis [pix]')
plt.ylabel('Cross-dispersion axis [pix]')
#plt.savefig('vis_echelle_main_10pporder_1.png')
plt.show()
