# HorribleCode

This project demonstrates two different approaches to writing a simple calculator in Python. It includes a bad_calculator.py version, which functions correctly but is poorly structured, and a good_calculator.py version, which refactors the code to meet professional coding conventions.

## The Good Version (good_calculator.py)
The good_calculator.py file represents the improved code. It meets the following three conventions:
- Single Responsibility: The code follows this principle by ensuring that each function has only one specific job. The get_valid_number function is solely responsible for getting input and handling errors, while the math functions (add, subtract, etc.) only perform calculations. This prevents the main program loop from becoming cluttered with details it doesn't need to know about.
- Separation of Concerns: The code separates the "business logic" (the math) from the "user interface" (the input and print statements). The math functions are pure logic—they take numbers in and return a number. They do not print to the screen or ask for user input. This separation makes the code modular, meaning the math logic could be reused in a different program without modification.
- Document Your Code: The code uses Python docstrings (text inside triple quotes """) to explain what each function does. These act as built-in instruction manuals, explaining the inputs and return values for every function. This ensures that anyone reading the code can understand the purpose of a function without needing to decipher the specific Python syntax inside it.

## The Bad Version (bad_calculator.py)
The bad_calc.py file represents the original, unstructured code. It violates the three conventions in the following ways:
- Violation of Single Responsibility: This version relies on one massive while loop to do everything. The loop is responsible for displaying the menu, getting user input, checking for errors, performing the math, and printing the results. Because one block of code is trying to handle every single task, the logic is tangled and difficult to isolate if a bug occurs.
- Violation of Separation of Concerns: In this version, the math logic is hard-coded directly inside the user interface print statements (e.g., print(f"... {number1 + number2}")). This means the calculation logic cannot be separated from the display logic. If I wanted to use this calculator code in a web app or a different script, I would have to rewrite it entirely because the math is trapped inside the print command.
- Violation of Documentation: This version contains no docstrings or comments explaining what is happening. A reader has to look at the raw code to figure out that try...except ValueError is being used for input validation or to understand how the division by zero check works. The lack of documentation makes the code harder to scan and understand quickly.
