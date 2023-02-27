class MapRender:
    def __init__(self, win, map_data: list[str], origin: tuple = None, size: tuple = None):
        if origin is None:
            origin = (0, 0)
        if size is None:
            size = tuple(map(lambda x: x - 1, win.getmaxyx()))

