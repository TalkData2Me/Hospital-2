import pandas as pd
import numpy as np
from loaddata import processedData

processedData = processedData.dropna()
y=processedData['num']
X=processedData.drop(['num'], axis=1)
processedData.head()

import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE
from sklearn import cross_validation
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import cross_val_predict
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVR

model = LogisticRegression()
selector = RFE(model, 12, step=1)
selector.fit(X,y)

# summarize the selection of the features
print X.columns[selector.get_support()]

#get the only selected features from X
X_new=selector.transform(X)
X_new = pd.DataFrame(X_new,columns = [X.columns[selector.get_support()]])

# 5-folder cross validation
y_pred=cross_val_predict(model,X_new,y, cv=5)

#print precision_score(y,y_pred,average=None)
#print recall_score(y,y_pred,average=None)
#print f1_score(y,y_pred,average=None)
#print accuracy_score(y,y_pred)
#print classification_report(y,y_pred)

#######################################################
# def full_precision (estimator, X_test, y_test):
#     y_pred = estimator.predict(X_test)
#     return precision_score(y_test,y_pred, average=None)

# cross_val_score(model,X_new,y,scoring = full_precision, cv=5)

# 5-folder cross validation
# skf = cross_validation.StratifiedKFold(y, n_folds=5)

# accs = []
# for train_index, test_index in skf:
#     #print("TRAIN:", train_index, "TEST:", test_index)
#     X_train, X_test = X_new.iloc[train_index], X_new.iloc[test_index]
#     y_train, y_test = y.iloc[train_index], y.iloc[test_index]
#     model.fit(X_train,y_train)
#     y_test_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test,y_test_pred)
#     accs.append(accuracy)
#     print 'Logistic Regression accuracy: %.4f' % (accuracy)

#model =  SVR(kernel="linear")

# create a base classifier used to evaluate a subset of attributes
model = LogisticRegression()

feature_combination = {}
result_precision = []

for number_feature in range(1,len(X.columns)+1):

    # create the RFE model with fixed number of features
    selector = RFE(model, number_feature, step=1)
    selector.fit(X,y)

    # summarize the selection of the features
    feature_combination[number_feature] = X.columns[selector.get_support()]

    #get the only selected features from X
    X_new=selector.transform(X)
    X_new = pd.DataFrame(X_new,columns = [X.columns[selector.get_support()]])

    # 5-folder cross validation
    y_pred=cross_val_predict(model,X_new,y, cv=5)
    precision = precision_score(y,y_pred,average=None)
    #recall_score(y,y_pred,average=None)
    #f1_score(y,y_pred,average=None)
    #accuracy_score(y,y_pred)

    result_precision.append(precision)


print(result_precision)
pd.DataFrame(result_precision)

print(featuer_combination[6])
#results.append(accs)
