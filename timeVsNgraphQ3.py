import time
import numpy as np
import matplotlib.pyplot as plt

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
    
print(runtimes)
# Plot time vs. n
plt.plot(n_values, runtimes, label='Measured Runtime', marker='o', linestyle='-')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime vs. n')
plt.legend()
plt.grid(True)
plt.show()
