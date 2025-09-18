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


#done
    password = input("Enter your password: ")
    
    length = len(password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)
    
    if length < 6:
        print("Weak password ❌")
    elif length >= 6 and has_digit and has_special:
        print("Strong password 💪")
    else:
        print("Medium strength ⚡")
