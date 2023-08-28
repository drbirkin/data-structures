# Python code to demonstrate the working of
# array(), append(), insert()
# https://www.geeksforgeeks.org/python-arrays/
# importing "array" for array operations
from array import array

# initializing array with array values
# initializes array with signed integers
# size of 3 O(n)
int_arr = array('i', [1, 2, 3])

# printing original array
print ("The new created array is : ",end=" ")
for i in range (0, 3):
	print (int_arr[i], end=" ")

print("\r")

# using append() to insert new value at end O(n)

# 1. Check Available Space:

# The module checks if there is enough space in the allocated memory for the new element. If there is enough space, it can directly add the new element. If not, it needs to allocate more memory.
# Allocate More Memory (if needed):

# If there is not enough space to add the new element, the module allocates a larger chunk of memory to store the elements. This new memory chunk is typically larger than the previous one to reduce the frequency of reallocations.
# 2. Copy Existing Elements:

# The module copies the existing elements from the old memory chunk to the new one. This copying process ensures that the data is preserved during the reallocation.
# 3. Add New Element:

# The new element is added to the end of the array in the new memory chunk.
# 4. Update Internal Metadata:

# The array module updates its internal metadata, such as the size of the allocated memory and the number of elements.
# 5. Release Old Memory (if applicable):

# The old memory chunk is no longer needed and can be released to the system to free up resources.
# TODO: show errors and bugs during those steps behind the scene

int_arr.append(4)

# printing appended array
print("The appended array is : ", end="")
for i in range (0, 4):
	print (int_arr[i], end=" ")
	
# using insert() to insert value at specific position
# inserts 5 at 2nd position O(n)
int_arr.insert(2, 5)

print("\r")

# printing array after insertion
print ("The array after insertion is : ", end="")
for i in range (0, 5):
	print (int_arr[i], end=" ")
 
print("\r")

# using pop() to remove element at 2nd position O(1)
print ("The popped element is : ",end="")
print (int_arr.pop(2))
 
# printing array after popping
print ("The array after popping is : ",end="")
for i in range (0,4):
    print (int_arr[i],end=" ")
 
print("\r")
 
# using remove() to remove 1st occurrence of 1 O(n)
int_arr.remove(1)

print ("\r")
 
# using index() to print index of 1st occurrence of 2 O(1)
print ("The index of 1st occurrence of 2 is : ",end="")
print (int_arr.index(2))
 
#using reverse() to reverse the array O(n)
int_arr.reverse()
 
# printing array after removing
print ("The array after removing is : ",end="")
for i in range (0,3):
    print (int_arr[i],end=" ")

print("\r")


# Displaying the array
print("Array:", int_arr)

#
# 
# 
# 

# two-dimensional array
two_dim_array = [array('i', [1, 2, 3]), array('i', [4, 1, 3]), array('i', [1, 2, 3]), array('i', [1, 2, 3])]

for i in range(0, len(two_dim_array)):
    # static row length to prevent memory outbound, python doesn't show error on creation
	for j in range(0, len(two_dim_array[1])):
		print(two_dim_array[i][j], end = ' ')
	print('\n')

print('Array 2D:', two_dim_array)