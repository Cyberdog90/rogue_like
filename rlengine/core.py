import curses
from random import randint

from rlengine.window.main_window import MainWindow


class Game:
    def __init__(self, main_window: MainWindow):
        self.__screen = curses.initscr()
        self.__window = main_window
        self.__screen.refresh()
        curses.curs_set(False)
        curses.resize_term(main_window.window_size.y, main_window.window_size.x)
        self.__key: int | None = None

    def input(self):
        self.__key = self.__screen.getch()
        return self.__key

    def update(self):
        self.__window.update()

    def __del__(self):
        self.__screen.keypad(False)
        curses.endwin()
        curses.curs_set(True)


if __name__ == '__main__':
    main()
