import numpy as np
import transform

def flat_out(DC, T):
    
    n = np.zeros(len(DC))
    DC_out = np.zeros(len(DC))
    angle = 0.0
  
    #mirror default normal
    n0 = np.asarray([0,0,1])
    n = transform.transform(n0, T)
        
    for i in range(len(DC)):
      angle += n[i]*DC[i]
      
    for i in range(len(DC)):
      DC_out[i] = DC[i] - 2*angle*n[i]
  
    return DC_out
  