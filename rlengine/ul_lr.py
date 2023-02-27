from rlengine.vec2 import Vec2YX


class ULLR:
    def __init__(self, ul: Vec2YX, lr: Vec2YX):
        self.__ul = ul
        self.__lr = lr

    @property
    def ul(self) -> Vec2YX:
        return self.__ul

    @property
    def lr(self) -> Vec2YX:
        return self.__lr

    @property
    def ur(self) -> Vec2YX:
        return Vec2YX(y_x=(self.ul.y, self.lr.x))

    @property
    def ll(self) -> Vec2YX:
        return Vec2YX(y_x=(self.lr.y, self.ul.x))
