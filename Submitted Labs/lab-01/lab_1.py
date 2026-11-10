# Lab 1: Linear Regression (corresponding to lecture handout 1)
import numpy as np

# This function computes the polynomial of order 'order' corresponding to a least-squares fit
# to the data (x, y), where 'y' contains the observed values and 'x' contains the x-ordinate
# of each observed value.
#
# The normal equation is solved in the function 'linear_regression'.
def LS_poly(x, y, order, eps = 0):
    # First build the polynomial design matrix (relies only x-ordinates, not observed values)
    X = polynomial_design_matrix(x, order)
    # Then find the polynomial using this matrix and the values 'y'.
    w = linear_regression(X, y, eps=eps)
    return w

# Computes the polynomial design matrix.
#
# For a vector 'x', this contains all powers up to 'order'
# of each element of 'x'.  This kind of matrix is also called
# a Vandermonde matrix.
#
# The numpy array 'x' contains the x-ordinates (x-axis
# values) which we are analyzing.
def polynomial_design_matrix(x, order=1):
    x_flat = np.asarray(x).flatten()
    X = np.zeros(shape=(x_flat.size, order+1))
    for p in range(0, order+1):
        for i in range(x_flat.size):
            X[i, p] = x_flat[i] ** p
    return X

# Given values 'y' and the polynomial design matrix for the x-ordinates of those
# values in 'X', find the polynomial having the best fit:
#
# theta = ((X'X + I)^(-1))*X'y
#
# This uses numpy to solve the normal equation (see slide 16 of handout 1)
def linear_regression(X, y, eps=0):
    M = np.dot(X.transpose(), X)
    # Implement Tikhonov regularisation exactly as required:
    M = M + eps * np.identity(M.shape[0])
    theta = np.dot(np.linalg.inv(M), np.dot(X.transpose(), y))
    return theta

# EXERCISE 3: implement computation of mean squared error between two vectors
def mean_squared_error(y1, y2):
    return np.mean((y1 - y2) ** 2)

# EXERCISE 4: return the number of the best order for the supplied
# data (see the notebook).
def question_4():
    return 3
