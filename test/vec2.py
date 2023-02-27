class Vec2:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f"{{x -> {self.__x}, y -> {self.__y}}}"

    def __add__(self, other: "Vec2"):
        return Vec2(self.__x + other.__x, self.__y + other.__y)

    def __iadd__(self, other: "Vec2"):
        self.__x += other.__x
        self.__y += other.__y

    def __sub__(self, other: "Vec2"):
        return Vec2(self.__x - other.__x, self.__y - other.__y)

    def __isub__(self, other: "Vec2"):
        self.__x -= other.__x
        self.__y -= other.__y

    def __call__(self, *args, **kwargs):
        return [self.__y][self.__x]
