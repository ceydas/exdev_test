import random

# Define a list of fruits
fruits = ['apple', 'banana', 'orange', 'kiwi', 'grape']

# Pick a random fruit from the list
random_fruit = random.choice(fruits)

# Print the selected fruit
print("I'm feeling like having a", random_fruit)

# Define a function to check if a number is odd or even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Use the function to check if some numbers are even or odd
print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))

# Create a dictionary of people and their ages
people = {'John': 25, 'Jane': 30, 'Bob': 20}

# Loop through the dictionary and print each person's name and age
for name, age in people.items():
    print(name, "is", age, "years old")

# Define a class for a person with a name and an age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print("Hello, my name is", self.name, "and I'm", self.age, "years old")

# Create a new person object and call the say_hello() method
person1 = Person("Alice", 35)
person1.say_hello()
