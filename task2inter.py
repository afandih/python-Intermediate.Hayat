import numpy as np


# TASK 1: The Power of Vectorization

matrix = np.random.randint(1, 101, (5, 5))

new_matrix = (matrix * 10) + 5

matrix_mean = np.mean(new_matrix)

print("--- TASK 1: VECTORIZATION ---")
print(f"Original Random Matrix:\n{matrix}")
print(f"Processed Matrix (x10 + 5):\n{new_matrix}")
print(f"Mean of the new matrix: {matrix_mean:.2f}\n")

#TASK 2: The Stretching Logic (Broadcasting)

row_to_add = np.array([1, 2, 3, 4, 5])

broadcasted_result = new_matrix + row_to_add

print("--- TASK 2: BROADCASTING ---")
print(f"1D Array to add: {row_to_add}")
print(f"Result after broadcasting (row added to every row of matrix):\n{broadcasted_result}\n")


