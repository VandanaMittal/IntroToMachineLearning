#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []

    ### your code goes here

    print "length of the original data is :", len(predictions)
    err = predictions - net_worths # Here we find the error between actual and predicted value
    abs_err = abs(err) # Since the error can be positive and negative, we have taken the absolute of the error

    # Here we find the index of the list abs_err which is sorted in ascending order
    sorted_err_index = [i[0] for i in sorted(enumerate(abs_err), key=lambda x:x[1])]

    # Create the lists for the tuple asked above and add 90% data
    list_age = []
    list_net_worth = []
    list_error = []
    for i in range(0, 81):
        idx = sorted_err_index[i]
        list_age.append(ages[idx])
        list_net_worth.append(net_worths[idx])
        list_error.append(abs_err[idx])

    cleaned_data = zip(list_age,list_net_worth,list_error) # zip convert lists into tuple
    print ("length of the clean data is :", len(cleaned_data)) # we have removed the outliers here
    return cleaned_data
