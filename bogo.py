# Small to large.
import random

def in_order(arr):
    in_order = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            in_order = False
    return in_order

array = input("Enter numbers separated with a space: ")
print("Sorting starts.")
array = array.split(" ")
array = [int(i) for i in array]  # Convert all elements to integer.

while in_order(array):
    random.shuffle(array)
    
print("Sorted: ")
print(" ".join([str(i) for i in array]))
