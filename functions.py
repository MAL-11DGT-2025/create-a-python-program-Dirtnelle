def greeting():
    print("Good Afternoon.")

def greeting_w_name(name):
    print(f"Good Afternoon {name}.")

def add(a, b):
    print(a + b)

def minus(a,b):
    print(a - b)

def divide(a, b):
    print(a / b)

    def multiply(a, b):
        print(a * b)

# greeting()
# greeting_w_name("Dohnelle")
# greeting_w_name("Peter")
# greeting_w_name("Paul")
# add(5, 10)
# add(3, 9)
# add(2314, 3223)
# minus(7,6)

operation = input("Which operation do you want to use ( +, - , *, /): ")
a = input("Enter your first number:")
b = input("Enter your second number")

if operation == "+":
    add(a, b)
elif operation == "-":
    minus(a, b)
elif operation == "*":
    multiply(a, b)
elif operation =="/":
    divide(a, b)