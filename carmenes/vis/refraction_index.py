import numpy as np

def n(l0, SC):
    #SC: Sellmeier coefficients
    #dn = 0.68
    dn = 0.0
    n = np.sqrt(1 + SC[0]*l0**2/(l0**2 - SC[3]) + SC[1]*l0**2/(l0**2 - SC[4]) + SC[2]*l0**2/(l0**2 - SC[5]))
    return n+dn
    

def SC(material):
    file = open('materials.txt','r')
    file.readline()
    for line in file:
        
        SCs = line.split()
        
        if str(material) == str(SCs[0]):
            
            SC_out = np.asarray([float(SCs[1]), float(SCs[2]), float(SCs[3]), float(SCs[4]), float(SCs[5]), float(SCs[6])])
            file.close()
            return SC_out
        
        
#x_CO2 in umol/mol
# t in Celsius, p in pascal
#f_tp no clue about what is it.
def n_air(wav_vac, x_CO2, t, p, RH, f_tp):    
    w0 = 295.235
    w1 = 2.6422
    w2 = -0.03238
    w3 = 0.004028
    
    k0 = 238.0185
    k1 = 5792105
    k2 = 57.362
    k2 = 167917.0
    
    a0 = 1.58123e-6
    a1 = -2.9331e-8
    a2 = 1.1043e-10
    
    b0 = 5.707e-6
    b1 = -2.051e-8
    
    c0 = 1.9898e-4
    c1 = -2.376e-6
    
    d = 1.83e-11
    e = -0.765e-8
    
    p_R1 = 101325.0
    T_R1 = 288.15
    Z_a = 0.9995922115
    rho_vs = 0.00985938
    R = 8.314472
    M_v = 0.018015
    
    K1 = 1.16705214528e3
    K2 = -7.24213167032e5
    K3 = -1.70738469401e1
    K4 = 1.20208247025e4
    K5 = -3.23255503223e6
    K6 = 1.49151086135e1
    K7 = -4.82326573616e3
    K8 = 4.05113405421e5
    K9 = -2.38555575678e-1
    K10 = 6.50175348448e2    
    
    S = 1/(lamda_vac**2)
    
    r_as = 1e-8*( k1/(k0 - S) + k3/(k2 - S) )
    r_vs = 1.022e-8*(w0 + w1*S + w2*S**2 + w3*S**3)
    
    M_a = 0.0289635 + 1.2011e-8*(x_CO2 - 450)
    r_axs = r_as*(1 + 5.34e-7*(x_CO2 - 450))
    T = t + 273.15 #Temperature in K
    Z_m = 1 - (p/T)*(a0 + a1*t + a2*t**2 + (b0 + b1*t)*chi_v**2) + (p/T)**2*(d + e*chi_v**2)

    Sigma = T + K9/(T - K10)
    A = Sigma**2 + K1*Sigma + K2
    B = K3*Sigma**2 + K4*Sigma + K5
    C = K6*Sigma**2 + K7*Sigma + K8
    X = -B + np.sqrt(B**2 - 4*A*C)
    
    p_sv =1e6*(2*C/X)**2
    chi_v = (RH/100)*f_pt*p_sv/p
    
    rho_axs = p_R1*M_a/(Z_a*R*T_R1)
    rho_v = chi_v*p*M_v/(Z_m*R*T)
    rho_a = (1 - chi_v)*p*M_a/(Z_m*R*T)
    
    n_air = 1 + (rho_a/rho_axs)*r_axs + (rho_v/rho_vs)*r_vs
    
    wav_air = n_air*wav_vac
    return n_air, wav_air