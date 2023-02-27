from item_name import ItemName
from item_value import ItemValue


class Item:
    def __init__(self, item: ItemValue, recipe: ItemValue = None, material: ItemValue = None):
        self.item: ItemValue = item
        self.recipe = recipe
        self.material = material
