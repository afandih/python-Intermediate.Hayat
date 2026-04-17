import numpy as np
#Task1: The Architect (Array Creation)

matrix = np.arange(1, 17).reshape(4, 4)

print("___Task1: The Architect___")
print("Original 4x4 Matrix:")
print(np.matrix)
print(f"Shape:{np.matrix.dtype}\n")

#Task2: (The Data slicing)

rows_extracted = np.matrix[1:3, :]
last_col = matrix[:, -1]

sub_square = matrix[-2:, -2:]
print("___task2:The data slicing___")
print(f"Extracted rows (2 & 3):\n{rows_extracted}") # type: ignore
print(f"last Column: {last_col}")
print(f"Bottom-Right 2x2 Sub-square:\n{sub_square}\n")

#Task3: Engineering Analysis
# Verifivation Test 
sub_square[1, 1] = 999
print("---Task3:verification---")
print("Matrix after modifying the sub-square view (index[3,3] should be 999):")
print(np.matrix)