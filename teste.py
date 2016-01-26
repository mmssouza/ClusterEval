#!/usr/bin/python

import cPickle
import sys
import metrics
import pylab

color = ["b","r","g"]
db = cPickle.load(open(sys.argv[1]))
X,Y = db[:,1:],db[:,0].astype(int)
print "CE = {0}".format(metrics.CE(X,Y-1))
print "PC = {0}".format(metrics.PC(X,Y-1))
print "CS = {0}".format(metrics.CS(X,Y-1))
print "DB = {0}".format(metrics.db(X,Y-1))
print "DI = {0}".format(metrics.di(X,Y))
print "Silhouette = {0}".format(metrics.silhouette(X,Y-1).mean())
for c,i in zip(color,range(1,4)):
 pylab.plot(X[pylab.where(Y == i)][:,0],X[pylab.where(Y == i)][:,1],"o"+c)
 
pylab.show()
