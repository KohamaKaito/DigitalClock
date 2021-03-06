import numpy as np

def make_pixel(num):

    if num == 0:
        X = np.array([[255,0,0,0,255],
             [255,0,255,0,255],
             [255,0,255,0,255],
             [255,0,255,0,255],
             [255,0,0,0,255]])
    elif num == 1:
        X = np.array([[255,255,0,0,255],
             [255,255,255,0,255],
             [255,255,255,0,255],
             [255,255,255,0,255],
             [255,255,255,0,255]])
    elif num == 2:
        X = np.array([[255,0,0,0,255],
             [255,255,255,0,255],
             [255,0,0,0,255],
             [255,0,255,255,255],
             [255,0,0,0,255]])
    elif num == 3:
        X = np.array([[255,0,0,0,255],
             [255,255,255,0,255],
             [255,0,0,0,255],
             [255,255,255,0,255],
             [255,0,0,0,255]])
    elif num == 4:
        X = np.array([[255,0,255,0,255],
             [255,0,255,0,255],
             [255,0,0,0,255],
             [255,255,255,0,255],
             [255,255,255,0,255]])
    elif num == 5:
        X = np.array([[255,0,0,0,255],
             [255,0,255,255,255],
             [255,0,0,0,255],
             [255,255,255,0,255],
             [255,0,0,0,255]])
    elif num == 6:
        X = np.array([[255,0,0,0,255],
             [255,0,255,255,255],
             [255,0,0,0,255],
             [255,0,255,0,255],
             [255,0,0,0,255]])
    elif num == 7:
        X = np.array([[255,0,0,0,255],
             [255,0,255,0,255],
             [255,255,255,0,255],
             [255,255,255,0,255],
             [255,255,255,0,255]])
    elif num == 8:
        X = np.array([[255,0,0,0,255],
             [255,0,255,0,255],
             [255,0,0,0,255],
             [255,0,255,0,255],
             [255,0,0,0,255]])
    elif num == 9:
        X = np.array([[255,0,0,0,255],
             [255,0,255,0,255],
             [255,0,0,0,255],
             [255,255,255,0,255],
             [255,0,0,0,255]])
    
    else:
        X = np.array([[255],
             [0],
             [255],
             [0],
             [255]])
    
    return X
