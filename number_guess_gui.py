import tkinter as tk
import random

# ----- game state -----
secret_number = random.randint(1, 100)
tries = 0

# ----- actions -----
def check_guess():
    global tries, secret_number
    text = guess_entry.get().strip()