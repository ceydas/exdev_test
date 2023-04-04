import random

def generate_password(length):
    """Generate a random password of given length."""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

class Person:
    """A class representing a person."""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
    
    def introduce(self):
        print(f"Hi, my name is {self.name} and I'm a {self.gender} who is {self.age} years old.")

class Employee(Person):
    """A class representing an employee."""
    def __init__(self, name, age, gender, company, salary):
        super().__init__(name, age, gender)
        self.company = company
        self.salary = salary
    
    def introduce(self):
        super().introduce()
        print(f"I work at {self.company} and earn {self.salary} dollars a year.")

class Calculator:
    """A class representing a calculator."""
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b if b != 0 else None

class BankAccount:
    """A class representing a bank account."""
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

class Car:
    """A class representing a car."""
    def __init__(self, make, model, year, color, speed):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed
    
    def accelerate(self, amount):
        self.speed += amount
    
    def brake(self, amount):
        self.speed -= amount if self.speed >= amount else self.speed
    
    def info(self):
        print(f"This is a {self.year} {self.make} {self.model} in {self.color} color.")

if __name__ == "__main__":
    password = generate_password(8)
    print(f"Your new password is: {password}")
    
    person = Person("John", 30, "male")
    person.greet()
    person.introduce()
    
    employee = Employee("Jane", 25, "female", "Acme Inc.", 50000)
    employee.greet()
    employee.introduce()
    
    calculator = Calculator()
    print(f"The result of 5 + 3 is: {calculator.add(5, 3)}")
    print(f"The result of 5 - 3 is: {calculator.subtract(5, 3)}")
    print(f"The result of 5 * 3 is: {calculator.multiply(5, 3)}")
    print(f"The result of 5 / 3 is: {calculator.divide(5, 3)}")
    
    account = BankAccount("123456789", 1000)
    print(f"The balance of your account is: {account.balance}")
    account.deposit(500)
   

# kavunici: fix issue 6

def fix_issue6():
    print("fixed issue 6")
    return True