#1. Fibonacci Series (using loop)
# Fibonacci series up to n terms
n = 10
a, b = 0, 1

print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
