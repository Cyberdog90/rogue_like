import curses
from curses import wrapper
from curses_color import CursesColor
from text_color import TextColor
import locale

locale.setlocale(locale.LC_ALL, "")


def main(stdscr):
    color = TextColor()
    curses.curs_set(False)
    stdscr.refresh()

    color.set_curses_color(color_name="Background", curses_color=curses.COLOR_BLACK)
    color.set_color(color_name="Green", color=CursesColor(red=200, green=1000, blue=200))
    color.set_color(color_name="Yellow", color=CursesColor(red=1000, green=1000, blue=200))
    color.set_color(color_name="Red", color=CursesColor(red=1000, green=200, blue=200))
    color.make_pair(pair_name="Green", text_color="Green", background_color="Background")
    color.make_pair(pair_name="Yellow", text_color="Yellow", background_color="Background")
    color.make_pair(pair_name="Red", text_color="Red", background_color="Background")

    bar = "■■■■■■■■■■"
    empty_bar = "□□□□□□□□□□"
    hp = 10
    stdscr.addstr(0, 0, f"{bar[:hp]}{empty_bar[hp:]} : {hp}/10", color.defined_pair(pair_name="Green"))
    while hp > 0:
        stdscr.getch()
        hp -= 1
        stdscr.clear()
        if hp >= 5:
            stdscr.addstr(0, 0, f"{bar[:hp]}{empty_bar[hp:]} : {hp}/10", color.defined_pair(pair_name="Green"))
        elif 5 > hp >= 3:
            stdscr.addstr(0, 0, f"{bar[:hp]}{empty_bar[hp:]} : {hp}/10", color.defined_pair(pair_name="Yellow"))
        else:
            stdscr.addstr(0, 0, f"{bar[:hp]}{empty_bar[hp:]} : {hp}/10", color.defined_pair(pair_name="Red"))
        stdscr.refresh()

    stdscr.clear()
    stdscr.addstr(0, 0, f"{bar[:hp]}{empty_bar[hp:]} : {hp}/10", color.defined_pair(pair_name="Red"))
    # stdscr.addstr(1, 0, "Game Over!!", color.defined_pair(pair_name="Red"))
    stdscr.addstr(1, 0, "ゲームオーバー", color.defined_pair(pair_name="Red"))
    stdscr.getch()
    curses.curs_set(True)


if __name__ == '__main__':
    wrapper(main)
