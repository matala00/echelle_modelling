import refraction_index
import grism
import numpy as np
import transform
import collimator
import echelle
import slit
import trace
import flat_mirror
import camera

def tracing(m, l0):
    
    x = []
    y = []
    z = []
 
    
    #Slit
    dec_x = 0.
    dec_y = 0.
    defocus = 0.
    
    H0, DC0 = slit.slit_params_init(dec_x, dec_y, defocus) #Output Position and initial orientation
    T_slit = np.asarray([-8.5*np.pi/180,0.0,-9.01*np.pi/180])
    H1 = transform.transform(H0, T_slit)
    DC1 = transform.transform(DC0, T_slit)
    
    x.append(H1[2])
    y.append(H1[1])
    z.append(H1[0])
  
    #Collimator
    z_pos_col = 1590.
    d_slit_col = np.abs(z_pos_col - H1[2])
    H2 = trace.to_next_surface(H1, DC1, d_slit_col)
    
    curvature_rad = -1590.*2
    H2, DC2 = collimator.DCcoll(H2, DC1, curvature_rad)
    
    x.append(H2[2])
    y.append(H2[1])
    z.append(H2[0])
  
    
    #Echelle
    z_pos_ech = 0.
    H3 = trace.to_next_surface(H2, DC2, z_pos_ech)
    
    x.append(H3[2])
    y.append(H3[1])
    z.append(H3[0])
    
    #Echelle    
    #Data
    dG = 0.
    G = (31.6 + dG)*1e-3 #lines per um
    d = 1/G
  
    #Orientation
    T_echelle = np.asarray([-1.2*np.pi/180, -75.58*np.pi/180,0.0])
    H3, DC3 = echelle.diffraction(H3, DC2, T_echelle, m, l0, d)
    
    #Collimator 2nd pass
    d_ech_col = z_pos_col
    H4 = trace.to_next_surface(H3, DC3, d_ech_col)
    H4, DC4 = collimator.DCcoll(H4, DC3, curvature_rad)
    
    x.append(H4[2])
    y.append(H4[1])
    z.append(H4[0])
    
    #Transfer mirror
    
    #Position
    z_pos_tm = 0.
    d_col2_tm = z_pos_tm - H4[2]    
    H5 = trace.to_transfer_mirror(H4, DC4, d_col2_tm, z_pos_tm)
        
    #Orientation
    T_flat = np.asarray([0.*np.pi/180, 0.0*np.pi/180, 0.0*np.pi/180])
       
    H5 = transform.transform(H5, T_flat)
    DC5 = flat_mirror.flat_out(DC4, T_flat)
    H5 = transform.transform(H5, -T_flat)
    
    x.append(H5[2])
    y.append(H5[1])
    z.append(H5[0])         
    
    #Collimator 3rd pass
  
    d_slit_col = np.abs(z_pos_col - H1[2])
    H6 = trace.to_next_surface(H5, DC5, d_slit_col)
    H6, DC6 = collimator.DCcoll(H6, DC5, curvature_rad)
    
    x.append(H6[2])
    y.append(H6[1])
    z.append(H6[0])
  
    #Grism
    
    #position
    z_pos_grism = 0.
    dcoll3_cross = z_pos_grism - H6[2]
    H7 = trace.to_grism(H6, DC6, dcoll3_cross, z_pos_grism)
    
    x.append(H7[2])
    y.append(H7[1])
    z.append(H7[0])
    
    #orientation
    apex = 17.8 #deg 17.8
    T_grism_in = np.asarray([-2.4*np.pi/180, 0.0*np.pi/180, 0.0*np.pi/180])
    T_grism_out = np.asarray([T_grism_in[0]-apex*np.pi/180, T_grism_in[1]*np.pi/180, T_grism_in[2]*np.pi/180])
        
    #Material and grating data
    SC_grism = refraction_index.SC('LF5')   #We load grims material Sellmeier coefficients
    dGG = 0.0 #-0.018
    GD = np.asarray([1,  (-223.0 + dGG)*1e-3])
    
    #Grism dispersion
    H7, DC7 = grism.dispersion(H7, DC6, T_grism_in, l0, SC_grism, T_grism_out, GD)
    
    x.append(H7[2])
    y.append(H7[1])
    z.append(H7[0])
    #End Grism
        
    #Camera
    #Position
    d_gr_cam = -49.992
    H8 = trace.to_next_surface2(H7, DC7, d_gr_cam)
    x.append(H8[2])
    y.append(H8[1])
    z.append(H8[0])
    
    #Orientation
    dalpha_cam = 0.
    dbeta_cam = 0.
    dgamma_cam = 0.
    #T_cam = np.asarray([(0.0 + dalpha_cam)*np.pi/180, (0.0+dbeta_cam)*np.pi/180, (0.0+dgamma_cam)*np.pi/180])
    T_cam = np.asarray([(1.635 + dalpha_cam)*np.pi/180, (0.0+dbeta_cam)*np.pi/180, (0.0+dgamma_cam)*np.pi/180])
    
    H8, DC8, x1, y1, z1 = camera.tracing(H8, DC7, T_cam,l0)
    
    
    
    for i in range(len(x1)):
      x.append(x1[i])
      y.append(y1[i])
      z.append(z1[i])
    
    
    
    return m, l0, H8[0], H8[1], H8[2], DC8[0], DC8[1], DC8[2]

    #return x,y,z,H8, DC8