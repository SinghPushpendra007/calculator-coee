def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def logic_and(x, y):
    return x & y  # Use bitwise AND for binary logic

def logic_or(x, y):
    return x | y  # Use bitwise OR for binary logic

def logic_not(x):
    return ~x & 1  # Use bitwise NOT and mask to get 0 or 1

def logic_nand(x, y):
    return ~(x & y) & 1  # Use bitwise NAND

def logic_nor(x, y):
    return ~(x | y) & 1  # Use bitwise NOR

def logic_xor(x, y):
    return x ^ y  # Use bitwise XOR

def logic_xnor(x, y):
    return ~(x ^ y) & 1  # Use bitwise XNOR

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. AND")
print("6. OR")
print("7. NOT")
print("8. NAND")
print("9. NOR")
print("10. XOR")
print("11. XNOR")

while True:
    choice = input("Enter choice (1-11): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

    elif choice in ('5', '6', '8', '9', '10', '11'):
        try:
            num1 = int(input("Enter first binary input (any integer): "))
            num2 = int(input("Enter second binary input (any integer): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Perform logic operations
        if choice == '5':
            print(f"{num1} AND {num2} = {logic_and(num1, num2)}")

        elif choice == '6':
            print(f"{num1} OR {num2} = {logic_or(num1, num2)}")

        elif choice == '7':
            print(f"NOT {num1} = {logic_not(num1)}")

        elif choice == '8':
            print(f"{num1} NAND {num2} = {logic_nand(num1, num2)}")

        elif choice == '9':
            print(f"{num1} NOR {num2} = {logic_nor(num1, num2)}")

        elif choice == '10':
            print(f"{num1} XOR {num2} = {logic_xor(num1, num2)}")

        elif choice == '11':
            print(f"{num1} XNOR {num2} = {logic_xnor(num1, num2)}")

    else:
        print("Invalid Input")

    next_calculation = input("Let's do the next calculation? (yes/no): ")
    if next_calculation.lower() == "no":
        break
