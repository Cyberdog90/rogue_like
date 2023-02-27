import curses


class DrawRectangle:
    def __init__(self, win, color, uly, ulx, lry, lrx) -> None:
        self.__corner_x, self.__corner_y = tuple(map(lambda x: int(x) - 1, win.getmaxyx()))

        self.__hline(win=win, color=color, y=uly, x=ulx, n=abs(lrx - ulx))
        self.__hline(win=win, color=color, y=lry, x=ulx, n=abs(lrx - ulx))
        self.__vline(win=win, color=color, y=uly, x=ulx, n=abs(lry - uly))
        self.__vline(win=win, color=color, y=uly, x=lrx, n=abs(lry - uly))
        win.addch(uly, ulx, curses.ACS_ULCORNER, color)
        win.addch(uly, lrx, curses.ACS_URCORNER, color)
        win.addch(lry, ulx, curses.ACS_LLCORNER, color)
        win.addch(lry, lrx, curses.ACS_LRCORNER, color)

    def __hline(self, win, color, y: int, x: int, n: int) -> None:
        for h in range(x, x + n + 1):
            win.addch(y, h, curses.ACS_HLINE, color)

    def __vline(self, win, color, y: int, x: int, n: int) -> None:
        for v in range(y, y + n + 1):
            win.addch(v, x, curses.ACS_VLINE, color)
