import numpy as np

def to_next_surface(H, DC, d):
    
    Hout = np.zeros(len(H))
        
    #coordinates in the next surface paraxial plane
        
    Hout[0] = (H[0]+((DC[0]/DC[2])*d))   
    Hout[1] = (H[1]+((DC[1]/DC[2])*d))
    Hout[2] = d
    
    return Hout

def to_transfer_mirror(H, DC, d, z):
    
    Hout = np.zeros(len(H))
        
    #coordinates in the next surface paraxial plane
        
    Hout[0] = (H[0]+((DC[0]/DC[2])*d))   
    Hout[1] = (H[1]+((DC[1]/DC[2])*d))
    Hout[2] = z
    
    return Hout

def to_grism(H, DC, d, z):
    
    Hout = np.zeros(len(H))
        
    #coordinates in the next surface paraxial plane
        
    Hout[0] = (H[0]+((DC[0]/DC[2])*d))   
    Hout[1] = (H[1]+((DC[1]/DC[2])*d))
    Hout[2] = z
    
    return Hout

def to_next_surface2(H0, DC0, d):
    H_out = np.zeros(len(H0))
        
    #coordinates in the next surface paraxial plane
    H0[2] = H0[2] + d
    H_out[2] = H0[2]
    H_out[0] = (H0[0]+((DC0[0]/DC0[2])*H0[2]))        
    H_out[1] = (H0[1]+((DC0[1]/DC0[2])*H0[2]))
    return H_out

def to_next_surface3(H0, DC0, z_pos_sf):
    
    H_out = np.zeros(len(H0))
    
    aux = H0[2]
    delta_z = z_pos_sf - H0[2]
    H0[2] = delta_z
    H_out[0] = (H0[0]+((DC0[0]/DC0[2])*H0[2]))        
    H_out[1] = (H0[1]+((DC0[1]/DC0[2])*H0[2]))
    H_out[2] = z_pos_sf
         
    return H_out

    