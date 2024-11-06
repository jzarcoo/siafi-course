"""
    Calculate the sum of all the numbers from 0 to n

    Args:
        n (int): The last number to sum

    Returns:
        int: The sum of all the numbers from 0 to n
"""
def sum_from_one_to(n):
    return n * (n + 1) >> 1

"""
    Ask the user for a number
    
    Returns:
        int: The number entered by the user
"""
def ask_number():
    while True:
        try:
            return int(input('Enter a number: '))
        except ValueError:
            print('The value entered is not a number')

"""
    Main function
"""
def main():
    number: int = ask_number()
    print(f'The sum of all the numbers from 1 to {number} is {sum_from_one_to(number)}')

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
