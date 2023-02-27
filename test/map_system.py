class MapSystem:
    def __init__(self, map_path: str) -> None:
        self.__map_data = [line for line in self.map_loader(map_path)]
        

    @staticmethod
    def map_loader(path):
        for line in open(path, "r", encoding="utf-8"):
            yield line.replace("\n", "")
