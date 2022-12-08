from util import operations
from art import logo
from replit import clear

list_with_operations = ['+', '-', '*', '/']


def calculator():
    global num1, num2
    print(logo)

    try:
        num1 = float(input("What's the first number?: "))

    except ValueError:
        print('The provided value is not a number')
        calculator()

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in list_with_operations:
            print('Incorrect symbol')
            continue

        try:
            num2 = float(input("What's the next number?: "))

        except ValueError:
            print('The provided value is not a number')
            calculator()

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            print(logo)
            calculator()


calculator()
