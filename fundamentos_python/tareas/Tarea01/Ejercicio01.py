"""
    Compare a number to zero

    Args:
        number (float): The number to compare

    Returns:
        str: 'greater than' if the number is greater than zero
             'less than' if the number is less than zero
             'equal to' if the number is equal to zero
"""
def compare_to_zero(number: float) -> str:
    if number > 0:
        return 'greater than'
    elif number < 0:
        return 'less than'
    return 'equal to'

"""
    Ask the user for a number

    Returns:
        float: The number entered by the user
"""
def ask_number() -> float:
    try:
        return float(input('Enter a number: '))
    except ValueError:
        print('The value entered is not a number')
        return ask_number()

"""
    Main function
"""
def main() -> None:
    number: float = ask_number()
    print(f'The number is {compare_to_zero(number)} zero')

"""
    Entry point
"""
if __name__ == '__main__':
    main()
