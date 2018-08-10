#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here

# Splitted the data into test and training data. Accuracy is 0.724
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
from sklearn.metrics import accuracy_score
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
pred = clf.predict(X_test)


# Quiz 28 : How many POIs are predicted for the test set for your POI identifier?
# Solution : If the the person in the predicted data is POI then the value in pred
# for that person is 1, otherwise 0.

print sum(pred)

count = 0
for i in pred:
    count = count + 1
    if i==1:
        print i
        print count

#print len(pred)
acc = accuracy_score(y_test, pred)
print("The accuracy on test data is :", acc)
