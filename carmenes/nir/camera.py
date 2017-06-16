import trace
import spheric_lens
import numpy as np
import transform 

def tracing(H, DC, Tin,l0):
    
    H_out = np.zeros(len(DC))
    DC_out = np.zeros(len(DC))
    x = []
    y = []
    z = []    
       
    
    dec_x = -8.61016372 
    dec_y = 238.81337731
    defocus = 0.0
    
    aux = H[2]
    
    H[0] = H[0] + dec_x
    H[1] = H[1] + dec_y
    H[2] = 0. + defocus
    
    x.append(H[2] + aux)
    y.append(H[1] - dec_y)
    z.append(H[0] - dec_x)
       
    H = transform.transform(H, Tin)
    DC = transform.transform(DC, Tin)
    
    H[2] = 0.0 #Paraxial plane of the first lens surface
    
        
    #Lens 1
    #print 'Wavelength: ', l0
    
    l1_r1 = -294.7609 #in mm
    l1_f1 = int(np.sign(l1_r1))
    l1_thickness = -26 #in mm
    l1_r2 = 12565.11
    l1_f2 = int(np.sign(l1_r2))
    
    z_l1_sf0 = 0. #position surface 0
    z_l1_sf1 = z_l1_sf0 + l1_thickness    #Position surface 1
    H_out, DC_out = spheric_lens.lens(H, DC, l0, l1_r1, z_l1_sf1, l1_r2,l1_f1, l1_f2, 'SFPL51', Tin)
    

    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    
    #Gap lens 1, lens 2
    d_l1l2 = -54.40822
    z_l2_sf0 = z_l1_sf1 + d_l1l2
    
    H_out = trace.to_next_surface3(H_out, DC_out, z_l2_sf0)
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    
    #Lens 2
    #print 'Lens 2\n'
    
    l2_r1 = -566.8996
    l2_f1 = int(np.sign(l2_r1))
    l2_thickness = -15
    l2_r2 = -146.4353
    l2_f2 = int(np.sign(l2_r2))
    
    z_l2_sf1 = z_l2_sf0 + l2_thickness    #Position surface 1
    H_out, DC_out = spheric_lens.lens(H_out, DC_out, l0, l2_r1, z_l2_sf1, l2_r2, l2_f1, l2_f2, 'SBAM4', Tin)
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    
    #gap lens 2, lens3
    d_l2l3 = -1
    z_l3_sf0 = z_l2_sf1 + d_l2l3
    H_out = trace.to_next_surface3(H_out, DC_out, z_l3_sf0)
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    
    
    #tracing lens 3
    #print 'Lens 3\n'
    l3_r1 = -146.562
    l3_f1 = int(np.sign(l3_r1))
    l3_thickness = -36.0
    l3_r2 = -2087.281
    l3_f2 = int(np.sign(l3_r2))
    
    z_l3_sf1 = z_l3_sf0 + l3_thickness
    H_out, DC_out = spheric_lens.lens(H_out, DC_out, l0, l3_r1, z_l3_sf1, l3_r2, l3_f1, l3_f2, 'SFPL53', Tin)
        
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    
    
    #gap lens3, lens4
    d_l3l4 = -17.342
    z_l4_sf0 = z_l3_sf1 + d_l3l4
    H_out = trace.to_next_surface3(H_out, DC_out, z_l4_sf0)
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    
    #Lens 4
    #print 'Lens 4\n'
    l4_r1 = 471.502
    l4_f1 = int(np.sign(l4_r1))
    l4_thickness = -15.0
    l4_r2 = 1032.687
    l4_f2 = int(np.sign(l4_r2))
    
    z_l4_sf1 = z_l4_sf0 + l4_thickness
    H_out, DC_out = spheric_lens.lens(H_out, DC_out, l0, l4_r1, z_l4_sf1, l4_r2, l4_f1, l4_f2, 'SBSL7', Tin)
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    #gap lens 4, lens 5
    d_l4l5 = -326.160
    z_l5_sf0 = z_l4_sf1 + d_l4l5
    H_out = trace.to_next_surface(H_out, DC_out, z_l5_sf0)
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    
    #lens 5
    #print 'Lens 5\n'
    l5_r1 = -246.217
    l5_f1 = int(np.sign(l5_r1))
    l5_thickness = -26.0
    l5_r2 = 1325.910
    l5_f2 = int(np.sign(l5_r2))
    
    z_l5_sf1 = z_l5_sf0 + l5_thickness
    H_out, DC_out = spheric_lens.lens(H_out, DC_out, l0, l5_r1, z_l5_sf1, l5_r2, l5_f1, l5_f2, 'SBAM4', Tin)
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
        
    #gap lens5, lens 6
    d_l5l6 = -157.852
    z_l6_sf0 = z_l5_sf1 + d_l5l6
    H_out = trace.to_next_surface(H_out, DC_out, z_l6_sf0)    
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    
    
    #lens 6
    l6_r1 = 215.365
    l6_f1 = int(np.sign(l6_r1))
    l6_thickness = -8.0
    l6_r2 = 1e3
    l6_f2 = int(np.sign(l6_r2))
    z_l6_sf1 = z_l6_sf0 + l6_thickness
    
    H_out, DC_out = spheric_lens.lens(H_out, DC_out, l0, l6_r1, z_l6_sf1, l6_r2, l6_f1, l6_f2, 'SLAL10', Tin)
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    
    
    l7_r1 = 1e10
    l7_f1 = int(np.sign(l7_r1))
    l7_thickness = -10.0
    l7_r2 = 544.665
    l7_f2 = int(np.sign(l7_r2))
    z_l7_sf1 = z_l6_sf1 + l7_thickness
    
    H_out, DC_out = spheric_lens.lens(H_out, DC_out, l0, l7_r1, z_l7_sf1, l7_r2, l7_f1, l7_f2, 'SK1300', Tin) #Toroidal surface
    
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
        
    
    #distance to detector
    
    d_l7_ccd = -5
    z_ccd = z_l7_sf1 + d_l7_ccd
    H_out = trace.to_next_surface(H_out, DC_out, z_ccd)
    
    H_out = transform.transform(H_out, -Tin)
    '''
    H_out2 = transform.transform(H_out, -Tin)
    x.append(H_out2[2] + aux)
    y.append(H_out2[1] - dec_y)
    z.append(H_out2[0] - dec_x)
    '''
    
    return H_out, DC_out, x,y,z
    #return H_out, DC_out, x, y, z
    