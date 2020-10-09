# Small to large.
import time

array = input("Enter numbers separated with a space: ")
print("Sorting starts.")
array = array.split(" ")
array = [int(i) for i in array]  # Convert all elements to integer.

not_in_order = False
for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
        not_in_order = True
        
while not_in_order:
    # Generate random numbers of indices and swap them.
    index_one = str(time.time_ns())
    index_one = int(index_one[8:11]) * int(index_one[11:14]) + int(index_one[14:16]) ** int(index_one[16:])
    index_one = index_one % len(array)
    
    index_two = index_one
    while index_two == index_one:
        index_two = str(time.time_ns())
        index_two = int(index_two[8:11]) * int(index_two[11:14]) + int(index_two[14:16]) ** int(index_two[16:])
        index_two = index_two % len(array)
        
    array[index_one], array[index_two] = array[index_two], array[index_one]
        
    not_in_order = False
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            not_in_order = True
            
    
print("Sorted: ")
print(" ".join([str(i) for i in array]))
