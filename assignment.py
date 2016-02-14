#! /usr/bin/python2.7

# -*- coding: utf-8 -*-
"""
@author: ondrej-tucek
@date: 2016-02-14
"""

import pandas as pd
import numpy as np

from sklearn.cross_validation import train_test_split, cross_val_predict, cross_val_score
from sklearn.metrics import mean_squared_error, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

from plot_visualization import plot_variable_importance, plot_confusion_matrix


# plots of Variable importance, Confusion matrix
# True  => save and don't show to us the plots
# False => don't save the plots but show to us
save = True


#================================== Preparation =====================================
data_dir = "data/"
save_plots_dir = "img/"
dt = pd.read_csv(data_dir + "clean_trainig_data.csv")
d_test = pd.read_csv(data_dir + "clean_testing_data.csv")

users = pd.unique(dt.user_name)
users_train = pd.unique(d_test.user_name)
unq_classe = pd.unique(dt.classe)


for user in users:
    print "Name of participant =", user

    # pick up data from particular participants
    participant = dt[dt.user_name.isin({user})]
    participant_test = d_test[d_test.user_name.isin({user})]
    par_row, par_col = participant.shape

    # and their classe values, A, B,...
    label_classe = participant.classe.values
    le = LabelEncoder()
    classe = le.fit_transform(label_classe)
    classe_names = le.inverse_transform( le.fit_transform(unq_classe) )

    # prepare data to classification
    dp = participant.iloc[:, 2:par_col-1]
    dp_test = participant_test.iloc[:, 2:par_col-1]


    #================================= Prediction ===================================
    # splitting dp = data_participiant and classe to train data and test data
    x_train, x_test, y_train, y_test = train_test_split(dp, classe, test_size=0.30, \
      random_state=0)

    # Random Forest Classifier
    har_model = RandomForestClassifier(n_estimators=10, max_depth=None, \
      max_features=4, oob_score=False)

    har_model.fit(x_train,y_train)
    y_true, y_pred = y_test, har_model.predict(x_test)
    print har_model.score


    #================================== Result ======================================
    res = le.inverse_transform(har_model.predict(participant_test.iloc[:, 2:par_col-1]))
    print "Result:"
    for (j, num_id) in enumerate(participant_test.problem_id.values):
	print "{:>8} id = {:>2} {:>2}".format("",num_id, res[j])
      

    #========================== Accuracy of a Classification ========================
    print "\nMSE = ", mean_squared_error(y_test, y_pred)
    print "\nClassification report:\n", classification_report(y_true, y_pred, \
      target_names=classe_names)


    #============================ Plot visualizations ===============================
    # Plot feature importance
    feature_importance = har_model.feature_importances_
    names_cols = dp.columns[range(0,dp.shape[1])]    
    plot_variable_importance(feature_importance, names_cols, save_plots_dir \
      + "Variable_Importance_" + user, save=save)

    # Plot confusion matrix    
    print "Confusion matrix:"
    print pd.crosstab(y_true, y_pred, rownames=['True'], colnames=['Predicted'], \
      margins=True)
    cm = confusion_matrix(y_true, y_pred)
    plot_confusion_matrix(cm, classe_names, save_plots_dir + "Confusion_Matrix_" \
      + user, save=save)
    
    #================================================================================


print ""
print "Done..."

