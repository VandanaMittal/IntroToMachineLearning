#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Quiz 13: How many data points (people) are in the dataset?
# Ans: 146
data_points = len(enron_data)
print "The number of data points are", data_points


# Quiz 14: For each person, how many features are available?
# Ans: 21
no_of_features = len(enron_data[enron_data.keys()[0]])
print(enron_data[enron_data.keys()[0]])
print "The number of features are", no_of_features


# Quiz 15: How many POIs are there in the E+F dataset?
# Ans: 18

i = sum(author['poi'] for author in enron_data.values())
print "Number of POIs",i


'''These are other ways to find the number of POIs
# This link was helpful
# https://www.reddit.com/r/learnprogramming/comments/58zg6x/python_count_items_in_values_of_a_dict/

i = 0
for key, value in enron_data.iteritems() :
    if value["poi"] == True:
	       i = i + 1
print i

i = sum(author['poi'] for author in enron_data.values())
print i

i = sum(1 if author['poi'] else 0 for author in enron_data.values())
print i
'''

# Quiz 18: What is the total value of the stock belonging to James Prentice?
# Ans: 1095040
print "total value of the stock belonging to James Prentice", enron_data['PRENTICE JAMES']['total_stock_value']

# Quiz 19: How many email messages do we have from Wesley Colwell to persons of interest?
# Ans: 11
print "email messages from COLWELL WESLEY to POIs", enron_data['COLWELL WESLEY']['from_this_person_to_poi']



# Quiz 20: What's the value of stock options exercised by Jeffrey K Skilling?
# Ans: 19250000
print "value of stock options exercised by Jeffrey K Skilling", enron_data['SKILLING JEFFREY K']['exercised_stock_options']
