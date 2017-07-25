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
        try:
            return Vector([coordinate * (1 / self.magnitude()) for coordinate in self.coordinates])
        except ZeroDivisionError:
            raise ZeroVectorMagnitudeError

    def dot_product(self, other):
        if len(self) == len(other) and isinstance(other, Vector):
            return sum([a * b for a, b in zip(self.coordinates, other.coordinates)])
        else:
            raise ValueError("Both arguments must be Vector objects of the same length")

    def compute_angle_radians(self, other):
        try:
            return math.acos(self.dot_product(other) / (self.magnitude() * other.magnitude()))
        except ZeroVectorMagnitudeError:
            raise ZeroVectorAngleError

    def compute_angle_degrees(self, other):
        return math.degrees(self.compute_angle_radians(other))


class ZeroVectorMagnitudeError(Exception):
    def __init__(self):
        message = "Cannot normalize vector whose magnitude is zero"
        super(ZeroVectorMagnitudeError, self).__init__(message)


class ZeroVectorAngleError(Exception):
    def __init__(self):
        message = "Cannot compute an angle wiwth a vector whose magnitude is zero"
        super(ZeroVectorAngleError, self).__init__(message)
