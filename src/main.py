from rlengine.window.sub_window import SubWindow
from rlengine.window.main_window import MainWindow

from game.window.status_window import StatusWindow
from game.window.log_window import LogWindow
from game.window.map_window import MapWindow
from game.window.map_info_window import MapInfoWindow
from game.window.textbox_window import TextboxWindow
from game.window.message_window import MessageWindow


def main():
    window = MainWindow(window_size=(24, 80))
    window.add_sub_window(SubWindow(StatusWindow()))
    window.add_sub_window(SubWindow(LogWindow()))
    window.add_sub_window(SubWindow(MapWindow()))
    window.add_sub_window(SubWindow(MapInfoWindow()))
    window.add_sub_window(SubWindow(TextboxWindow()))
    window.add_sub_window(SubWindow(MessageWindow()))
    window.run()


if __name__ == '__main__':
    main()
