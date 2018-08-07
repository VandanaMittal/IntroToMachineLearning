#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
# Quiz 26
# Soluion : Accuracy on the test data is 0.94
from sklearn.metrics import accuracy_score
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(labels_test, pred)
print("Accuracy on the test data is :", acc)


# Quiz 27
# Solution : The feature value is 0.76 and its index is 33614
features_list = clf.feature_importances_
counter = 0
for i in features_list:
    counter = counter + 1
    if (i > 0.2):
        print "important feature is :", i, "feature index is :", counter-1

# Quiz 28
# Solution : sshacklensf
features_name = vectorizer.get_feature_names()
# print("words associated to most important feature", features_name[33614])

# Quiz 29 Next feature is : cgermannsf
print("words associated to most important feature", features_name[14343])

# Quiz 30 Next feature is : houectect : but it doesn't look like an obvious signature word so let's keep moving without removing it.
print("words associated to most important feature", features_name[21323])

print("Accuracy on the test data is :", acc) # Accuracy is 0.816
print("Now that we've removed the outlier signature words : the training data is starting to overfit to the words that remain.")
