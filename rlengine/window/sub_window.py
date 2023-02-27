from typing import Final, Dict

from rlengine.window.window_system import WindowSystem
from rlengine.vec2 import Vec2YX
from rlengine.ul_lr import ULLR

__all__ = ["SubWindow"]


class SubWindow:
    def __init__(self, window: WindowSystem) -> None:
        self.__windows: Dict = {window.window_name: window.window}
        self.__BEGIN_YX: Final[Vec2YX] = Vec2YX(y_x=window.window.getbegyx())
        self.__SUB_WINDOW_SIZE: Final[Vec2YX] = Vec2YX(y_x=window.window.getmaxyx())

    def set_new_window(self, window: WindowSystem) -> None:
        assert window.window.getbegyx() == self.begin_yx, "ウィンドウの座標が違います\t" \
                                                          f"期待された座標 => {self.begin_yx}, " \
                                                          f"実際の座標 => {window.window.getbegyx()}"

        assert window.window.getmaxyx() == self.sub_window_size, "ウィンドウのサイズが違います\t" \
                                                                 f"期待されたサイズ => {self.sub_window_size}, " \
                                                                 f"実際のサイズ => {window.window.getmaxyx()}"

        assert window.window_name not in self.__windows, f"ウィンドウ名: '{window.window_name}'　は既に存在します"

        self.__windows[window.window_name] = window.window

    @property
    def ul_lr(self) -> ULLR:
        ul: Vec2YX = self.begin_yx
        lr: Vec2YX = ul + self.sub_window_size
        return ULLR(ul=ul, lr=lr)

    @property
    def begin_yx(self) -> Vec2YX:
        return self.__BEGIN_YX

    @property
    def sub_window_size(self) -> Vec2YX:
        return self.__SUB_WINDOW_SIZE

    @property
    def windows(self) -> Dict:
        return self.__windows
