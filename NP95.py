def f(n):
#   Fibonacci
    if n == 1:
        return 2 
    elif n == 2:
        return  3
    else:
        return f(n-1) + f(n-2)

print(f(int(input())))
