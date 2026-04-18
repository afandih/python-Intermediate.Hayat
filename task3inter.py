import numpy as np

np.random.seed(42)

#Task: The Summary Report (Aggregation)

data = np.random.randint(1, 101, 20)
 
data_mean = np.mean(data)
data_max = np.max(data)
data_min = np.min(data)

print("---Task1: The Summary Report---")
print(f"Dataset: {data}")
print(f"1. Average (Mean): {data_mean}")
print(f"2. highest Value: {data_max}")
print(f"3. Lowest Value: {data_min}\n")

#Task2: The Logical Filter (Boolean Masking)

above_average_mask = (data % 2 == 0)
even_average = data[above_average_mask]

even_mask = (data %2 == 0)
even_numbers = data[even_mask]

print("--- Task2: The Logical Filter---")
print(f"Boolean Mask (Above Average?):\n{above_average_mask}")
print(f"Values Above Average:\n{above_average_mask}")
print(f"Even Numbers only:\n{even_numbers}\n")
