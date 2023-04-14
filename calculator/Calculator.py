from Calculator_art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    exit = False
    while not exit:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the second number: "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if should_continue == "y":
            num1 = result
            continue
        elif should_continue == "n":
            exit = True
            calculator()

print(logo)
calculator()






