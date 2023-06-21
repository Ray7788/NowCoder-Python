num = int(input())
matr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    
for i in matr:
    for j in range(len(i)):
        i[j] = i[j] * num

print(matr) 
