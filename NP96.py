from math import pi


rs = [1, 2, 4, 9, 10, 13]

def squ(r):
    return 4*pi*r**2

for i in rs:
    print(round(squ(i),2))
    
