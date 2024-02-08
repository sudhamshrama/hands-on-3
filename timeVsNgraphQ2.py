import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time

# Function to measure runtime
def f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

# Define the range of n values
n_values = np.arange(1, 1001)  # From n = 1 to n = 1000

# Measure runtime for each n value
runtimes = []
for n in n_values:
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    runtimes.append(end_time - start_time)

# Fit a polynomial to the data
fit_coefficients = np.polyfit(n_values, runtimes, 2)
fit_curve = np.poly1d(fit_coefficients)

# Plot the measured runtime and the fitted polynomial
plt.figure(figsize=(10, 6))
plt.plot(n_values, runtimes, label='Measured Runtime', marker='o', linestyle='-')
plt.plot(n_values, fit_curve(n_values), label='Fitted Polynomial', color='red', linestyle='--')

plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime vs. n')
plt.legend()
plt.grid(True)

# Find approximate location of n_0 (where deviation starts)
n_0 = 50  # Update this value based on visual inspection
runtime_at_n_0 = runtimes[n_0 - 1]  # Subtract 1 because indexing starts from 0
plt.annotate('n_0', xy=(n_0, runtime_at_n_0), xytext=(n_0 + 50, runtime_at_n_0 + 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()
