import re

s = input()
result = re.sub(r"[^x(\d)]", "", s)
print(result)
