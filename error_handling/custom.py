# Created by Su Myat Phyoe at 10:44 pm 7/11/2023 using PyCharm

class CustomError(Exception):
    """Custom exception to indicate a specific error condition."""

    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(self.message)


def divide_numbers(a, b):
    """Divide two numbers and raise a custom exception for specific error conditions."""
    if b == 0:
        raise CustomError("Cannot divide by zero")
    elif not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise CustomError("Invalid input. Both numbers must be numeric")

    return a / b


# Example usage
try:
    result = divide_numbers(10, 0)
    print(f"Result: {result}")
except CustomError as e:
    print(f"Error: {e}")
