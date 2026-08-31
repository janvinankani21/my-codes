# Automatically generated daily program
# Date: 2026-08-31 20:57:03

def is_palindrome(text):
    text = str(text).lower().replace(" ", "")
    return text == text[::-1]

if __name__ == "__main__":
    words = ["radar", "hello", "A man a plan a canal Panama", "python"]
    for word in words:
        print(f"'{word}' is palindrome? {is_palindrome(word)}")
