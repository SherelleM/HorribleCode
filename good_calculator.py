def add(number1, number2):
    """Returns the sum of two numbers."""
    return number1 + number2

def subtract(number1, number2):
    """Returns the difference between two numbers."""
    return number1 - number2

def multiply(number1, number2):
    """Returns the product of two numbers."""
    return number1 * number2

def divide(number1, number2):
    """Returns the quotient of two numbers. Returns None if dividing by zero."""
    if number2 == 0:
        print("Cannot divide by zero.")
        return None
    return number1 / number2

def get_valid_number(prompt):
    """Handles getting input to make sure it is actually a number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("\nEnter choice: ")

    if choice in ("1", "2", "3", "4"):
        number1 = get_valid_number("Enter first number: ")
        number2 = get_valid_number("Enter second number: ")

        if choice == "1":
            print(f"\n{number1} + {number2} = {add(number1, number2)}")

        elif choice == "2":
            print(f"\n{number1} - {number2} = {subtract(number1, number2)}")

        elif choice == "3":
            print(f"\n{number1} * {number2} = {multiply(number1, number2)}")

        elif choice == "4":
            result = divide(number1, number2)
            if result is None:
                print("Cannot divide by zero.")
            else:
                print(f"\n{number1} / {number2} = {divide(number1, number2)}")

        # check if user wants to do another calculation
        continue_calculation = input("\nDo you want to continue? (y/n): ")
        if continue_calculation == "n":
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")

