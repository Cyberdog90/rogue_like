from window_system import WindowSystem
import curses


class ErrorWindow(WindowSystem):
    def __init__(self):
        super().__init__(self.__make_window(), __class__.__name__)

    @staticmethod
    def __make_window():
        window = curses.newwin(10, 10, 0, 0)
        return window
