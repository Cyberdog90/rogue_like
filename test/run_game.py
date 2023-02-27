import os

x = os.get_terminal_size().lines
y = os.get_terminal_size().columns
os.system(f"mode {30},{50}")
