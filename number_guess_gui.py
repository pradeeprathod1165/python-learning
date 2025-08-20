import tkinter as tk
import random

# ----- game state -----
secret_number = random.randint(1, 100)
tries = 0

# ----- actions -----
def check_guess():
    global tries, secret_number
    text = guess_entry.get().strip()


     # validate
    try:
        guess = int(text)
    except ValueError:
        result_label.config(text="Please enter a whole number.")
        return

    if not (1 <= guess <= 100):
        result_label.config(text="Enter a number between 1 and 100.")
        return

    tries += 1
    status_label.config(text=f"Attempts: {tries}")

    if guess < secret_number:
        result_label.config(text="Too low ❌")
    elif guess > secret_number:
        result_label.config(text="Too high ❌")
    else:
        result_label.config(text=f"🎉 Correct! It was {secret_number}.")
        check_btn.config(state="disabled")

    guess_entry.delete(0, tk.END)
    guess_entry.focus()

def new_game():
    global secret_number, tries
    secret_number = random.randint(1, 100)
    tries = 0
    result_label.config(text="")
    status_label.config(text="Attempts: 0")
    check_btn.config(state="normal")
    guess_entry.delete(0, tk.END)
    guess_entry.focus()