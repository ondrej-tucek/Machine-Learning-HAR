#! /usr/bin/python2.7

# -*- coding: utf-8 -*-
"""
@author: ondrej-tucek
@date: 2016-02-14
"""

import pandas as pd

data_dir = "data/"
in_data = (data_dir+"HAR_training.csv", data_dir+"HAR_testing.csv")
out_data = (data_dir+"clean_training_data.csv", data_dir+"clean_testing_data.csv")


# what we want to remove, columns or row
axis = 'columns'


# ======================== Data cleaning ========================
for (out, dataset) in enumerate(in_data):
    # reading data
    data = pd.read_csv(dataset, low_memory=False)
    #The reason you get this low_memory warning is because 
    #guessing dtypes for each column is very memory demanding. 
    #Pandas tries to determine what dtype to set by analyzing 
    #the data in each column.

    # drop columns with empty cells (or nan) and strings
    d = data.dropna(axis)

    # remove a first a few columns
    dd = d.drop(d.columns[[0, 2, 3, 4, 5, 6]], axis) # Note: zero indexed

    dd.to_csv(out_data[out])


print "Done... cleaning data.\n"