word = input()
a = []
b = []
for i in word:
    j = word.count(i)
    a.append(i)
    b.append(j)

print(dict(zip(a,b)))
