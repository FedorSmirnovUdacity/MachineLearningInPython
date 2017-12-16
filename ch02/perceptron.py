"""

Perceptron classifier class

"""

import numpy as np


class Perceptron(object):
    """
    Parameters:

        eta : float - learning rate (between 0.0 and 1.0)
        n_iter _ int - number of training iterations

    Attributes:

        w_ : 1d-Array weights after adjustment
        errors_ : list number of wrong classifications per epoch

    """

    def __init__(self, eta=.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        Fit to the training data

        :param X: array-like, shape = [n_samples, n_features] training vectors
        :param y: array-like, shape = [n_samples] labels
        :return:
        """

        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """
        Calculate the net input to the perceptron (input before the thresholding)

        :param X:
        :return:
        """
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """
        Return the classifications

        :param X:
        :return:
        """
        return np.where(self.net_input(X) >= 0.0, 1, -1)
