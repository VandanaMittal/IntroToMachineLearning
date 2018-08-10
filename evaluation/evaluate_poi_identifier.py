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
print "the number of predicted POIs are :", sum(pred)  # ans = 4

# Quiz 29 : How many people total are in your test set?
print "the total people in test set are :", len(pred) # ans = 29
acc = accuracy_score(y_test, pred)
print("The accuracy on test data is :", acc) # accuracy =  0.724

# Quiz 30 : If your identifier predicted 0. (not POI) for everyone in the test set,
# what would its accuracy be?
count = 0
for i in pred:
    count = count + 1
    if i==1:
        # print i
        print count
        # set the predicted POI as 0, the accuracy is improved to 86.2%
        pred[count-1] = 0 # 0.862
acc = accuracy_score(y_test, pred)
print("The accuracy on test data after replacing POI as 0 is :", acc) # accuracy = 0.862

# Quiz 31 : Do you get any true positives? (a true positive is the
# case where both the actual label and the predicted label are 1)

predicted_labels = pred
true_labels = y_test
true_positives = 0
for i in range(len(predicted_labels)):
    if predicted_labels[i] == 1 and true_labels[i] == 1:
        true_positives = true_positives + 1
print "the true positives are: ", true_positives   # there are no true positives. having imbalanced classes like we have in the Enron dataset (many more non-POIs than POIs) introduces some special challenges, namely that you can just guess the more common class label for every point, not a very insightful strategy, and still get pretty good accuracy!
