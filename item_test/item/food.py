from .item import Item

__all__ = ["Food"]


class Food(Item):
    def __init__(self, food_item: dict) -> None:
        super().__init__(item_data=food_item)
        self.__hp: float = food_item["hp"]

    @property
    def hp(self) -> float:
        return self.__hp
