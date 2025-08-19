import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

saved_num = 0
run = True
while run:
    if saved_num == 0:
        print(art.logo)
        num1 = float(input("What is the first number? :"))
    operator = input("+\n-\n*\n/\nWhat is the operation to perform? :")
    num2 = float(input("What is the second number? :"))
    result = operations[operator](num1, num2)
    print(f"The result is: {result}")
    next_calc = input(f"Would you like keep calculating with the number {result}? y/n? ").lower()
    if next_calc == "y":
        saved_num = result
    elif next_calc == "n":
        saved_num = 0
