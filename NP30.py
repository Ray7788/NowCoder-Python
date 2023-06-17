queue = [1, 2, 3, 4, 5]
num = int(input())

for i in range(3):
    if i <2:
        queue.pop(0)
        print(queue)
    else:
        queue.append(num)
        print(queue)
