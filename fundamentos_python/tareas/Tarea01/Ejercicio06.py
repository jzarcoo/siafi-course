# Generics
from typing import List, TypeVar

# Type variable for numbers
T = TypeVar('T', int, float)

# Custom exception
"""
    Exception for division by zero
"""
class MyExceptionError(ZeroDivisionError):
    """
        Constructor
    """
    def __init__(self) -> None:
        super().__init__('Division by zero is not allowed')    

"""
    Calculate the arithmetic mean of a list of numbers, ignoring the negative numbers

    Args:
        numbers (List[T]): The list of numbers

    Returns:
        T: The arithmetic mean of the list
"""
def arithmetic_mean(numbers: List[T]) -> T:
    if len(numbers) == 0:
        raise MyExceptionError
    length: int = 0
    result: T = 0
    # filter returns an iterator
    for i in filter(lambda x: x >= 0, numbers):
        result += i
        length += 1
    return result / length


"""
    Main function
"""
def main() -> None:
    numbers: List[T] = [ 20, 50, -12, 6, -60, -5, 8, -14, 80, 90, -56, 50 ]
    try:
        result: T = arithmetic_mean(numbers)
    except MyExceptionError as e:
        print(e)
    else:
        print(f'The arithmetic mean is {result}')

"""
    Entry point
"""
if __name__ == '__main__':
    main()