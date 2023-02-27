from rlengine.window.window_system import WindowSystem
from rlengine.text_platform import TextPlatform
import curses

__all__ = ["LogWindow"]


class LogWindow(WindowSystem):
    def __init__(self):
        window = curses.newwin(12, 24, 12, 0)
        window_name = {"win": "ログ", "unix": "ログ"}
        super().__init__(curses_window=window, window_name=TextPlatform(text=window_name), is_active=True)
        self.set_inactive()

    def update(self, u_input: str = ""):
        pass


if __name__ == '__main__':
    LogWindow()
