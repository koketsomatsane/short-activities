words = ["orange", "book", "banana", "bag", "pineapple"]

words_length = [word.upper() for word in words if len(word)>=4]

print(f"Initial words {words}")
print(f"The filtered words: {words_length}")