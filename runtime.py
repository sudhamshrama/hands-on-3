import time

def f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

# Test the function and measure runtime
n = 1000  # Change the value of n as needed
start_time = time.time()
result = f(n)
end_time = time.time()

print("Result:", result)
print("Runtime:", end_time - start_time, "seconds")

n = 100  # Change the value of n as needed
start_time = time.time()
result = f(n)
end_time = time.time()

print("Result:", result)
print("Runtime:", end_time - start_time, "seconds")

n = 9758  # Change the value of n as needed
start_time = time.time()
result = f(n)
end_time = time.time()

print("Result:", result)
print("Runtime:", end_time - start_time, "seconds")
