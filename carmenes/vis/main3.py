import matplotlib.pyplot as plt
import vis_spectrometer
import time
import numpy as np

if __name__ == "__main__":
    
    
    m0 = 111
    l00 = 0.54879
    l01 = 0.551
    l02 = 0.554
    m1 = 59
    l10 = 1.028352
    l11 = 1.038899
    l12 = 1.045931
    m2 = 77
    l20 = 0.790
    l21 = 0.795
    l22 = 0.800
    
    #H0, DC0 = spectrometer.tracing(m1, l1)
    x10, y10, z10, H10, DC10 = vis_spectrometer.tracing(m1,l10)
    x11, y11, z11, H11, DC11 = vis_spectrometer.tracing(m1,l11)
    x12, y12, z12, H12, DC12 = vis_spectrometer.tracing(m1,l12)
    
    x00, y00, z00, H00, DC00 = vis_spectrometer.tracing(m0,l00)
    x01, y01, z01, H01, DC01 = vis_spectrometer.tracing(m0,l01)
    x02, y02, z02, H02, DC02 = vis_spectrometer.tracing(m0,l02)
    
    x20, y20, z20, H20, DC20 = vis_spectrometer.tracing(m2,l20)
    x21, y21, z21, H21, DC21 = vis_spectrometer.tracing(m2,l21)
    x22, y22, z22, H22, DC22 = vis_spectrometer.tracing(m2,l22)
    
    '''
    plt.plot(x10,z10,'.-')
    plt.plot(x11,z11,'.-')
    plt.plot(x12,z12,'.-')

    plt.plot(x00,z00,'.-')
    plt.plot(x01,z01,'.-')
    plt.plot(x02,z02,'.-')

    plt.plot(x20,z20,'.-')
    plt.plot(x21,z21,'.-')
    plt.plot(x22,z22,'.-')

    
    plt.xlabel('z')
    plt.ylabel('x')
    #plt.xlim(-180.5, 0)
    #plt.ylim(-45, 45)
    
    plt.axis('equal')
    plt.show()
    '''
    
    plt.plot(x10,y10,'.-')
    plt.plot(x11,y11,'.-')
    plt.plot(x12,y12,'.-')
    
    plt.plot(x00,y00,'.-')
    plt.plot(x01,y01,'.-')
    plt.plot(x02,y02,'.-')
    
    plt.plot(x20,y20,'.-')
    plt.plot(x21,y21,'.-')
    plt.plot(x22,y22,'.-')
    
    plt.xlabel('z')
    plt.ylabel('y')
    #plt.xlim(-400.5, 0)
    #plt.ylim(-45, 45)
    #plt.xlim(-800.5, 0)
    #plt.ylim(-400, -100)
    
    #plt.axis('equal')
    plt.show()
    '''
    plt.plot(z10,y10,'.-')
    plt.plot(z11,y11,'.-')
    plt.plot(z12,y12,'.-')
    
    plt.plot(z00,y00,'.-')
    plt.plot(z01,y01,'.-')
    plt.plot(z02,y02,'.-')
    
    plt.plot(z20,y20,'.-')
    plt.plot(z21,y21,'.-')
    plt.plot(z22,y22,'.-')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    '''
    plt.show()
    