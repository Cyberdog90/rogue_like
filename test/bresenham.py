from vec2 import Vec2


def bresenham(p0: Vec2, p1: Vec2):
    dx = p1.x - p0.x
    dy = p1.y - p0.y

    x_sign = 1 if dx > 0 else -1
    y_sign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = x_sign, 0, 0, y_sign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, y_sign, x_sign, 0

    delta = 2 * dy - dx
    y = 0

    for x in range(dx + 1):
        yield Vec2(p0.x + x * xx + y * yx, p0.y + x * xy + y * yy)
        if delta >= 0:
            y += 1
            delta -= 2 * dx
        delta += 2 * dy
