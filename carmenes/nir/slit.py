import numpy as np
import pyfits
import matplotlib.pyplot as plt

def slit_params_init(dec_x, dec_y, defocus):
  
  H = np.array([0 + dec_x, 0 + dec_y, 0 + defocus])
  DCs = np.array([0, 0, 1])
  
  return H, DCs
  



def slit_shape_fibAB(alpha, beta, gama):
  img = np.zeros([1000,1000])
  fibre_core_diameter = 100 #in um
  fibre_mean_separation = 346.0 #in um
  width = len(img[0])

  fiber_separation = 0.346 #in mm, separation center to center

  #interpolation function: receives two points of the XY plane, and the number of points to be interpolated
  def interp(x0,y0,x1,y1,n):
    if x0 == x1 and y0 < y1:
      s = np.sqrt((x0 - x1)**2 + (y0 - y1)**2)
      s_prime = s/n
      theta = 90*np.pi/180
      dx = s_prime*np.cos(theta)
      dy = s_prime*np.sin(theta) 
    elif x0 < x1:
      m = (y0 - y1)/(x0 - x1)
      theta = np.arctan(m) 
      s = np.sqrt((x0 - x1)**2 + (y0 - y1)**2)
      s_prime = s/n
      dx = s_prime*np.cos(theta)
      dy = s_prime*np.sin(theta)
    elif x0 > x1:
      m = (y0 - y1)/(x0 - x1)
      theta = np.arctan(m) 
      s = np.sqrt((x0 - x1)**2 + (y0 - y1)**2)
      s_prime = s/n
      dx = -1*s_prime*np.cos(theta)
      dy = -1*s_prime*np.sin(theta)
    elif x0 == x1 and y0 > y1:
      s = np.sqrt((x0 - x1)**2 + (y0 - y1)**2)
      s_prime = s/n
      theta = -90*np.pi/180
      dx = s_prime*np.cos(theta)
      dy = s_prime*np.sin(theta) 
    
    xaux = x0
    yaux = y0
    x_out = []
    y_out = []
    for i in range(int(n)):
      x_out.append(xaux)
      y_out.append(yaux)
      xaux += dx
      yaux += dy
    
    return x_out, y_out


#Returns the coordinates of the polygon, as function of diameter, and number of points of the polygon on the XY plane
  def polygon(diameter,offset_x,offset_y,npoints):
    dtheta = 360.0/npoints
    radius = diameter/2.0
    theta = 0.0
    points = []
    oct_x = []
    oct_y = []
    for i in range(npoints+1):
      oct_x.append(float(radius*np.cos(theta*np.pi/180) + offset_x))
      oct_y.append(float(radius*np.sin(theta*np.pi/180) + offset_y))
      theta = theta + dtheta
  
    x_side = []
    y_side = []
    n = 10
    for i in range(len(oct_x)-1):
      x,y = interp(oct_x[i],oct_y[i],oct_x[i+1],oct_y[i+1],n)
      x_side.append(x)
      y_side.append(y)

    #print len(x_side) #number of sides
    #print len(x_side[0]) #number of points on each side
    x_final = []
    y_final = []
    for i in range(len(x_side)):
      for k in range(len(x_side[0])):
	x, y = interp(x_side[i][k],y_side[i][k],offset_x,offset_y,20)
	x_final.append(x)
	y_final.append(y)
  
    return x_final, y_final
  

  
  #rotation around Z axis 
  #, angle_X, angle_Y
  #Rotation function
  def rot(x,y,angle_X, angle_Y, angle_Z):
    x_new = []
    y_new = []
    z_new = []
    x_Z = []
    y_Z = []
    z_Z = []
    theta_0 = 0.0
    #rotation around Z
    for i in range(len(x)):
      for k in range(len(x[0])):
	x_prima = x[i][k]*np.cos(angle_Z) - y[i][k]*np.sin(angle_Z)
	y_prima = x[i][k]*np.sin(angle_Z) + y[i][k]*np.cos(angle_Z)
	z_prima = 0.0
	x_Z.append(x_prima)
	y_Z.append(y_prima)
	z_Z.append(z_prima)
  
    #print len(x_Z)
  
    x_X = []
    y_X = []
    z_X = []
   
    x_Y = []
    y_Y = []
    z_Y = []
  
    #rotation around X
    for i in range(len(x_Z)):
      x_prima = x_Z[i]
      y_prima = y_Z[i]*np.cos(angle_X) - z_Z[i]*np.sin(angle_X)
      z_prima = y_Z[i]*np.sin(angle_X) + z_Z[i]*np.cos(angle_X)
      x_Y.append(x_prima)
      y_Y.append(y_prima)
      z_Y.append(z_prima)
  
    #Rotation around Y
    for i in range(len(x_Y)):
      x_prima = x_Y[i]*np.cos(angle_Y) + z_Y[i]*np.sin(angle_Y)
      y_prima = y_Y[i]
      z_prima = -1*x_Y[i]*np.sin(angle_Y) + z_Y[i]*np.cos(angle_Y)
      x_new.append(x_prima)
      y_new.append(y_prima)
      z_new.append(z_prima)
  
    return x_new, y_new, z_new



  #we create an array with the coordinates of the octagon vertices

  #gamma = 0.0*np.pi/180 #Rotation around X
  #eta = 0.0*np.pi/180 #Rotation around Y
  #beta = 0.0*np.pi/180 #Rotation around Z
  x_oct_A, y_oct_A  = polygon(fibre_core_diameter,fibre_mean_separation/2,0,8) #fiber A
  x_oct_B, y_oct_B  = polygon(fibre_core_diameter,-1*fibre_mean_separation/2,0,8) #fiber B

  x_oct_rot_A, y_oct_rot_A, z_oct_rot_A = rot(x_oct_A,y_oct_A, alpha, beta, gama)
  x_oct_rot_B, y_oct_rot_B, z_oct_rot_B = rot(x_oct_B,y_oct_B, alpha, beta, gama)


  #print DCx, DCy, DCz
  return x_oct_rot_A, y_oct_rot_A, z_oct_rot_A, x_oct_rot_B, y_oct_rot_B, z_oct_rot_B
  
  
    
