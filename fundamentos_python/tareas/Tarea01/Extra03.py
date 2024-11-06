"""
    Calculate the factorial of a number

    Args:
        n (int): The number to calculate the factorial

    Returns:
        int: The factorial of the number
"""
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

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
    print(factorial(number))

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
