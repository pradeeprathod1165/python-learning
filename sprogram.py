n = int(input("Enter how many terms: "))
a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#clock
import time

while True:
    current_time = time.strftime("%H:%M:%S")
    print("⏰ Time:", current_time, end="\r")  # overwrite same line
    time.sleep(1)
