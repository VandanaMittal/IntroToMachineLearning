#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

# Remove a key-value pair from a dictionary is the following line: dictionary.pop( key, 0 )
# In our data TOTAL was the key which we want to pop out
data_dict.pop( 'TOTAL' )
data = featureFormat(data_dict, features)

#for i in data_dict:
#    print i

# Quiz 18: Two people made bonuses of at least 5 million dollars, and a salary of over 1 million dollars.
# What are the names associated with those points?

### your code below
'''for i in data_dict:
    if (data_dict[i]['bonus'] > 4000000  and data_dict[i]['bonus'] != 'NaN'):
        print i, data_dict[i]['bonus']
'''

for i in data_dict:
    if (data_dict[i]['bonus'] > 5000000  and data_dict[i]['bonus'] != 'NaN' and data_dict[i]['salary'] > 1000000 ):
        print i, data_dict[i]['bonus']

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
