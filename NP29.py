stack = [1, 2, 3, 4, 5]
int1 = int(input())

for i in range(2):
    stack.pop(len(stack)-1)
    print(stack)

stack.append(int1)
print(stack)
