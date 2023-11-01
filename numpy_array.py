import numpy

one_dim_array = numpy.array([1, 2, 3, "test"])
two_dim_array = numpy.array(
    [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, "test"],
    ]
)
dimensions = 4, 3, 3
three_dim_array = numpy.ones(dimensions, dtype=numpy.uint8)

print(type(one_dim_array))
print(one_dim_array, one_dim_array.size)
print(two_dim_array, two_dim_array.size, two_dim_array.shape)
print(three_dim_array)

m = numpy.linspace(0, 10, 36)
m = m.reshape(dimensions)

print(m)