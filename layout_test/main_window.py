from typing import Dict

import curses
from test_sub_window import TestSubWindow
from itertools import accumulate


class MainWindow:
    def main(self, stdscr) -> None:
        stdscr.clear()
        stdscr.refresh()
        curses.curs_set(False)
        stdscr.refresh()

        while (key := stdscr.getch()) != 27:
            pass

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        curses.curs_set(True)

    def __init__(self) -> None:
        curses.initscr()

        test_sub_window = TestSubWindow()
        print(test_sub_window.windows)


        # self.active_window_system = sub_window01.windows["test_window"]
        # self.sub_windows = [sub_window01]

    def check_overlap(self):
        for y in range(len(game_map)):
            game_map[y] = list(accumulate(game_map[y]))

        for y in range(len(game_map[0])):
            for x, e in enumerate(accumulate([game_map[i][y] for i in range(len(game_map))])):
                game_map[x][y] = e

        return all(map(lambda x: x == 1, sum(game_map, [])))

    def getch(self):
        pass


if __name__ == '__main__':
    main_window = MainWindow()
    curses.wrapper(main_window.main)
