
def mmtopix(x,y,dec_x, dec_y):
    
    pix_size = 15*1e-3 #in mm
    x_out = []
    y_out = []
    for i in range(len(x)):
        x_out.append(float(x[i])/pix_size + dec_x)
        y_out.append(float(y[i])/pix_size + dec_y)
    return x_out, y_out
    