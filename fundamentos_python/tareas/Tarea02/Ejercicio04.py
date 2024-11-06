# Exercise 4. Create two 3x3 matrices with random integers and perform addition, subtraction and multiplication operations on the matrices.
import numpy as np

MAX_INT: int = np.iinfo(np.int32).max
MIN_INT: int = np.iinfo(np.int32).min

"""
    Main function.
"""
def main() -> None:
    generator: np.random.Generator = np.random.default_rng(12345)
    numbers1: np.ndarray = generator.integers(MIN_INT, MAX_INT, size=(3, 3))
    numbers2: np.ndarray = generator.integers(MIN_INT, MAX_INT, size=(3, 3))
    print(f'Matrix 1:\n{numbers1}')
    print(f'Matrix 2:\n{numbers2}')

    print(f'Sum:\n{numbers1 + numbers2}')
    print(f'Subtraction:\n{numbers1 - numbers2}')
    print(f'Multiplication:\n{numbers1 * numbers2}')

"""
    Entry point for the script.
"""
if __name__ == '__main__':
    main()