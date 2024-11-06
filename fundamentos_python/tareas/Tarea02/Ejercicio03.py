# Exercise 3. Given an array of 10 elements, select the values ​​that are greater than 5.
# Replace values ​​greater than 8 with 0.
import numpy as np

"""
    Main function.
"""
def main() -> None:
    # default_rng. Construct a new Generator with the default BitGenerator (PCG64).
    generator: np.random.Generator = np.random.default_rng(12345)
    # integers. Return random integers from low (inclusive) to high (exclusive).
    numbers: np.ndarray = generator.integers(0, 11, size=10)

    print(f'Original numbers: {numbers}')

    gretter_than_five: np.ndarray = numbers[numbers > 5]
    print(f'Numbers greater than 5: {gretter_than_five}')
    
    numbers[numbers > 8] = 0
    print(f'Numbers greater than 8 replaced with 0: {numbers}')

"""
    Entry point for the script.
"""
if __name__ == '__main__':
    main()