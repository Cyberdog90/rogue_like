from typing import Final, Tuple, Dict
from window_system import WindowSystem
from invalid_window_size_exception import InvalidWindowSizeException
from duplicate_window_name_exception import DuplicateWindowNameException


class SubWindow:
    def __init__(self, window: WindowSystem) -> None:
        self.__windows: Dict = {window.window_name: window.window}
        self.__BEGIN_YX: Final[Tuple[int, int]] = window.window.getbegyx()
        self.__SUB_WINDOW_SIZE: Final[Tuple[int, int]] = window.window.getmaxyx()

    def set_new_window(self, window: WindowSystem) -> None:
        if window.window.getbegyx() != self.begin_yx:
            raise InvalidWindowSizeException(f"Expected begin => {self.begin_yx}, "
                                             f"Window begin => {window.window.getbegyx()}")

        if window.window.getmaxyx() != self.sub_window_size:
            raise InvalidWindowSizeException(f"Expected size => {self.sub_window_size}, "
                                             f"Window size => {window.window.getmaxyx()}")

        if window.window_name in self.__windows:
            raise DuplicateWindowNameException(f"window name '{window.window_name}' already existed.")

        self.__windows[window.window_name] = window.window

    @property
    def ul_lr(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        ul: Tuple[int, int] = self.begin_yx
        lr: Tuple[int, int] = (ul[0] + self.sub_window_size[0], ul[1] + self.sub_window_size[1])
        return ul, lr

    @property
    def begin_yx(self) -> Tuple[int, int]:
        return self.__BEGIN_YX

    @property
    def sub_window_size(self) -> Tuple[int, int]:
        return self.__SUB_WINDOW_SIZE

    @property
    def windows(self) -> Dict:
        return self.__windows
