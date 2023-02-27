from window_system import WindowSystem
from text_platform import TextPlatform
import curses

__all__ = ["MapWindow"]


class MapWindow(WindowSystem):
    def __init__(self):
        window = curses.newwin(__nlines=19, __ncols=56, __begin_x=24, __begin_y=0)
        window_name = {"win": "ﾏｯﾌﾟ", "unix": "マップ"}
        super().__init__(curses_window=window, window_name=TextPlatform(text=window_name))
