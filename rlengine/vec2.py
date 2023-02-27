from math import ceil, floor, sqrt
from typing import Tuple

__all__ = ["Vec2YX"]


class Vec2YX:
    def __init__(self, y_x: Tuple[int | float]) -> None:
        self.x = y_x[1]
        self.y = y_x[0]

    def distance(self, other: "Vec2YX") -> float:
        return sqrt(
            (self.y - other.y) * (self.y - other.y) +
            (self.x - other.x) * (self.x - other.x)
        )

    def int(self) -> "Vec2YX":
        return Vec2YX((int(self.y), int(self.x)))

    def float(self) -> "Vec2YX":
        return Vec2YX((float(self.y), float(self.x)))

    def tuple(self) -> tuple:
        return self.y, self.x

    def __pos__(self) -> "Vec2YX":
        return Vec2YX((self.y, self.x))

    def __neg__(self) -> "Vec2YX":
        return Vec2YX((-self.y, -self.x))

    def __add__(self, other: "Vec2YX") -> "Vec2YX":
        return Vec2YX((self.y + other.y, self.x + other.x))

    def __sub__(self, other: "Vec2YX") -> "Vec2YX":
        return Vec2YX((self.y - other.y, self.x - other.x))

    def __mul__(self, other: "Vec2YX") -> "Vec2YX":
        return Vec2YX((self.y * other.y, self.x * other.x))

    def __truediv__(self, other: "Vec2YX") -> "Vec2YX":
        return Vec2YX((self.y / other.y, self.x / other.x))

    def __iadd__(self, other: "Vec2YX") -> "Vec2YX":
        self.y += other.y
        self.x += other.x
        return self

    def __isub__(self, other: "Vec2YX") -> "Vec2YX":
        self.y -= other.y
        self.x -= other.x
        return self

    def __imul__(self, other: "Vec2YX") -> "Vec2YX":
        self.y *= other.y
        self.x *= other.x
        return self

    def __itruediv__(self, other: "Vec2YX") -> "Vec2YX":
        self.y /= other.y
        self.x /= other.x
        return self

    def __abs__(self) -> "Vec2YX":
        return Vec2YX((abs(self.y), abs(self.x)))

    def __ceil__(self) -> "Vec2YX":
        return Vec2YX((ceil(self.y), ceil(self.x)))

    def __floor__(self) -> "Vec2YX":
        return Vec2YX((floor(self.y), floor(self.x)))

    def __repr__(self) -> str:
        return f" y -> {self.y}, x -> {self.x}"

    def __eq__(self, other: "Vec2YX") -> bool:
        return self.y == other.y == self.x == other.x

    def __ne__(self, other: "Vec2YX") -> bool:
        return self.y != other.y or self.x != other.x
