# Python code to demonstrate the working of
# array(), append(), insert()

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