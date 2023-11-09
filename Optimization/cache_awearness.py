# Created by Su Myat Phyoe at 11:37 pm 9/11/2023 using PyCharm
import timeit
import numpy as np

def sum_matrix_naive(matrix):
    """Naive summation of matrix elements."""
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    return total_sum

def sum_matrix_cache_aware(matrix):
    """Cache-aware summation of matrix elements."""
    total_sum = 0
    rows, cols = len(matrix), len(matrix[0])

    for j in range(cols):
        for i in range(rows):
            total_sum += matrix[i][j]

    return total_sum

# Generate a random matrix for testing
matrix_size = 1000
test_matrix = np.random.randint(1, 10, size=(matrix_size, matrix_size)).tolist()

# Measure execution time for naive summation
naive_time = timeit.timeit(lambda: sum_matrix_naive(test_matrix), number=100)
print(f"Naive Summation Time: {naive_time:.6f} seconds")

# Measure execution time for cache-aware summation
cache_aware_time = timeit.timeit(lambda: sum_matrix_cache_aware(test_matrix), number=100)
print(f"Cache-Aware Summation Time: {cache_aware_time:.6f} seconds")


