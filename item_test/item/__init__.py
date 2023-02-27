import tomllib
from .food import Food

__all__ = ["food", "item", "load"]


def _load(file_name: str) -> dict:
    with open(file=file_name, mode="rb") as f:
        return tomllib.load(f)


def load(file_name):
    return {item_type: {key: item_table[item_type](item) for key, item in _load(file_name).items()} for item_type, file_name in _load(file_name).items()}


item_table = {
    "food": Food
}
