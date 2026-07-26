# Get range values
x = int(input("Enter x: "))
y = int(input("Enter y: "))

# Calculate sum
total = 0

for number in range(x, y + 1):
    total += number

# Display result
print("Sum =", total)