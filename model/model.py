import pandas as pd
import numpy as np

from sklearn.cross_validation import train_test_split

from sklearn import model_selection
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LogisticRegression
from sklearn import metrics

import statsmodels.api as sm

import dill as pickle

def build_and_train():

    df = pd.read_csv('games.csv')

    cols = ['t1_batAvg', 't2_batAvg', 't1_OBP', 't2_OBP', 't1_OPS', 't2_OPS', 't1_slug', 't2_slug', 't1_ERA', 't2_ERA']

    X = df[cols]
    y = df['t1_winner?']

    logreg = LogisticRegression()
    logreg.fit(X, y)

    return logreg


def build_and_test():
    df = pd.read_csv('games.csv')

    cols = ['t1_batAvg', 't2_batAvg', 't1_OBP', 't2_OBP', 't1_OPS', 't2_OPS', 't1_slug', 't2_slug', 't1_ERA', 't2_ERA']

    X = df[cols]
    y = df['t1_winner?']


    logit_model=sm.Logit(y,X)
    result=logit_model.fit()
    print(result.summary())

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)

    y_pred = logreg.predict(X_test)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))


    kfold = model_selection.KFold(n_splits=10, random_state=7)
    modelCV = LogisticRegression()
    scoring = 'accuracy'
    results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
    print("10-fold cross validation average accuracy: %.3f" % (results.mean()))


    # li = [0.257, 0.182, 0.308, 0.250, 0.679, 0.614, 0.371, 0.364, 3.00, 5.0] # 1
    # li2 = [0.176,0.219,0.2,0.265,0.465,0.546,0.265,0.281,0.0,3.0] # 1
    # li3 = [0.156,0.2,0.208,0.25,0.431,0.472,0.222,0.222,0.75,0.0] # 0

    # a = np.reshape(li3, (1, -1))

    # print(logreg.predict(a))

if __name__ == '__main__':
    model = build_and_train()
    # build_and_test()

    filename = 'model_v1.pk'
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
    
    # with open(filename ,'rb') as f:
    #     loaded_model = pickle.load(f)

    # li = [0.257, 0.182, 0.308, 0.250, 0.679, 0.614, 0.371, 0.364, 3.00, 5.0] # 1
    # li2 = [0.176,0.219,0.2,0.265,0.465,0.546,0.265,0.281,0.0,3.0] # 1
    # li3 = [0.156,0.2,0.208,0.25,0.431,0.472,0.222,0.222,0.75,0.0] # 0

    # a = np.reshape(li3, (1, -1))

    # print(loaded_model.predict(a))