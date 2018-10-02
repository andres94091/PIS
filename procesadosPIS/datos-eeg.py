# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:16:44 2018

@author: Usuario
"""

import scipy.io as io

dat = io.loadmat("Sujeto1Registro1_notch_ReposoDiferencia_asimetric_qeeg_channels.mat")

feat=['coheA1','coheA2','coheB','coheD','coheT']
A=[];

for i in feat:
    A.append(dat[i][0,1])