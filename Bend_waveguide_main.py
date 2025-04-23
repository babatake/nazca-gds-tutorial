# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:52:30 2019

@author: Takeshi
"""

import nazca as nd
import layers
from Bend_waveguide_functions1 import bend_waveguide1

layers
# 使用するパラメータの定義
Width_taper1 = 0.48       # テーパー開始幅
Width_taper2 = 0.48       # テーパー終了幅（ストレートやベンドの幅にも使う）
L_taper = 1             # テーパーの長さ
L1 = 1                  # 最初のストレート長
L2 = 1                  # 最後のストレート長
xp = 0                    # 配置X座標
yp = 0                    # 配置Y座標
Radii = 2                # ベンドの半径

# 関数の呼び出し
cell=bend_waveguide1(
    Width_taper1=Width_taper1,
    Width_taper2=Width_taper2,
    L_taper=L_taper,
    L1=L1,
    L2=L2,
    xp=xp,
    yp=yp,
    Radii=Radii
)

cell.put(0, 0)  # ✅ここでセルをGDSに配置する！

# GDSファイルへのエクスポート
nd.export_gds(filename='Bend_waveguide1.gds')
