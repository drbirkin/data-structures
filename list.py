def create_multidimensional_list(dimensions, value=None):
    if not dimensions:
        return value
    return [create_multidimensional_list(dimensions[1:], value) for _ in range(dimensions[0])]

# Create a 3x3x3 multidimensional list
dimensions = [3, 4, 3]
multi_dim_list = create_multidimensional_list(dimensions, 1)

# Accessing elements
print(multi_dim_list[1][2][0])  # Access element at depth 1, row 2, column 0
print(multi_dim_list)  # Access elements

# TODO print array