import random

word_list = ['python', 'hangman', 'challenge', 'programming', 'github']

chosen_word = random.choice(word_list)
print("The secret word (for now):", chosen_word)  

#display
display = []
for letter in chosen_word:
    display.append('_')

print("Welcome to Hangman!")
print(" ".join(display))

#guess
guess = input("Guess a letter: ").lower()

# Reveal the guessed letter in the correct position(s)
for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        display[position] = guess

print(" ".join(display))