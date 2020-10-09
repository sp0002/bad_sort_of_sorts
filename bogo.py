import random

array = input("Enter numbers separated with a space: ")
print("Sorting starts.")
array = array.split(" ")
array = [int(i) for i in array]  # Convert all elements to integer.

while array != sorted(array):
    random.shuffle(array)
    
print("Sorted: ")
print(" ".join([str(i) for i in array]))
