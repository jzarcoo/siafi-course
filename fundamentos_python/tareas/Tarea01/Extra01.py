from typing import List

"""
    Generate a Fibonacci sequence of n numbers

    Args:
        n (int): The number of elements in the sequence

    Returns:
        List[int]: The Fibonacci sequence of n numbers
"""
def fibonacci_sequence(n: int) -> List[int]:
    fibo = []
    a, b = 0, 1
    for _ in range(n):
        fibo.append(a)
        a, b = b, a + b
    return fibo

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
    for i in fibonacci_sequence(number):
        print(i)

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