# Function that returns the sum of numbers in an array
def sum_array(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


# Example usage
numbers = [1, 2, 3]

result = sum_array(numbers)

print(result)