import random

def sum_so_far(numbers):
    # Initialize a variable to keep track of the sum-so-far
    sum_so_far = 0

    # Iterate over the list of numbers and print the sum-so-far for each number
    for number in numbers:
        sum_so_far += number
        print("{:d}\t{:d}".format(number, sum_so_far))



def generate_name():
    # Generate 10 random integers between 1-5
    numbers = [random.randint(1, 5) for i in range(10)]

    # Sum up the numbers
    total = sum(numbers)

    # Convert the sum to ASCII letters (A=65, B=66, C=67, etc.)
    name = "".join([chr(total + 64) for i in range(3)])

    return name