import tty
import termios
import sys
import os
from template_colors import *


class Unit:
    def __init__(self, fields, status_bar):
        self.x = None
        self.y = None
        self.fields = fields
        self.level = 1
        self.field = self.fields[self.level]
        self.image = '@'
        self.find_hero()
        self.status_bar = status_bar
        self.money = 0
        self.heal_points = 50
        self.experience = 0
        self.hero_level = 1
        self.defend = 0
        self.attack = 5
        self.owerhand = 0
        self.fill_bar()

    def next_level(self):
        """
        Переход на следущую локацию
        """
        self.level += 1
        self.field = self.fields[self.level]
        self.find_hero()

    def events(self, key):
        self.field[self.y][self.x] = '.'

        if key == 'w':
            if self.field[self.y-1][self.x] != '#':
                self.y -= 1
                if self.y < 0:
                    self.y = len(self.field) - 1
        elif key == 's':
            if self.field[self.y+1][self.x] != '#':
                self.y += 1
                if self.y >= len(self.field):
                    self.y = 0

        if key == 'a':
            if self.field[self.y][self.x-1] != '#' and self.field[self.y][self.x-1] != '/':
                self.x -= 1
                if self.x < 0:
                    self.x = len(self.field[self.y]) - 1
        elif key == 'd':
            if self.field[self.y][self.x+1] != '#':
                self.x += 1
                if self.x >= len(self.field[self.y]):
                    self.x = 0

    def find_hero(self):
        """
        Ищет персонажа
        """
        j = 0
        i = -1
        for line in self.field:
            try:
                i = line.index(self.image)
                break
            except ValueError:
                j += 1

        if i == -1:
            raise AttributeError("Hero not found")
        else:
            self.x = i
            self.y = j

    def update(self):
        self.field[self.y][self.x] = self.image
        self.fill_bar()

    def inspection(self):
        """
        Проверка на ключевые символы
        """
        if self.x == len(self.field[self.y])-1 or self.y == len(self.field)-1 or self.y == 0:
            self.next_level()
        if self.field[self.y][self.x] == '$':
            self.money += 10
        if self.field[self.y][self.x] == '=':
            self.owerhand += 3

    def fill_bar(self):
        """
        Заполняет status_bar значениями
        """
        self.status_bar[0] = self.status_bar[0].format(str(self.hero_level))
        self.status_bar[1] = self.status_bar[1].format(str(self.heal_points), str(self.attack))
        self.status_bar[2] = self.status_bar[2].format(str(self.experience), str(self.defend))
        self.status_bar[3] = self.status_bar[3].format(str(self.owerhand), str(self.money))



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


def render(field):
    for line in field:
        print(" ".join(line).replace("@", BLUE.format("@")))
    print("Press 'q' to Exit")
    print("'w' - move up")
    print("'a' - move left")
    print("'s' - move down")
    print("'d' - move right")

# Список локаций
fields = {1:[
    ['#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '@', '.', '$', '.', '.', '/'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#']
],
2:[
    ['#','#','#','#'],
    ['#','.','.','#'],
    ['#','.','.','/'],
    ['@','.','.','#'],
    ['#','#','#','#'],
    ],
3:[
    ['#','#','#','#','#'],
    ['@','.','.','.','#'],
    ['#','.','.','.','#'],
    ['#','.','.','.','#'],
    ['#','#','#','#','#'],
]}

status_bar = [
    '(-----LEVEL {0} -----)',
    '(Heal={0}  Attack={1})',
    '(EX={0}    Defend={1})',
    '(OverH={0} Money={1} )',
    '(--------------------)'
]

# Инициализация
unit = Unit(fields, status_bar)
cls()
render(unit.field)

ch = ''
while ch != 'q':
    ch = getchar()
    unit.events(ch)
    unit.inspection()
    unit.update()
    cls()
    render(unit.field)
    print('You pressed', ch)
    print('LEVEL -', unit.level)

