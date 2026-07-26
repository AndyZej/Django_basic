import random

# Create an array of 10 random numbers from 1 to 60
numbers = []

for i in range(10):
    numbers.append(random.randint(1, 60))

print("Original array:", numbers)

# Modify numbers to make them even
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] += 1

print("Modified array:", numbers)