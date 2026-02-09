print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("\nEnter choice: ")

    if choice in ("1", "2", "3", "4"):
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == "1":
            print(f"\n{number1} + {number2} = {number1 + number2}")

        elif choice == "2":
            print(f"\n{number1} - {number2} = {number1 - number2}")

        elif choice == "3":
            print(f"\n{number1} * {number2} = {number1 * number2}")

        elif choice == "4":
            if number2 == 0:
                print("Cannot divide by zero.")
            else:
                print(f"\n{number1} / {number2} = {number1 / number2}")

        continue_calculation = input("\nDo you want to continue? (y/n): ")
        if continue_calculation == "n":
            break
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")