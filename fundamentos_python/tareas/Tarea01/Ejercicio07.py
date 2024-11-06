from typing import List
from collections.abc import Iterator

"""
    Generate an iterator with the odd numbers from a list of numbers

    Args:
        numbers (List[int]): The list of numbers

    Returns:
        Iterator[int]: The iterator with the odd numbers
"""
def odd_numbers(numbers: List[int]) -> Iterator[int]:
    return filter(lambda x: x % 2 != 0, numbers)

"""
    Main function.
"""
def main() -> None:
    numbers: List[int] = [ 11, 47, 96, 8, 5, -43, 91, 0, 41, 38, 33, 10 ]
    for i in odd_numbers(numbers):
        print(i)

"""
    Entry point.
"""
if __name__ == '__main__':
    main()