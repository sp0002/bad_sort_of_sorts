import random
x = input("Enter numbers: ")
x = x.split(" ")
y = []
for i in x:
    y.append(int(i))
while y != sorted(y):
    random.shuffle(y)
print("Sorted: ")
print("y")
