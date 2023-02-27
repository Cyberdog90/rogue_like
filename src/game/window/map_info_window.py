from rlengine.window.window_system import WindowSystem
from rlengine.text_platform import TextPlatform
import curses

__all__ = ["MapInfoWindow"]


class MapInfoWindow(WindowSystem):
    def __init__(self):
        window = curses.newwin(1, 56, 19, 24)
        window_name = {"win": "ﾏｯﾌﾟｼﾞｮｳﾎｳ", "unix": "マップ情報"}
        super().__init__(curses_window=window, window_name=TextPlatform(text=window_name), is_active=True)

    def update(self, u_input: str = ""):
        pass
