from window_system import WindowSystem
from text_platform import TextPlatform
import curses

__all__ = ["MessageWindow"]


class MessageWindow(WindowSystem):
    def __init__(self):
        window = curses.newwin(__nlines=1, __ncols=56, __begin_x=24, __begin_y=23)
        window_name = {"win": "ﾃｷｽﾄ", "unix": "テキスト"}
        super().__init__(curses_window=window, window_name=TextPlatform(text=window_name))
