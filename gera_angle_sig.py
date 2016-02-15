#!/usr/bin/python

import sys
import scipy
import cPickle
import descritores
import numpy as np

diretorio = sys.argv[1]
raio = 15
bins = 250
range = (0.05,3.1)
f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   print im_file
   tmp = descritores.ass(diretorio+im_file,raio).sig
   tmp_h = np.histogram(tmp,bins = bins,range = range)[0]
   tmp_h = tmp_h.astype(float)/tmp_h.sum()
   db[im_file] = scipy.hstack((cl[im_file],tmp_h))
   print im_file,tmp_h
cPickle.dump(db,open(sys.argv[2],"wb"))
