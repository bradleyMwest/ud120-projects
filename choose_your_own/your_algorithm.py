#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from time import time


maxfeat = 'sqrt'
#samp_split = 5

macc = 0
samp_split = 17
n_est = 2
clf = RandomForestClassifier(	max_features=maxfeat, min_samples_split=samp_split,
			criterion='gini')
t = time()
clf.fit(features_train,labels_train)
#print 'The trainign time is ', round(time()-t,2), 'seconds'
pred = clf.predict(features_test)
acc = accuracy_score(labels_test,pred)
print 'n_est = ',n_est, 'min_samples_split=',samp_split,'max_features=',maxfeat
print 'The Random Forest accuracy is', round(acc*100,2), '%'

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
lr = 0.5
nest = 13
for md in range(1,10,1):
	clf = AdaBoostClassifier(DecisionTreeClassifier(criterion='entropy',splitter='random',max_depth=4),n_estimators=nest,learning_rate=lr,algorithm='SAMME')
	t = time()
	clf.fit(features_train,labels_train)
	print 'The trainign time is ', round(time()-t,2), 'seconds'
	pred = clf.predict(features_test)
	acc = accuracy_score(labels_test,pred)
	print 'The AdaBoost accuracy is', round(acc*100,2), '%', 'for max_depth=', md


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
plt.show()