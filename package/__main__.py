import numpy as np
import datetime
import math
from . import module_img as m_img
from . import module_pixel as mp
from . import module_time as mt

one,two,three,four = mt.get_time()

time = np.full((5,21),255,np.uint8)

time[:,0:5] = mp.make_pixel(one)
time[:,5:10] = mp.make_pixel(two)
time[:,10:11] = mp.make_pixel('a')
time[:,11:16] = mp.make_pixel(three)
time[:,16:21] = mp.make_pixel(four)

m_img.plot_img(time)




