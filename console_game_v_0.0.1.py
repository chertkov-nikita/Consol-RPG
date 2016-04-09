import tty
import termios
import sys
import os
from template_colors import *
from Data.fields import *
from Data.Status_bar import *
from Classes.Hero import *


def getchar():
    """
    Returns a single character from standard input
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def cls():
    """
    Очищаем консоль
    """
    os.system(['clear', 'cls'][os.name == 'nt'])


def render(field, status_bar_cope):
    for line_f, line_st in zip(field, status_bar_cope):
        print(" ".join(line_f + [' '*10] + [line_st]).replace("@", BLUE.format("@")))
    print("Press 'q' to Exit")
    print("'w' - move up")
    print("'a' - move left")
    print("'s' - move down")
    print("'d' - move right")

# Инициализация
unit = Unit(fields, status_bar)
cls()
render(unit.field, unit.status_bar_cope)

ch = ''
while ch != 'q':
    ch = getchar()
    unit.events(ch)
    unit.inspection()
    unit.update()
    cls()
    render(unit.field, unit.status_bar_cope)
    print('You pressed', ch)
    print('LEVEL -', unit.level+1)