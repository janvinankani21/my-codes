# Automatically generated daily program
# Date: 2026-07-03 16:53:18

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

if __name__ == "__main__":
    print("Simple Calculator")
    print("5 + 3 =", add(5, 3))
    print("10 - 2 =", subtract(10, 2))
    print("4 * 4 =", multiply(4, 4))
    print("20 / 5 =", divide(20, 5))
