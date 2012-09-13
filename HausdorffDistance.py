import math

#Brute Force O(mn)
def H(points1, points2):
    h = 0
    for a in points1:
        shortest = float('Inf')
        for b in points2:
            d = a.EuclDistance(b)
            if d < shortest:
                shortest = d
        if shortest > h:
            h = shortest
    return h

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" +str(self.x)+","+str(self.y)+")"

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def length(self):
        return math.sqrt(self.x*self.x + self.y *self.y)

    def EuclDistance(self, other):
        return (other-self).length()


poly1 = [
        Point2D( 1, -1),
        Point2D( 1,  1),
        Point2D(-1,  1),
        Point2D(-1 ,-1)
    ]

#left lower edge has longest distance
poly2 = [
        Point2D( 1.5, -1.5),
        Point2D( 1.5,  1.5),
        Point2D(-1.5,  1.5),
        Point2D(-1.6, -1.6)
    ]


print(poly1)
print(poly2)

h = H(poly1, poly2)
expectedH = poly1[3].EuclDistance(poly2[3])

print(h, h == expectedH )

