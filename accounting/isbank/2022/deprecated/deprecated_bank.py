import random

# Generate 30 random floats with 2 decimal precision
numbers = [round(random.uniform(0, 100), 2) for i in range(30)]

# Initialize a variable to keep track of the sum-so-far
sum_so_far = 0

# Iterate over the list of numbers and print the sum-so-far for each number
for number in numbers:
    sum_so_far += number
    print("{:.2f}\t{:.2f}".format(number, sum_so_far))
