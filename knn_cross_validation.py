#!/usr/bin/python


# Code source: Gael Varoqueux
# Modified for Documentation merge by Jaques Grobler
# License: BSD
import warnings
import numpy as np
from sklearn import neighbors,decomposition,cross_validation,pipeline,metrics,naive_bayes,qda,lda
import sys
import cPickle
from sklearn.preprocessing import scale
import silhouette

# import some data to play with
warnings.simplefilter("ignore")

db = cPickle.load(open(sys.argv[1],'r'))
Y = np.array([db[i][0] for i in db.keys()]).astype(int)
X = np.array([db[i][1:] for i in db.keys()])
 
s = float(Y.shape[0])
priors = np.array([float(np.where(Y == i)[0].shape[0])/s for i in range(1,Y.max()+1)])

classifiers = ['nb','knn','lda','qda']


clf = [pipeline.Pipeline([('pca',decomposition.PCA(n_components = 6,whiten = False)),('nb',naive_bayes.GaussianNB())]),
           pipeline.Pipeline([('pca',decomposition.PCA(n_components = 6,whiten = False)),('knn',neighbors.KNeighborsClassifier(n_neighbors = 1))]),
           pipeline.Pipeline([('pca',decomposition.PCA(n_components = 6,whiten = False)),('lda',lda.LDA())]),
		   pipeline.Pipeline([('pca',decomposition.PCA(n_components = 6,whiten = False)),('qda',qda.QDA())])]

s = silhouette.silhouette(X,Y-1)
print np.median(s)
it = cross_validation.KFold(Y.size,n_folds = 10)
for c,cn in zip(clf,classifiers):
  res = cross_validation.cross_val_score(c,scale(X),Y,cv = it,scoring = "f1_weighted")
  print  cn+': ',res.mean(),res.std()
  
