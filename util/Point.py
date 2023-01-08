from dataclasses import dataclass, astuple


@dataclass
class Point:
    x: int
    y: int

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other: int):
        return Point(self.x * other, self.y * other)

    def __hash__(self) -> int:
        return hash(astuple(self))


Point.N = Point(0, 1)
Point.S = Point(0, -1)
Point.E = Point(1, 0)
Point.W = Point(-1, 0)
Point.NW = Point.N + Point.W
Point.NE = Point.N + Point.E
Point.SW = Point.S + Point.W
Point.SE = Point.S + Point.E
