import matplotlib.pyplot as plt
import nir_spectrometer
import time
import numpy as np

if __name__ == "__main__":
    
    
    m0 = 64
    l00 = 0.948645
    l01 = 0.958605
    l02 = 0.963585 
    
    m1 = 55    
    l10 = 1.102456
    l11 = 1.115941
    l12 = 1.122684 
    
    m2 = 36
    l20 = 1.676152
    l21 = 1.691891
    l22 = 1.723368
    
    #H0, DC0 = spectrometer.tracing(m1, l1)
    x10, y10, z10, H10, DC10 = nir_spectrometer.tracing(m1,l10)
    x11, y11, z11, H11, DC11 = nir_spectrometer.tracing(m1,l11)
    x12, y12, z12, H12, DC12 = nir_spectrometer.tracing(m1,l12)
    
    x00, y00, z00, H00, DC00 = nir_spectrometer.tracing(m0,l00)
    x01, y01, z01, H01, DC01 = nir_spectrometer.tracing(m0,l01)
    x02, y02, z02, H02, DC02 = nir_spectrometer.tracing(m0,l02)
    
    x20, y20, z20, H20, DC20 = nir_spectrometer.tracing(m2,l20)
    x21, y21, z21, H21, DC21 = nir_spectrometer.tracing(m2,l21)
    x22, y22, z22, H22, DC22 = nir_spectrometer.tracing(m2,l22)
    
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
    plt.axis('equal')
    plt.show()
    
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
    #plt.xlim(-400.5, 0)
    #plt.ylim(-45, 45)
    plt.axis('equal')
    plt.show()
    