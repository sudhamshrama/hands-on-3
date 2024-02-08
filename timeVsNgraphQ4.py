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
plt.show()

# Calculate upper and lower bounds
upper_bound = fit_curve(n_values)
lower_bound = [0.5 * runtime for runtime in runtimes]

# Plot the upper and lower bounds
plt.figure(figsize=(10, 6))
plt.plot(n_values, runtimes, label='Measured Runtime', marker='o', linestyle='-')
plt.plot(n_values, upper_bound, label='Upper Bound (Polynomial Fit)', color='red', linestyle='--')
plt.plot(n_values, lower_bound, label='Lower Bound (Half of Measured Runtime)', color='green', linestyle='--')

plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime vs. n with Upper and Lower Bounds')
plt.legend()
plt.grid(True)
plt.show()

# Big-O, Big-Omega, Big-Theta
print("Big-O Notation:", "O(n^2)")
print("Big-Omega Notation:", "Ω(n)")
print("Big-Theta Notation:", "Θ(n^2)")
