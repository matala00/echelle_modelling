import echelle_orders
import vis_spectrometer
import numpy as np
import time
if __name__ == "__main__":
    
    order, wave, Htest, DCtest = echelle_orders.init()
    
        
    t0 = time.time()
    spectrum = map(vis_spectrometer.tracing, order, wave)
    t1 = time.time()
    
    file = open('echelle_orders_main.txt','w')
    for i in range(len(spectrum)):
        file.write(str(spectrum[i])+'\n')
    file.close()
        
    t2 = time.time()
    print('time for spectrum tracing = {}'.format((t1-t0)))
    print('time for file writing = {}'.format((t2-t1)))
    
    
    
    
    

    
    
    