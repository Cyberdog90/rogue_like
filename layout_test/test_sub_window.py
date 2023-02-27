from sub_window import SubWindow
from test_window import TestWindow
from error_window import ErrorWindow


class TestSubWindow(SubWindow):
    def __init__(self):
        test_window = TestWindow()
        error_window = ErrorWindow()
        super().__init__(test_window)
        super().set_new_window(error_window)
