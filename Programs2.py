#guess the number
import random

secret = random.randint(1,20)

while True:
    guess = int(input('enter number to guess: '))

    if guess == secret:
        print('successful')
        break
    elif guess < secret:
        print('too low')
    else:
        print('too high')
    

