import re

s = input()
# \d表示匹配数字字符，[\d-]*表示匹配任意数量的数字字符或连字符，
r = re.match(r'\d[\d-]*\d', s)  
print(r.group())  # 提取出一部分内容
