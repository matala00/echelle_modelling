import numpy as np
  
#sag equation for a parabolic mirror

def DCcoll(H, DCs, r):
  
  n = np.zeros(len(DCs))
  DC_out = np.zeros(len(DCs))
  angle = 0.0
  
  old_z_coor = H[2]
  H[2] = 0 
  
  #print "Coordinates at the paraxial plane of the collimator:", H
  x_p = H[0]
  y_p = H[1]
  T_x = DCs[0]/DCs[2]
  T_y = DCs[1]/DCs[2]
  
  dz = (x_p*T_x + y_p*T_y + r + np.sqrt(r**2 + 2*r*y_p*T_y + 2*r*x_p*T_x - (T_x*y_p - T_y*x_p)**2))/(T_x**2 + T_y**2)
    
  #Coordinates at collimator surface
  H[0] = H[0] + dz*T_x
  H[1] = H[1] + dz*T_y
  H[2] = old_z_coor + dz
     
  #Normal vector at collimator surface  
  n[0] = H[0]/np.sqrt(H[0]**2 + H[1]**2 + r**2)
  n[1] = H[1]/np.sqrt(H[0]**2 + H[1]**2 + r**2)  
  n[2] = -r/np.sqrt(H[0]**2 + H[1]**2 + r**2)
      
  for i in range(len(DCs)):
      angle += n[i]*DCs[i]
    
  for i in range(len(DCs)):
      DC_out[i] = DCs[i] - 2*angle*n[i]
          
  return H, DC_out