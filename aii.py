import pylab
import scipy
import cv2

def AreaIntegralInvariant(name,r):
 im = cv2.imread(name,0)
# Descomente caso imagem seja fundo branco
# im = cv2.bitwise_not(im)
 im_aux = scipy.zeros((im.shape[0]+4*r,im.shape[1]+4*r),dtype=im.dtype)
 im_aux[2*r:im_aux.shape[0]-2*r,2*r:im_aux.shape[1]-2*r] = im
 im = im_aux.copy()
 cnt,h = cv2.findContours(im_aux,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
 l = []
 for a in cnt[0]:
  c = a[0][0],a[0][1]
  aux = scipy.zeros(im.shape,dtype = im.dtype)
  cv2.circle(aux,c,r,255,-1)
  aux2 = cv2.bitwise_and(aux,im)
  cnt2,h = cv2.findContours(aux2,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
  area = 0
  for c in cnt2:
   area = area + cv2.contourArea(c)
  l.append(area)

 return scipy.array(l)


