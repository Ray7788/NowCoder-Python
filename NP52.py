x = input().split()
s = 0
for i in x:
    s = s + int(i)
print(s, "{:.1f}".format(s/len(x)))
