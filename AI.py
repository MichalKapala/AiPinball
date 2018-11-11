import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score


class AI():
    def __init__(self, estimator='log'):
        self.fited = False
        self.estimator = estimator
        if estimator == 'log':
            self.Model = LogisticRegression(max_iter=10)
        if estimator == 'sgd':
            self.Model = SGDClassifier(max_iter=10)

    def fit(self):
        dane = pd.read_csv('ruch.data', sep=' ', header=None)
        X = dane.iloc[:, 0:3].values
        y = dane.iloc[:, [3]].values
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3)
        self.y_train, self.y_test = self.y_train.ravel(), self.y_test.ravel()
        self.Model.fit(self.x_train, self.y_train)
        self.fited = True

    def predict(self, dt_y, dt_x, v_y):
        x = np.zeros(3)
        x[0] = dt_y
        x[1] = dt_x
        x[2] = v_y
        x = x.reshape(1, -1)
        return self.Model.predict(x)







