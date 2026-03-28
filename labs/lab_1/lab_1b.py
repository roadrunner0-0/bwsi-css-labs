"""
lab_1b.py

This is a script that implements a simple calculator.
It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

import sys


def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation,
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform
        ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation." 
        "Please choose from 'add', 'subtract', " 
        "'multiply', or 'divide'.")


def main():
    
    print("===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = input("Enter the first number: ")
    try:
        num1 = float(num1)
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
        main()  # Restart the main function to get valid input
    num2 = input("Enter the second number: ")
    try:
        num2 = float(num2)
    except ValueError:
        print(
            "Invalid input. Please enter a valid number.\n")
        main()  # Restart the main function to get valid input
    operation = input(
        "Enter the operation (add, subtract, multiply, divide):"
        ).strip().lower()
    if operation not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid operation. Please choose from"
              " 'add', 'subtract', 'multiply', or 'divide'.")
    
        main()  # Restart the main function to get valid input
    # Perform the calculation and display the result
    else:
        result = simple_calculator(operation, num1, num2)
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
        sys.exit(0)  # Exit the program after displaying the result


if __name__ == "__main__":
    main()
