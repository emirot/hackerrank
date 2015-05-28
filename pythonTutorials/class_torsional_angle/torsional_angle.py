__author__ = 'nolanemirot'

import math

class Point():

    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        xx =  self.x - other.x
        yy =  self.y - other.y
        zz =  self.z - other.z
        return Point(xx, yy, zz)

    def __mul__(self, other):
        xx = self.y * other.z - self.z * other.y
        yy = self.z * other.x - self.x * other.z
        zz = self.x * other.y - self.y * other.x
        return Point(xx, yy, zz)

    def dot(self, other):
        xx = self.x * other.x
        yy = self.y * other.y
        zz = self.z * other.z
        return xx + yy + zz

    def absolute_val(self):
        return math.sqrt(self.x **2 + self.y **2 + self.z ** 2)


if __name__ == '__main__':
    ax ,ay, az = map(float, input().split())
    a = Point(ax, ay, az)
    bx ,by, bz = map(float, input().split())
    b = Point(bx, by, bz)
    cx , cy, cz = map(float, input().split())
    c = Point(cx, cy, cz)
    cx , cy, cz = map(float, input().split())
    d = Point(cx, cy, cz)


    X = (b - a) * (c - b)
    Y = (c - b) * (d - c)


    A = X * Y
    XX = X.absolute_val()
    YY = Y.absolute_val()
    res = (X.dot(Y)) / (XX * YY)

    res = math.acos(res)
    print("%.2f" % math.degrees(res))






