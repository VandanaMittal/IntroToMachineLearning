#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!

# Quiz 17 : Training the full dataset and using the default parameters of the decision treeself.
# Testing is then done on the same data. Accuracy is pretty high 0.989 which is ambigous.
from sklearn.metrics import accuracy_score
from sklearn import tree
#clf = tree.DecisionTreeClassifier(min_samples_split = 40)
#clf = clf.fit(features_train, labels_train)
#pred = clf.predict(features_test)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
pred = clf.predict(features)
acc = accuracy_score(labels, pred)
print("The accuracy of overfitted data is :", acc)
