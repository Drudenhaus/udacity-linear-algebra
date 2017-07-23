import vector

#1
num1_vector_a = vector.Vector([8.218, -9.341])
num1_vector_b = vector.Vector([-1.129, 2.111])
print("#1 - plus: {}".format(num1_vector_a + num1_vector_b))

# 2
num2_vector_a = vector.Vector([7.119, 8.215])
num2_vector_b = vector.Vector([-8.223, 0.878])
print("#2 - minus: {}".format(num2_vector_a - num2_vector_b))

# 3
num3_scalar = 7.41
num3_vector = vector.Vector([1.671, 1.012, -0.318])
print("#3 - scalar multiplication: {}".format(num3_vector * num3_scalar))
