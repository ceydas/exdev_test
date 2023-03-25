
def add(x, y):
    return x + y        

def subtract(x, y):
    return x - y


#TODO: Multiply


def divide(x, y):
    return x / y

def main():
    while True:
        try:
            x = int(input("Enter first number: "))
            if x == 0:
                break
            y = int(input("Enter second number: "))
            op = input("Enter operation: ")
            if op == "+":
                print(add(x, y))
            elif op == "-":
                print(subtract(x, y))
            # TODO : Multiply
            elif op == "/":
                print(divide(x, y))
            else:
                print("Invalid operation.")
        except:
            print("Invalid input.")

main()