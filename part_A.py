"""

TECH2 mandatory assignment - Part A

"""

from math import sqrt
import numpy as np

# Example list of numbers for testing the standard deviation functions
num_lst = [1, 2, 3, 4, 5]
x = num_lst

# Function to compute the standard deviation using loops
def std_loops(x):
    
    N = len(x)
    
    #1-Compute the mean
    total_sum = 0
    for num in x:
        total_sum += num
    mean = total_sum / N
    
    #2-Compute the mean of square
    sum_of_squares = 0
    for num in x:
        sum_of_squares += num ** 2
    mean_of_squares = sum_of_squares / N
    
    #3-Compute the variance
    variance = mean_of_squares - mean ** 2
    
    #4-Compute the standard deviation
    standard_deviation = sqrt(variance)
    
    return standard_deviation

#Calculate the standard deviation using Python's built-in functions len() and sum()
def std_builtin(x):

    N = len(x)
    
    #1-Comput the mean
    mean = sum(x) / N
    
    #2-Compute the mean of squares
    mean_of_squares = sum([num ** 2 for num in x]) / N
    
    #3-Compute the variance
    variance = mean_of_squares - mean ** 2
    
    # 4-Compute the standard deviation
    standard_deviation = sqrt(variance)
    
    return standard_deviation

# Calculate the standard deviation using NumPy's built-in function
def std_numpy(x):
    return np.std(x)

#Print the result
result_loops = std_loops(x)
result_builtin = std_builtin(x)
result_numpy = std_numpy(x)

print(f"Standard Deviation using loops: {result_loops}")
print(f"Standard Deviation using builtin: {result_builtin}")
print(f"Standard Deviation using numpy: {result_numpy}")

# Check if all three methods produce the same result
if std_loops(x) == std_builtin(x) == std_numpy(x):
    print("All three calculated the same standard deviation for num_lst")