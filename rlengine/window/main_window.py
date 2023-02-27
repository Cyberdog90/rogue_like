from typing import Dict, Tuple, List
from itertools import accumulate
import curses
from curses import wrapper

from rlengine.window.sub_window import SubWindow
from rlengine.ul_lr import ULLR
from rlengine.vec2 import Vec2YX

__all__ = ["MainWindow"]


class MainWindow:
    def __init__(self, window_size: Tuple[int, int], allow_overlap: bool = False,
                 allow_blank_space: bool = False) -> None:
        self.__window_size: Vec2YX = Vec2YX(y_x=window_size)
        self.allow_overlap: bool = allow_overlap
        self.allow_blank_space: bool = allow_blank_space
        self.window_positions: List[ULLR] = []

    @property
    def window_size(self) -> Vec2YX:
        return self.__window_size

    def add_sub_window(self, sub_window: SubWindow) -> None:
        self.window_positions.append(sub_window.ul_lr)

    def check_overlap(self) -> None:
        check_array: List[int, int] = self.__make_check_array()
        for y in range(len(check_array)):
            check_array[y] = list(accumulate(check_array[y]))

        for y in range(len(check_array[0])):
            for x, e in enumerate(accumulate([check_array[i][y] for i in range(len(check_array))])):
                check_array[x][y] = e

        if not self.allow_overlap:
            assert not any(map(lambda x: x > 1, sum(check_array, [])))

        if not self.allow_blank_space:
            assert not any(map(lambda x: x < 1, sum(check_array, [])))

    def __make_check_array(self) -> List[List[int]]:
        check_array: List[int, int] = [[0] * self.__window_size.x for _ in range(self.__window_size.y)]

        for window_position in self.window_positions:
            check_array[window_position.ul.y][window_position.ul.x] += 1

            if window_position.ur.x < self.__window_size.x:
                check_array[window_position.ur.y][window_position.ur.x] -= 1

            if window_position.ll.y < self.__window_size.y:
                check_array[window_position.ll.y][window_position.ll.x] -= 1

            if window_position.lr.x < self.__window_size.x and \
                    window_position.lr.y < self.__window_size.y:
                check_array[window_position.lr.y][window_position.lr.x] += 1
        return check_array
