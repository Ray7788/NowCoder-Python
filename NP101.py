import re

str = input()
result = re.match("https://www", str, re.I)
print(result.span())
