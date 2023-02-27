from sys import platform

__all__ = ["Item"]


class Item:
    def __init__(self, item_data: dict) -> None:
        self.__name: TextPlatform = TextPlatform(item_data["name"])
        self.__flavor: TextPlatform = TextPlatform(item_data["flavor"])

    @property
    def name(self) -> str:
        return self.__name.text

    @property
    def flavor(self) -> str:
        return self.__flavor.text


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
