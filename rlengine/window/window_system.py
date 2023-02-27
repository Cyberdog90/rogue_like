from rlengine.text_platform import TextPlatform
from abc import ABCMeta, abstractmethod

__all__ = ["WindowSystem"]


class WindowSystem(metaclass=ABCMeta):
    def __init__(self, curses_window, window_name: TextPlatform, is_active: bool):
        self.__curses_window = curses_window
        self.__window_name: TextPlatform = window_name
        self.__is_active: bool = is_active

    def get_size_yx(self):
        return self.__curses_window.getmaxyx()

    @property
    def window(self):
        return self.__curses_window

    @property
    def window_name(self) -> str:
        return self.__window_name.text

    def set_active(self) -> None:
        self.__is_active = True

    def set_inactive(self) -> None:
        self.__is_active = False

    @property
    def is_active(self) -> bool:
        return self.__is_active

    @abstractmethod
    def update(self, u_input: str = ""):
        pass
