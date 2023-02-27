import curses
from curses import wrapper
from text_color import TextColor
from bresenham import bresenham
from vec2 import Vec2


def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(False)
    file = [line for line in file_loader("map2.txt")]
    tc = TextColor()
    p_x = 40
    p_y = 50
    key = 0
    while key != 27:
        for x in range(-10, 11):
            for y in range(-10, 11):
                if (new_x := p_x + x) >= 0 and (new_y := p_y + y) >= 0:
                    try:
                        char = file[new_x][new_y]
                        seen = set()
                        for pos in bresenham(Vec2(p_x, p_y), Vec2(new_x, new_y)):
                            if file[pos.x][pos.y] == "#":
                                if pos.x == new_x and pos.y == new_y:
                                    seen.add((x + 10, y + 10, "#"))

                                else:
                                    stdscr.addstr(x + 10, y + 10, char, tc.no_color)
                                break
                        else:
                            for i in range(-1, 2):
                                for j in range(-1, 2):
                                    seen.add((x + 10 + i, y + 10 + j, "."))
                    except IndexError:
                        stdscr.addstr(x + 10, y + 10, "#", tc.no_color)
                else:
                    stdscr.addstr(x + 10, y + 10, "#", tc.no_color)
        stdscr.addstr(10, 10, "@", tc.player_color)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            if file[p_x - 1][p_y] != "#":
                p_x -= 1
        if key == curses.KEY_DOWN:
            if file[p_x + 1][p_y] != "#":
                p_x += 1
        if key == curses.KEY_LEFT:
            if file[p_x][p_y - 1] != "#":
                p_y -= 1
        if key == curses.KEY_RIGHT:
            if file[p_x][p_y + 1] != "#":
                p_y += 1
    curses.curs_set(True)


def file_loader(path):
    for line in open(path, "r", encoding="utf-8"):
        yield line.replace("\n", "")


if __name__ == '__main__':
    wrapper(main)
