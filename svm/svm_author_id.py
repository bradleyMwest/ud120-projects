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

#import packages
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from time import time

#define SVM parameters
gam = 'auto'
cfactor = 10000.0
kern = 'rbf'
clf = SVC(C=cfactor,kernel=kern,gamma=gam)

#only use 1% of the data
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

#train the SVM model and calculate the time
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0,3), "s"

#predict the new classifications
pred = clf.predict(features_test)

#calculate the accuracy
acc = accuracy_score(pred, labels_test)
print 'RBF-SVM accuracy for Cfactor', cfactor,'is', round(acc*100,2), '%'

# pull out specific emails for certain lables
email_nums = [10,26,50]
for i in email_nums:
	if pred[i] == 0:
		Author = 'Sara'
	elif pred[i] == 1:
		Author = 'Chris'
	print 'Email number', i, 'was authored by', Author

#Count the toal number of emails written by Chris
chris_num = 0
sara_num = 0
for i in pred:
	if i == 0:
		sara_num+=1
	elif i == 1:
		chris_num+=1		

print 'Chris wrote ', chris_num, 'emails'
print 'Sara wrote ', sara_num, 'emails'
print 'The total number of test emails is', len(pred)
#########################################################


