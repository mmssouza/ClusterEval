#!/usr/bin/python
import sys
import cPickle
import numpy
import matplotlib.pyplot as PLT
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from PIL import Image
from PIL import ImageColor
from sklearn.manifold import Isomap,MDS
from sklearn.preprocessing import scale
import descritores as desc
from scipy.spatial.distance import pdist
import silhouette
		  
colors = {1:"#555500",2:"#7faa00",3:"#aaff00",4:"#ff5500",5:"#00aa2a",6:"#2aff2a",7:"#7f002a",	
8:"#aa2a2a",9:"#d4552a",10:"#ff7f2a",11:"#00d455",12:"#2aff55",13:"#7f2a55",14:"#aa5555",15:"#d47f55",	
16:"#ffaa55",17:"#2a2a00",18:"#2aff7f",19:"#7f007f",20:"#aa557f",21:"#d47f7f",22:"#ffaa7f",23:"#00ffaa",	
24:"#5500aa",25:"#7f2aaa",26:"#aa55aa",27:"#d4aaaa",28:"#ffd4aa",29:"#2a00d4",30:"#552ad4",31:"#7f55d4",	
32:"#aa7fd4"}

path = sys.argv[2]
with open(sys.argv[1],"r") as f:
  db = cPickle.load(f)

# nome das figuras
data1 = numpy.array([db[i] for i in db.keys()])

Y = data1[:,0].astype(int)
X1 = data1[:,1:]
s = silhouette.silhouette(X1,Y-1)
print numpy.median(s)

#iso = Isomap(n_neighbors=98, max_iter= 2500)
mds =  MDS(n_init = 20,dissimilarity = 'euclidean',max_iter = 2500)
#X1 = iso.fit_transform(data1[:,1:])
X1 = mds.fit_transform(X1)

data = numpy.vstack((Y,X1.transpose())).transpose()

db = dict(zip(db.keys(),data))
 
fig = PLT.gcf()
fig.clf()
ax = PLT.subplot(111)
PLT.gray()
PLT.xlim((-3.5,3.5))
PLT.ylim((-3.5,4))
for im in db.keys():
 # add a first image
 img = Image.open(path+im)
 img.thumbnail((150,150),Image.ANTIALIAS)
 #img = PIL.ImageOps.invert(img.convert("L"))
 img = img.convert("RGBA")
 datas = img.getdata()
 newData = []
 for item in datas:
   if item[0] == 255 and item[1] == 255 and item[2] == 255:
     newData.append((255, 255, 255, 0))
   else:
     newData.append(ImageColor.getrgb(colors[int(db[im][0])]))
 img.putdata(newData) 
 imagebox = OffsetImage(numpy.array(img), zoom=.15)
 xy = [db[im][1],db[im][2]]               # coordinates to position this image
 ab = AnnotationBbox(imagebox, xy,
      xybox=(5., -5.),
      xycoords='data',
      boxcoords="offset points",
	  frameon = False)                                  
 ax.add_artist(ab)

# rest is just standard matplotlib boilerplate
ax.grid(False)
PLT.draw()
PLT.show()

