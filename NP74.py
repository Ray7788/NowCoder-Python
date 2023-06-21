words = {
    "a": ["apple", "abandon", "ant"],
    "b": ["banana", "bee", "become"],
    "c": ["cat", "come"],
    "d": "down",
}

new_letter = input()
new_word = input()

words[new_letter] = new_word
print(words)
