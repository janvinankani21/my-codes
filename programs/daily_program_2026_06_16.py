# Automatically generated daily program
# Date: 2026-06-16 19:01:56

def count_words(text):
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
