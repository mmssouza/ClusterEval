#!/usr/bin/python

import sys
import scipy
import cPickle
import descritores
import numpy as np

diretorio = sys.argv[1]
bins = 150
range = (0.05,1.)
f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = descritores.cd(diretorio+im_file)
   tmp_h = np.histogram(tmp,bins = bins,range = range)[0]
   tmp_h = tmp_h.astype(float)/tmp_h.sum()
   db[im_file] = scipy.hstack((cl[im_file],tmp_h))
   if np.isnan(db[im_file]).any():
    print im_file,tmp_h
cPickle.dump(db,open(sys.argv[2],"wb"))
