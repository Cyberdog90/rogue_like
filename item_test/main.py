from item import load

print(load("items.toml")["food"]["normal_candy"].name)
