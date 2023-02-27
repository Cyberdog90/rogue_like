import curses
from random import randint


def main():
    game = Game()
    while game.input() != 27:
        game.update()
    del game


class Game:
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.refresh()
        curses.noecho()
        curses.curs_set(False)
        curses.resize_term(24, 80)
        self.key: int | None = None

    def input(self):
        self.key = self.screen.getch()
        return self.key

    def update(self):
        self.screen.addstr(0, 0, chr(randint(65, 65 + 26)))
        self.screen.refresh()

    def __del__(self):
        self.screen.keypad(False)
        curses.endwin()
        curses.curs_set(True)


if __name__ == '__main__':
    main()
