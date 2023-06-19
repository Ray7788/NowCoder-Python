table = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0}
lst_x = []
lst_y = []

while True:
    level = input()
    if level == 'False':
        break
    point = int(input())
    total = point * table[level]
    lst_x.append(total)
    lst_y.append(point)

print("{:.2f}".format(sum(lst_x) / sum(lst_y)))
