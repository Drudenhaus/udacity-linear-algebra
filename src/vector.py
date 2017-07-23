"""
Object class representation of an vector.
"""
import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __len__(self):
        return self.dimension

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        if len(self) == len(other) and isinstance(other, Vector):
            return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])
        else:
            raise ValueError("Both arguments must be Vector objects of the same length")

    def __sub__(self, other):
        if len(self) == len(other) and isinstance(other, Vector):
            return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])
        else:
            raise ValueError("Both arguments must be Vector objects of the same length")

    def __mul__(self, scalar):
        try:
            float(scalar)
            return Vector([coordinate * scalar for coordinate in self.coordinates])
        except ValueError:
            raise ValueError("Scalar must be a real number")

    def magnitude(self):
        return math.sqrt(sum([coordinate ** 2 for coordinate in self.coordinates]))

    def direction(self):
        return Vector([coordinate * (1 / self.magnitude()) for coordinate in self.coordinates])
