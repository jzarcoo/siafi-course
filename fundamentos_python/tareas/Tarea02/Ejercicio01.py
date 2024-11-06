# Exercise 1. Create a one-dimensional array with the numbers 0 to 9 and find the maximum, minimum, and average number of values ​​in the array.
import numpy as np

"""
    Main function.
"""
def main() -> None:
    # arange. Return evenly spaced values within a given interval.
    numbers: np.ndarray = np.arange(10)
    max_number: int = np.max(numbers)
    min_number: int = np.min(numbers)
    mean: float = np.mean(numbers)
    print(f'Numbers: {numbers}')
    print(f'Max: {max_number}')
    print(f'Min: {min_number}')
    print(f'Mean: {mean}')

"""
    Entry point of the program.
"""
if __name__ == '__main__':
    main()