# Exercise 2. Create a 3x3 matrix with values ​​of 0 and another with values ​​of 1.
import numpy as np

"""
    Create a 3x3 matrix with values of n

    Args:
        n: Value to fill the matrix with
"""
def create_matrix(n: int) -> None:
    matrix = np.full((3, 3), n)
    print(f'Matrix with values of {n}:')
    print(matrix)

"""
    Main function.
"""
def main() -> None:
    create_matrix(0)
    create_matrix(1)

"""
    Entry point for the script.
"""
if __name__ == '__main__':
    main()