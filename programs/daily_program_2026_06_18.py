# Automatically generated daily program
# Date: 2026-06-18 18:14:10

import random

def simulate_guessing_game():
    target = random.randint(1, 100)
    print(f"Target number is {target}")
    attempts = 0
    while True:
        guess = random.randint(1, 100)
        attempts += 1
        if guess == target:
            print(f"Guessed {target} correctly in {attempts} attempts!")
            break
        elif attempts > 1000:
            print("Took too many attempts.")
            break

if __name__ == "__main__":
    simulate_guessing_game()
