import time

def modified_f(n):
    x = 1
    y = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
            y = i + j
    return x

# Test the modified function and measure runtime
n = 1000  # Change the value of n as needed
start_time = time.time()
result = modified_f(n)
end_time = time.time()

print("Result:", result)
print("Modified Runtime:", end_time - start_time, "seconds")
