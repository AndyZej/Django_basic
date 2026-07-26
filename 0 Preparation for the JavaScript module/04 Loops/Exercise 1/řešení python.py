# Variable x
x = int(input("Enter a number: "))

# Calculate factorial
factorial = 1

for i in range(1, x + 1):
    factorial *= i

# Display result
print(f"{x}! = {factorial}")