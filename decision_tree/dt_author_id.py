#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
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

# Features used in this data
number_of_features = len(features_train[0]) # number of columns is the number of features
print(number_of_features)

#########################################################
### your code goes here ###

# Changed the number of features from 10% to 1% and then calculated the accuracy
# Accuracy changed from 0.9795221843 to 0.966439135381

from sklearn.metrics import accuracy_score
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split = 40)
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(labels_test, pred)
print(acc)
#########################################################
