#!/usr/bin/python

import sys
import scipy
import cPickle
import descritores as desc
import numpy as np

diretorio = sys.argv[1]
sigma = 32.
bins = 35
range = (-1.,1.)
f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = desc.curvatura(diretorio+im_file,scipy.array([sigma])).curvs[0]
   tmp_h = np.histogram(tmp,bins = bins,range = range)[0]
   tmp_h = tmp_h.astype(float)/tmp_h.sum()
   db[im_file] = scipy.hstack((cl[im_file],tmp_h))
   print im_file,tmp_h
cPickle.dump(db,open(sys.argv[2],"w"))
