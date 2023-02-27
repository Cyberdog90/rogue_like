import curses


# from main_window import MainWindow

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(False)
    stdscr.refresh()

    stdscr.addstr(0, 0, "hello")
    while (key := stdscr.getch()) != 27:
        if key == ord("f"):
            stdscr.addstr(1, 0, "f")
            curses.flash()

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    curses.curs_set(True)


if __name__ == '__main__':
    curses.wrapper(main)
