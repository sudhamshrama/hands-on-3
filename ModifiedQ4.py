import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def modified_f(n):
    x = 1
    y = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
            y = i + j
    return x

# Define the range of n values
n_values = range(1, 1001)  # From n = 1 to n = 1000

# Measure runtime for each n value
runtimes_modified = []
for n in n_values:
    start_time = time.time()
    result = modified_f(n)
    end_time = time.time()
    runtimes_modified.append(end_time - start_time)

# Plot time vs. n
plt.plot(n_values, runtimes_modified, label='Modified Runtime', marker='o', linestyle='-')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Modified Runtime vs. n')
plt.legend()
plt.grid(True)
plt.show()
