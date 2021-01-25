import numpy as np
from . import module_time as mt     # 現在の時刻を取得するモジュール
from . import module_img as m_img   # 行列の描画を行うためのモジュール
from . import module_pixel as mp    # 数字のピクセル画像を作成するモジュール


# 現在の時刻から４つの数字を取得する　
# 例) 7:15　→ 0,7,1,5
one,two,three,four = mt.get_time()

# 5×21　行列を生成．
time = np.full((5,21),255,np.uint8)

# 数値を引数にピクセル数字の行列を取得 → 代入
time[:,0:5] = mp.make_pixel(one)
time[:,5:10] = mp.make_pixel(two)
time[:,10:11] = mp.make_pixel('a')
time[:,11:16] = mp.make_pixel(three)
time[:,16:21] = mp.make_pixel(four)

m_img.plot_img(time)
