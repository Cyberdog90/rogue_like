from item_name import ItemName
from item_value import ItemValue
from item import Item
from dataclasses import dataclass


@dataclass(frozen=True)
class Items:
    STONE: Item = Item(item=ItemValue(item=ItemName(item_id="stone", item_name="石"), value=0),
                       recipe=ItemValue(item=Items.FORGE, value=0))
    PIPE: ItemName = ItemName(item_id="pipe", item_name="パイプ")
    FORGE: ItemName = ItemName(item_id="forge", item_name="炉")


if __name__ == '__main__':
    items = Items()
    print(items.STONE.name)
