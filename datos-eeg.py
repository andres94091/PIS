# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:16:44 2018

@author: Usuario
"""

import scipy.io as io
from os import listdir

feat=['coheA1','coheA2','coheB','coheD','coheT']
path=listdir(path='procesadosPIS')
f=open('datos.csv','w')

for i in path:
    print(i)
    dat = io.loadmat('procesadosPIS/'+i)
    A=[];
    for j in feat:
        f.write(str(dat[j][0,1])+',')
    f.write(i.split('_')[2]+'_'+i.split('_')[3]+'\n')
    
f.close()