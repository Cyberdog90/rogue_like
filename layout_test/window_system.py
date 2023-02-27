from text_platform import TextPlatform


class WindowSystem:
    def __init__(self, curses_window, window_name: TextPlatform):
        self.__curses_window = curses_window
        self.__window_name: TextPlatform = window_name

    def get_size_yx(self):
        return self.__curses_window.getmaxyx()

    @property
    def window(self):
        return self.__curses_window

    @property
    def window_name(self) -> str:
        return self.__window_name.text
