from sys import platform

__all__ = ["TextPlatform"]


class TextPlatform:
    def __init__(self, text: dict[str]) -> None:
        self.__win: str = text["win"]
        self.__unix: str = text["unix"]

    @property
    def text(self) -> str:
        if platform == "win32":
            return self.__win
        else:
            return self.__unix
