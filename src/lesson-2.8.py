import vector

# 1
a = vector.Vector([7.8870, 4.138])
b = vector.Vector([-8.802, 6.776])
print("#1 - dot product:\t{}".format(a.dot_product(b)))

# 2
c = vector.Vector([-5.955, -4.904, -1.874])
d = vector.Vector([-4.496, -8.7550, 7.103])
print("#2 - dot product:\t{}".format(c.dot_product(d)))

# 3
e = vector.Vector([3.183, -7.627])
f = vector.Vector([-2.668, 5.319])
print("#3 - angle in radians:\t{}".format(e.compute_angle_radians(f)))

# 4
g = vector.Vector([7.350, 0.221, 5.188])
h = vector.Vector([2.751, 8.259, 3.985])
print("#4 - angle in degrees:\t{}".format(g.compute_angle_degrees(h)))
