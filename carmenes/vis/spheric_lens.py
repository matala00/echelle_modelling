import numpy as np
import transform
import refraction_index
import trace
#sag equation for a spheric surface

def dZ(H, DCs, r, flag):
  
    n = np.zeros(len(DCs))
    aux = H[2]
    H[2] = 0 
  
    #print "Coordinates at the paraxial plane of the surface:", H
    x_p = H[0]
    y_p = H[1]
    T_x = DCs[0]/DCs[2]
    T_y = DCs[1]/DCs[2]
  
    sign_r = r/np.abs(r)
    signDCz = DCs[2]/np.abs(DCs[2])
    
    
    #print 'Coords. at paraxial surface: ', H
    dz = ((x_p*T_x + y_p*T_y - r) + sign_r*np.sqrt(r**2 - (T_x*y_p - T_y*x_p)**2 - 2*r*(x_p*T_x + y_p*T_y) - (x_p**2 + y_p**2) ))/(T_x**2 + T_y**2 + 1)
    #print 'dz = ', dz
    #Coordinates at lens surface
    H[0] = H[0] + dz*T_x
    H[1] = H[1] + dz*T_y
    H[2] += signDCz*dz    
    #print 'Coords. at sphere surface: ', H
    #Normal vector at spherical surface  
    cen = np.asarray([0, 0, r])
    if np.sign(r) < 0:
        mod_n = np.sqrt((cen[0] - H[0])**2 + (cen[1] - H[1])**2 + (cen[2] - H[2])**2)
        n = (cen - H)/mod_n
    
    elif np.sign(r) > 0:
        
        mod_n = np.sqrt((cen[0] - H[0])**2 + (cen[1] - H[1])**2 + (cen[2] - H[2])**2)
        n = (H - cen)/mod_n
    
        
    #print 'Normal vector: ', n
    H[2] += aux
    #print 'General coords: ', H
    
    return H, n
  
def lens(H, DC, l0, r1, thickness, r2, f1, f2, material, Tin):
    
    n = np.zeros(len(DC))
    DC_out_sf1 = np.zeros(len(DC))
    DC_out_sf2 = np.zeros(len(DC))
    
    #Lens 1
    
    #Projection onto lens surface
    H, n = dZ(H, DC, r1, f1)
        
    #Refraction index
    n0 = 1.0 #coming from air
    SC_sf1_cam = refraction_index.SC(material)
    n1 = refraction_index.n(l0, SC_sf1_cam)
    
    signz=(DC[2]/np.abs(DC[2]))
    
    #Refraction at 1st surface
    cosi = np.dot(n, DC)
    sini = np.sqrt(1 - cosi**2)
    sinr = (n0/n1)*sini
    cosr = np.sqrt(1 - sinr**2)
        
    
    for i in range(len(DC)-1):
      DC_out_sf1[i] = (n0/n1)*DC[i] + (cosr - (n0/n1)*cosi)*n[i]
    
    DC_out_sf1[2] = signz*np.sqrt(1 - DC_out_sf1[0]**2 - DC_out_sf1[1]**2)
      
    #End refraction at 1st surface
    
    #Baffle between sf1 and sf2
   
    H = trace.to_next_surface3(H, DC_out_sf1, thickness)

    #Surface 2     
    H, nout = dZ(H, DC,r2,f2)
    
    
    n1 = refraction_index.n(l0, SC_sf1_cam) #coming from glass
    n2 = 1.0
    
    signz=(DC_out_sf1[2]/np.abs(DC_out_sf1[2]))
    
    cosi12 = np.dot(nout, DC_out_sf1)
    sini12 = np.sqrt(1 - cosi12**2)
    sinr12 = (n1/n2)*sini12
    cosr12 = np.sqrt(1 - sinr12**2)
        
    for i in range(len(DC)-1):
      DC_out_sf2[i] = (n1/n2)*DC_out_sf1[i] + (cosr12 - (n1/n2)*cosi12)*nout[i]
    
    DC_out_sf2[2] = signz*np.sqrt(1 - DC_out_sf2[0]**2 - DC_out_sf2[1]**2)
    
    return H, DC_out_sf2
    
    