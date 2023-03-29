import random
import math


# ceydas : 2 functions
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


# brianhenderburg: 4 functions
def check_ascii_sum(string):
    # Convert the string to a list of ASCII character values
    ascii_values = [ord(char) for char in string]

    # Sum up the ASCII character values
    ascii_sum = sum(ascii_values)

    # Divide the sum by 300
    result = ascii_sum / 300

    # Check if the result is smaller than 1
    if result < 1:
        return True
    else:
        return False


def play_rps():
    # Define the list of choices
    choices = ["rock", "paper", "scissors"]

    # Choose a random index from the list
    index = random.randint(0, 2)

    # Return the choice at the random index
    return choices[index]


def calculate_average(num1, num2, num3):
    # Calculate the average of three numbers
    average = (num1 + num2 + num3) / 3

    # Round the average to 2 decimal places
    rounded_average = round(average, 2)

    # Return the rounded average
    return rounded_average


def calculate_integral(a, b, n):
    # Define the function to integrate
    def f(x):
        return math.sin(x)

    # Calculate the width of each subinterval
    h = (b - a) / n

    # Calculate the sum of the function values at the endpoints of each subinterval
    sum = 0
    for i in range(n):
        xi = a + i * h
        sum += f(xi) + f(xi + h)

    # Multiply the sum by the width of each subinterval and divide by 2 to get the approximate integral
    integral = (h / 2) * sum

    # Return the approximate integral
    return integral