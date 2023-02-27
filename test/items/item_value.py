from item_name import ItemName


class ItemValue:
    def __init__(self, item: ItemName, value: int) -> None:
        self.__item = item
        self.__value: int = value

    @property
    def item(self) -> ItemName:
        return self.__item

    @property
    def sell_value(self):
        return self.__value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
