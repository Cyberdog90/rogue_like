from window_system import WindowSystem
from text_platform import TextPlatform
import curses

__all__ = ["LogWindow"]


class LogWindow(WindowSystem):
    def __init__(self):
        window = curses.newwin(__nlines=12, __ncols=24, __begin_x=0, __begin_y=12)
        window_name = {"win": "ログ", "unix": "ログ"}
        super().__init__(curses_window=window, window_name=TextPlatform(text=window_name))
