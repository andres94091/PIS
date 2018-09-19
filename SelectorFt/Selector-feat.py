# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:59:26 2018

@author: andre
"""

import pandas as pd

from sklearn.feature_selection import VarianceThreshold;
iris = pd.read_csv('iris.csv', header=None )
irisfeat , irisclass = iris, iris.pop(4)

#%%

sel = VarianceThreshold(0.5)
featsVars=sel.fit_transform (irisfeat)

#%%

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

featsKb = SelectKBest(chi2, k=2).fit_transform(irisfeat,irisclass)

#%% recursive featuring elimination 
# http://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html#sphx-glr-auto-examples-feature-selection-plot-rfe-digits-py
# no lo entendi

#%%

from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel

lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(irisfeat, irisclass)
model = SelectFromModel(lsvc, prefit = True)
featsL1 = model.transform(irisfeat)

#%%

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

clf = ExtraTreesClassifier().fit(irisfeat, irisclass)
clf.feature_importances_  

model = SelectFromModel(clf, prefit=True)
featsTree = model.transform (irisfeat)




