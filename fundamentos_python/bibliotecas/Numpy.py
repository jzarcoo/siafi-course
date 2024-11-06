import numpy as np

arr1D = np.array([1, 2, 3, 4, 5])
print(arr1D)

arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2D)

arr_zeros = np.zeros((2, 3))
print(arr_zeros)

arr_ones = np.ones((2, 3))
print(arr_ones)

arr_square = np.full((2, 2), 7)
print(arr_square)

arr1D_2 = arr1D ** 2
print(arr1D_2)
arr1D = np.square(arr1D_2)
print(arr1D)
arr1D_2 = arr1D + 1
print(arr1D_2)

arr1D = arr1D_2 % 2 == 0
print(arr1D)
print(arr1D[1])

partir = arr1D[1:4] # inicio:fin+1
print(partir)


numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Promedio
mean = np.mean(numbers)
print(f'Mean: {mean}')

# Desviación estándar
std = np.std(numbers)
print(f'Standard deviation: {std}')