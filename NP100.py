class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f"({self.x}, {self.y})")

    def __add__(self, Coordinate1):
        return Coordinate(self.x + Coordinate1.x, self.y + Coordinate1.y)


x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

c1 = Coordinate(x1, y1)
c2 = Coordinate(x2, y2)

c = c1.__add__(c2)
c.__str__()
