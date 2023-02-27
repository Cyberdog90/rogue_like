from rlengine.window.window_system import WindowSystem
from rlengine.text_platform import TextPlatform
import curses

__all__ = ["TextboxWindow"]


class TextboxWindow(WindowSystem):
    def __init__(self):
        window = curses.newwin(3, 56, 20, 24)
        window_name = {"win": "ﾃｷｽﾄ", "unix": "テキスト"}
        super().__init__(curses_window=window, window_name=TextPlatform(text=window_name), is_active=True)

    def update(self, u_input: str = ""):
        pass
