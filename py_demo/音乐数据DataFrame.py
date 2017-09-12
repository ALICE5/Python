# -*- coding:utf-8 -*-
import pandas as pd
music_data = [("the rolling stones","Satisfaction"),
              ("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),
              ("Metallica","Nothing Else Matters")]

music_table = pd.DataFrame(music_data)
music_table.index = range(1,5)
music_table.columns = ['singer','song_name']

print(music_table)

#

import time
import math
import numpy as np

x = np.arange(0,100,0.01)
t1_start = time.clock()
for i,t in enumerate(x):
    x[i] = math.sqrt(t)
t1_end = time.clock()

y = np.arange(0,100,0.01)
t2_start = time.clock()
y = np.sqrt(y)
t2_end = time.clock()

print('Running time of math:',t1_end-t1_start)
print('Running time of numpy:',t2_end-t2_start)