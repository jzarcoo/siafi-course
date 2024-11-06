"""
    Determine the sign of a number

    Args:
        num (int): The number to check

    Returns:
        str: 'positive' if the number is positive
             'negative' if the number is negative
             'zero' if the number is zero
"""
def sign(num: int) -> str:
    if num > 0:
        return 'positive'
    elif num < 0:
        return 'negative'
    return 'zero'

"""
    Determine the parity of a number

    Args:
        num (int): The number to check

    Returns:
        str: 'even' if the number is even
             'odd' if the number is odd
"""
def parity(num: int) -> str:
    return 'even' if num % 2 == 0 else 'odd'

"""
    Analyze a number

    Args:
        num (int): The number to analyze
"""
def analyze_number(num: int) -> None:
    print(f'The number is {sign(num)} and {parity(num)}')

"""
    Ask the user for a number

    Returns:
        int: The number entered by the user
"""
def ask_number() -> int:
    while True:
        try:
            return int(input('Enter a number: '))
        except ValueError:
            print('The value entered is not a number')

"""
    Main function
"""
def main() -> None:
    number: int = ask_number()
    analyze_number(number)

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