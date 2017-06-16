import refraction_index
import numpy as np
import transform
import trace

#Grism NIR
#Material: glass Infrasil
#Apex angle: 13.85 deg, 81 grooves/mm

#Grism Optical
#Material: LF5
#Apex angle: 223 l/mm, 17.8
#input angle = -11.8
#used in order no. 1

def dispersion(H,DC, Tin, l0, SC, Tout, GD):
                                                                   
    n = np.zeros(len(DC))
    H_out = np.zeros(len(H))
    DC_out = np.zeros(len(DC))
    DC_out_gp = np.zeros(len(DC))
    
    #surface default normal
    n = np.asarray([0,0,-1])
    H = transform.transform(H, Tin)
    DC = transform.transform(DC, Tin)
    
    #Refraction index
    n0 = 1.0 #coming from air
    n1 = refraction_index.n(l0, SC) 
    n2 = 1.0 #output in air
    
    signz=(DC[2]/np.abs(DC[2]))
    cosi = np.dot(DC, n)
    sini = np.sqrt(1 - cosi**2)
    sinr = (n0/n1)*sini
    cosr = np.sqrt(1 - sinr**2)
        
    for i in range(len(DC)-1):
      DC_out[i] = (n0/n1)*DC[i] + (cosr - (n0/n1)*cosi)*n[i]
      
    DC_out[2] = signz*np.sqrt(1 - DC_out[0]**2 - DC_out[1]**2)
    DC_out = transform.transform(DC_out, -Tin)
    H = transform.transform(H, -Tin)
    #End refraction at 1st surface
        
    #We trace to the grating surface
    d_in_out = -40.0 #in mm
    H_out = trace.to_next_surface2(H, DC_out, d_in_out)
    
    #We transform to the grating plane
    H_out = transform.transform(H_out, Tout)
    DC_grating_in = transform.transform(DC_out, Tout)
    n_gr = np.asarray([0,0,-1])
    
    cosi0 = np.dot(n_gr, DC_grating_in)    
    sini0 = np.sqrt(1 - cosi0**2)
    sinr0 = (n1/n2)*sini0
    cosr0 = np.sqrt(1 - sinr0**2)
            
    if (DC_grating_in[1]==0):
        signx=1
        
    else:
        signx=(DC_grating_in[1]/np.abs(DC_grating_in[1]))
    
    signz=(DC_grating_in[2]/np.abs(DC_grating_in[2]))
    
    #Snell's law and diffraction in output grating surface
    DC_out_gp[0] = (n1/n2)*DC_grating_in[0] + (cosr0 - (n1/n2)*cosi0)*n_gr[0]
    DC_out_gp[1] = (n1/n2)*DC_grating_in[1] + (cosr0 - (n1/n2)*cosi0)*n_gr[1] + (GD[0]*l0*GD[1] - DC_grating_in[1])
    DC_out_gp[2] = signz*np.sqrt(1 - DC_out_gp[0]**2 - DC_out_gp[1]**2)
          
    DC_out_final = transform.transform(DC_out_gp, -Tout)
    H_out = transform.transform(H_out, -Tout)
    
    
    return H_out, DC_out_final
