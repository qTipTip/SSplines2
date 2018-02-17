import numpy as np

from SSplines.spline_function import SplineFunction


class SplineSpace(object):
    """
    Represents a space of spline functions of degree 0/1/2 over the PS12-split of a triangle.
    """

    def __init__(self, triangle, degree):
        """
        Initialise a spline space of degree d over the triangle delineated by given vertices.
        :param np.ndarray triangle:
        :param int degree:
        """

        self.triangle = np.array(triangle)
        self.degree = int(degree)
        self.dimension = 10 if degree == 1 else 12

    def function(self, coefficients):
        """
        Returns a callable spline function with given coefficients.
        :param np.ndarray coefficients:
        :return: SplineFunction
        """
        return SplineFunction(self.triangle, self.degree, coefficients)

    def basis(self):
        """
        Returns a list of '~self.dimension' number of basis functions as callable spline functions.
        :return list: basis SplineFunctions
        """
        coefficients = np.eye(self.dimension)
        return [self.function(c) for c in coefficients]