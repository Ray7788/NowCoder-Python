dict = {
    "a": ["apple", "abandon", "ant"],
    "b": ["banana", "bee", "become"],
    "c": ["cat", "come"],
    "d": "down",
}
letter = input()
for i in dict[letter]:
    print(i, end=" ")
