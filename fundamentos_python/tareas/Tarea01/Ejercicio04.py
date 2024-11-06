from typing import List

"""
    Generate a multiplication table for a given number

    Args:
        number (int): The number to generate the multiplication table

    Returns:
        List[int]: The multiplication table for the given number
"""
def multiplication_table(number: int) -> List[int]:
    return [number * i for i in range (1, 11)]

"""
    Ask the user for a number

    Returns:
        int: The number entered by the user
"""
def ask_number() -> int:
    try:
        return int(input('Enter a number: '))
    except ValueError:
        print('The value entered is not a number')
        return ask_number()

"""
    Main function
"""
def main() -> None:
    number: int = ask_number()
    for n in multiplication_table(number):
        print(n)

"""
    Entry point
"""
if __name__ == '__main__':
    main()