class ItemName:
    def __init__(self, item_id, item_name):
        self.__item_id = item_id
        self.__item_name = item_name

    @property
    def id(self):
        return self.__item_id

    @property
    def name(self):
        return self.__item_name
