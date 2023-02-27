from draw_rectangle import rectangle


class SmartRectangle:
    def __init__(self, win, name: str, color, uly: int = None, ulx: int = None, lry: int = None, lrx: int = None):
        self.__window_instance = win
        self.__default_color = color

        if uly is None:
            uly = 0
        if ulx is None:
            ulx = 0

        y, x = self.__get_max()
        if lry is None:
            lry = y
        if lrx is None:
            lrx = x

        rectangle(self.__window_instance, self.__default_color, uly, ulx, lry, lrx)
        self.__rectangles = {name: (0, 0, lry, lrx)}
        self.__insertable_space = {name: (uly + 1, ulx + 1, lry - 1, lrx - 1)}

    def add_rectangle(self, parent, name, color=None, uly=None, ulx=None, lry=None, lrx=None):
        assert parent in self.__rectangles, f"rectangle {parent} is not defined"

        i_uly, i_ulx, i_lry, i_lrx = self.__insertable_space[parent]
        if uly is None:
            uly = i_uly
        if ulx is None:
            ulx = i_ulx
        if lry is None:
            lry = i_lry
        if lrx is None:
            lrx = i_lrx
        if color is None:
            color = self.__default_color

        rectangle(self.__window_instance, color, uly, ulx, lry, lrx)
        self.__rectangles[name] = (uly, ulx, lry, lrx)
        self.__insertable_space[parent] = (min(lry + 1, i_lry), min(lrx + 1), i_lrx,)
        self.__insertable_space[name] = (uly + 1, ulx + 1, lry - 1, lrx - 1)

    def add_smart_rectangle(self, parent, name, color=None, h_size=None, v_size=None):
        assert h_size is not None and v_size is not None, f"h_size and v_size is None"

    def add_smart(self, upper, name, color=None, space=0, size=0):
        assert upper in self.__rectangles, f"rectangle {upper} is not defined"
        uly, ulx, lry, lrx = self.__rectangles[upper]
        uly += 1
        lrx = uly + space
        rectangle(self.__window_instance, color, uly, ulx, lry, lrx)
        self.__rectangles[name] = (uly, ulx, lry + 1, lrx)

    def __get_max(self) -> tuple:
        return tuple(map(lambda x: int(x) - 1, self.__window_instance.getmaxyx()))

    def get_rectangle(self, name) -> dict:
        assert name in self.__rectangles, f"rectangle {name} is not defined"
        return self.__rectangles[name]
