from rlengine.window.window_system import WindowSystem
from rlengine.text_platform import TextPlatform
import curses

__all__ = ["StatusWindow"]


class StatusWindow(WindowSystem):
    def __init__(self):
        window = curses.newwin(12, 24, 0, 0)
        window_name = {"win": "ｽﾃｰﾀｽ", "unix": "ステータス"}
        super().__init__(curses_window=window, window_name=TextPlatform(text=window_name), is_active=True)

    def update(self, u_input: str = ""):
        pass
