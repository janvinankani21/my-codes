import random
import datetime
import os

TEMPLATES = [
    # 1. Simple Calculator
    '''def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

if __name__ == "__main__":
    print("Simple Calculator")
    print("5 + 3 =", add(5, 3))
    print("10 - 2 =", subtract(10, 2))
    print("4 * 4 =", multiply(4, 4))
    print("20 / 5 =", divide(20, 5))
''',
    
    # 2. Fibonacci Sequence
    '''def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    print("Fibonacci Sequence (first 10 numbers):")
    print(fibonacci(10))
''',
    
    # 3. Random Password Generator
    '''import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Generated Password:")
    print(generate_password())
''',

    # 4. Palindrome Checker
    '''def is_palindrome(text):
    text = str(text).lower().replace(" ", "")
    return text == text[::-1]

if __name__ == "__main__":
    words = ["radar", "hello", "A man a plan a canal Panama", "python"]
    for word in words:
        print(f"'{word}' is palindrome? {is_palindrome(word)}")
''',

    # 5. Number Guessing Game (Simulation)
    '''import random

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
''',

    # 6. Basic To-Do List Manager
    '''class TodoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            
    def display(self):
        for i, t in enumerate(self.tasks):
            status = "[x]" if t["done"] else "[ ]"
            print(f"{i}. {status} {t['task']}")

if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Learn Python")
    todo.add_task("Automate GitHub Push")
    todo.mark_done(1)
    print("My Tasks:")
    todo.display()
''',

    # 7. Dictionary/Word Counter
    '''def count_words(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

if __name__ == "__main__":
    sample_text = "hello world hello python python is great"
    print("Word Counts:")
    for word, count in count_words(sample_text).items():
        print(f"{word}: {count}")
'''
]

def main():
    # Ensure a 'programs' directory exists
    os.makedirs("programs", exist_ok=True)
    
    # Generate timestamped filename
    today = datetime.datetime.now().strftime("%Y_%m_%d")
    filename = f"programs/daily_program_{today}.py"
    
    # Pick a random template
    selected_code = random.choice(TEMPLATES)
    
    # Write to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Automatically generated daily program\n")
        f.write(f"# Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(selected_code)
        
    print(f"Successfully generated and saved {filename}")

if __name__ == "__main__":
    main()
