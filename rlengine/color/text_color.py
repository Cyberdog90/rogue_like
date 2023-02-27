import curses

from curses_color import CursesColor

__all__ = ["TextColor"]


class TextColor:
    def __init__(self):
        self.__defined_color = dict()
        self.__defined_color_pair = dict()
        self.__color_counter = 16
        self.__color_pair_counter = 1

    def set_color(self, color_name: str, color: CursesColor) -> None:
        assert color_name not in self.__defined_color, f"color {color_name} is already exist"
        curses.init_color(self.__color_counter, color.red, color.green, color.blue)
        self.__set_curses_color(color_name=color_name, curses_color=self.__color_counter)

    def __set_curses_color(self, color_name: str, curses_color: int) -> None:
        assert color_name not in self.__defined_color, f"color {color_name} is already exist"
        self.__defined_color[color_name] = curses_color
        self.__color_counter += 1

    def make_pair(self, pair_name: str, text_color: str, background_color: str) -> None:
        assert text_color in self.__defined_color, f"color {text_color} is not defined"
        assert background_color in self.__defined_color, f"color {background_color} is not defined"
        curses.init_pair(self.__color_pair_counter,
                         self.__defined_color[text_color],
                         self.__defined_color[background_color])
        self.__defined_color_pair[pair_name] = self.__color_pair_counter
        self.__color_pair_counter += 1

    def defined_pair(self, pair_name: str):
        assert pair_name in self.__defined_color_pair, f"color_pair {pair_name} is not defined"
        return curses.color_pair(self.__defined_color_pair[pair_name])
