"""
    Check if a number is even or odd

    Args:
        number (float): The number to check

    Returns:
        str: The result of the check
"""
def even_or_odd(number: float) -> str:
    return 'even' if number % 2 == 0 else 'odd'

"""
    Ask the user for a number

    Returns:
        float: The number entered by the user
"""
def ask_number() -> float:
    while True:
        try:
            return float(input('Enter a number: '))
        except ValueError:
            print('The value entered is not a number')

"""
    Main function
"""
def main() -> None:
    number: float = ask_number()
    print(f'The number is {even_or_odd(number)}')

"""
    Entry point
"""
if __name__ == '__main__':
    main()