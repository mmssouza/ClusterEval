import numpy as np
import math
import scipy.stats
import warnings

warnings.filterwarnings("ignore", category = RuntimeWarning)

def chi_square(x,y): # chi square distance
    acum = 0.
    for p,q in zip(x,y):
     h = (p + q)/2
     if h < 1e-12:
      h = 0
     else:
      h = ((p - h)**2)/h
     acum = acum + h
    return acum

def He(x,y): # Hellinger distance
    acum = 0.
    for p,q in zip(x,y):
     acum = acum + (math.sqrt(p) - math.sqrt(q))**2
    acum = acum/2
    acum = math.sqrt(acum)
    return acum

def D_KL(p,q): # Kullback Leiben divergence
  aux = (p + q)/2
 return (scipy.stats.entropy(p,aux) + scipy.stats.entropy(p,aux))/2

def jsd(x,y): #Jensen-shannon divergence
    d1 = x*np.log2(2*x/(x+y))
    d2 = y*np.log2(2*y/(x+y))
    d1[np.isnan(d1)] = 0
    d2[np.isnan(d2)] = 0
    d = 0.5*np.sum(d1+d2)    
    return d

def Patrick_Fisher(x,y):
 acum = 0
 for p,q in zip(x,y):
  acum = acum + (p - q)**2
 return acum**0.5    

