from __future__ import annotations # This import must occur at the beginning of the file
from abc import ABC, abstractmethod # ABS stands for Abstract Base Class

"""
    The Operation interface declares a method for calculating the operation
"""
class Operation(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

"""
    The Sum class implements the Operation interface
"""
class Sum(Operation):

    """
        Calculate the sum of two numbers

        Args:
            a (T): The first number
            b (T): The second number

        Returns:
            T: The sum of the two numbers
    """
    def calculate(self, a, b):
        return a + b

"""
    The Subtraction class implements the Operation interface
"""
class Subtraction:

    """
        Calculate the subtraction of two numbers

        Args:
            a (T): The first number
            b (T): The second number

        Returns:
            T: The subtraction of the two numbers
    """
    def calculate(self, a, b):
        return a - b
    
"""
    The Multiplication class implements the Operation interface
"""
class Multiplication(Operation):

    """
        Calculate the multiplication of two numbers

        Args:
            a (T): The first number
            b (T): The second number

        Returns:
            T: The multiplication of the two numbers
    """
    def calculate(self, a, b):
        return a * b

"""
    The Division class implements the Operation interface
"""
class Division(Operation):

    """
        Calculate the division of two numbers

        Args:
            a (T): The first number
            b (T): The second number

        Returns:
            T: The division of the two numbers
        
        Raises:
            ZeroDivisionError: If the second number is zero
    """
    def calculate(self, a, b):
        if b == 0:
            raise ZeroDivisionError('Division by zero is not allowed')
        return a / b
    
"""
    The Calculator class
"""
class Calculator:

    """
        Constructor

        Args:
            operation (Operation): The operation to perform
    """
    def __init__(self, operation: Operation):
        self._operation = operation


    """
        Getter for the operation property

        Returns:
            Operation: The operation to perform
    """
    @property
    def operation(self) -> Operation:
        return self._operation
    
    """
        Setter for the operation property

        Args:
            operation (Operation): The operation to perform
    """
    @operation.setter
    def operation(self, operation: Operation) -> None:
        self._operation = operation

    """
        Calculate the operation

        Args:
            a (T): The first number
            b (T): The second number

        Returns:
            T: The result of the operation
    """
    def calculate(self, a, b):
        return self._operation.calculate(a, b)
    
"""
    Ask the user for a number

    Args:
        numero (str): The number to ask

    Returns:
        float: The number entered by the user
"""
def ask_number(numero: str) -> float:
    while True:
        try:
            return float(input(f'Enter a number ({numero}): '))
        except ValueError:
            print('The value entered is not a number')

"""
    Ask the user for an operation

    Returns:
        str: The operation entered by the user
"""
def ask_operation() -> str:
    while True:
        operation = input('Enter the operation (+, -, *, /): ')
        if operation in '+-*/':
            return operation
        print('Invalid operation')
    
"""
    Main function
"""
def main() -> None:
    operations = {
        '+': Sum(),
        '-': Subtraction(),
        '*': Multiplication(),
        '/': Division()
    }
    calculator = Calculator(operations['+']) # Default operation
    flag = True
    while flag:
        try:
            a = ask_number('A')
            op = ask_operation()
            b = ask_number('B')
            calculator.operation = operations[op]
            result = calculator.calculate(a, b)
        except ZeroDivisionError as e:
            print(e)
        else:
            print(f'The result is {result}')
        flag = input('Do you want to continue? (yes/no): ') == 'yes'


"""
    Entry point
"""
if __name__ == '__main__':
    try:
        main()
    except EOFError: # Ctrl + D
        print('Bye')
    except KeyboardInterrupt: # Ctrl + C
        print('Bye')