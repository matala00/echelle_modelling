import transform
import numpy as np
#[X, Y, Z]: [Echelle dispersion direction, cross-dispersion direction, optical axis direction]


def diffraction(H, DC, T, m, l, d):
    
    DC_out = np.zeros(len(DC))
    DC_out_final = np.zeros(len(DC))
    Hout = np.zeros(len(H))
    
    H = transform.transform(H, T)
    DC= transform.transform(DC, T) 
    
    if (DC[0]==0):
        signy=1
        
    else:
        signy=(DC[0]/np.abs(DC[0]))
                
    signz=(DC[2]/np.abs(DC[2]))
    
    
    DC_out[1] = DC[1]
    DC_out[0] = signy*(m*l/d - DC[0])
    DC_out[2] = signz*(np.sqrt( 1 - DC_out[0]**2 - DC_out[1]**2))
    
    DC_out_final = transform.transform(DC_out, -T)
    DC_out_final[2] = - DC_out_final[2]
    
    Hout = transform.transform(H, -T)
    
    return Hout, DC_out_final
    