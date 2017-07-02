#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

gam = 'auto'
cfactor = 10000.0

features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 

clf = SVC(C=cfactor,kernel="rbf",gamma=gam)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print 'RBF-SVM accuracy for Cfactor', cfactor,'is', round(acc*100,2), '%'

indexes = [10,26,50]
for i in indexes
	if pred[i] == 0:
		Author = 'Sara'
	elif pred[i] == 1:
		Author = 'Chris'
	print 'Email number', i, 'was authored by', Author
#########################################################


