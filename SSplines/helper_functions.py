import numpy as np


def barycentric_coordinates(triangle, points, tol=1.0E-15):
    """
    Computes the barycentric coordinates of one or more point(s) with respect to the given triangle.
    :param triangle: vertices of the triangle
    :param points: a set of points
    :param tol: a tolerance for round off error
    :return: a set of barycentric coordinates, ndarray of ndim = 2.
    """

    p = np.atleast_2d(points) # make sure the points are shaped properly
    A = np.concatenate((triangle, np.ones((3, 1))), axis=1).T # append a column of ones
    b = np.concatenate((p, np.ones((len(p), 1))), axis=1) # append a column of ones

    x = np.linalg.solve(A[None, :, :], b) # broadcast A to solve all systems at once

    x[abs(x) < tol] = 0 # remove round off errors around zero
    return x