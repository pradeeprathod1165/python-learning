import random

word_list = ['python', 'hangman', 'challenge', 'programming', 'github']
chosen_word = random.choice(word_list)

display = ['_'] * len(chosen_word)
lives = 6  # Number of allowed wrong guesses
guessed_letters = set()

print("Welcome to Hangman!")

while '_' in display and lives > 0:
    print("\nWord:", " ".join(display))
    print(f"Lives left: {lives}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"Wrong! '{guess}' is not in the word.")

if '_' not in display:
    print(f"\nCongratulations! You guessed the word: {chosen_word}")
else:
    print(f"\nGame over! The word was: {chosen_word}")