from array import array

# Write a program to reverse an array or string
# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

int_arr = array("i", [10, 4, 3, 50, 23, 90])

# printing original array
def show_arr(arr):
    print("The new created array is : ", end=" ")
    for i in range(0, len(arr)):
        print(arr[i], end=" ")

    print("\r")

#TODO 
def find_largest_three(arr):
    print("Find the largest three elements")
    
    
# def reverse_arr(arr):
#     print("Reverse array")
#     for i in range(0, len(arr)):
#         if len(arr) - 1 - i == i: break
            
#         arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]

# int_arr.reverse()
# reverse_arr(int_arr)

show_arr(int_arr)