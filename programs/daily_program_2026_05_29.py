# Automatically generated daily program
# Date: 2026-05-29 21:29:26

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Generated Password:")
    print(generate_password())
