import numpy as np

def init():
    
    file = open('echelle_orders.txt','w')
    file_0 = open('echelle_blaze_wave.txt','w')
    wav_N = 3 #1575

    wav_lo = 0.95 #in microns
    wav_hi = 1.70

    R = 3.78
    blaze_angle = 75.2*np.pi/180
    G = 31.6*1e-3 #lines per um
    d = 1/G
    #n*lambda = d(sin in + sin out)

    ord_blu = int(2*np.sin(blaze_angle)/(G*wav_lo))
    ord_red = int(2*np.sin(blaze_angle)/(G*wav_hi))

    print 'Reddest order:', ord_red
    print 'Bluest order:', ord_blu
    
    spectrum = []
    order = []
    wave = []
    Hs = []
    DCs = []
    while ord_red < ord_blu + 1:
        
        
        wav_blz = 2*np.sin(blaze_angle)/(G*ord_red)
        wav_min = wav_blz - wav_blz/(2*ord_red)
        wav_max = wav_blz + wav_blz/(2*ord_red)
        dwav = (wav_max - wav_min)/wav_N
        file.write('%d ' %(ord_red))
        #file_0.write('%d %f %f %f\n' %(ord_red, wav_min ,wav_blz, wav_max))
        file_0.write('%d %f\n' %(ord_red, wav_blz))
        k = 0

        while k <= wav_N:
            
            H = np.zeros([3])
            DC = np.zeros([3])
            
            
            order.append(ord_red)
            wave.append(wav_min)
            Hs.append(H)
            DCs.append(DC)
            
            
            single_element = [ord_red, wav_min, H, DC]
            #print single_element, '\n'
            spectrum.append(single_element)
            file.write('%f ' %(wav_min))
            wav_min += dwav
            k += 1
        file.write('\n')
        ord_red += 1
    
    file.close()
    file_0.close()
    return order, wave, Hs, DCs
    

    
