from rlengine.window.window_system import WindowSystem
from rlengine.text_platform import TextPlatform
import curses

__all__ = ["MapWindow"]


class MapWindow(WindowSystem):
    def __init__(self):
        window = curses.newwin(19, 56, 0, 24)
        window_name = {"win": "ﾏｯﾌﾟ", "unix": "マップ"}
        super().__init__(curses_window=window, window_name=TextPlatform(text=window_name), is_active=True)

    def update(self, u_input: str = ""):
        pass
