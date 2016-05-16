import tty
import termios
import sys
import os
from Data.template_colors import *
from Data.fields import *
from Data.Status_bar import *
from Classes.Hero import *
from Classes.Monster import *


class Game:
    def __init__(self):
        self.hero = Unit(fields)
        self.snake = Snake()
        self.status_bar = Status_bar(status_bar, self.hero)

    def cls(self):
        """
        Очищаем консоль
        """
        os.system(['clear', 'cls'][os.name == 'nt'])


    def getchar(self):
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

    def render_status_bar(self):
        for line in self.status_bar.render():
            print(line)

    def render_field(self):
        for line_f in self.hero.field:
            print(" ".join(line_f).replace("@", BLUE.format("@")))
        print("Press 'q' to Exit")
        print("'w' - move up")
        print("'a' - move left")
        print("'s' - move down")
        print("'d' - move right")

    def run(self):
        self.cls()
        self.render_status_bar()
        print('\n')
        self.render_field()
        ch = ''
        while ch != 'q':
            ch = self.getchar()
            self.hero.events(ch)
            self.hero.update()
            self.cls()
            self.render_status_bar()
            print('\n')
            self.render_field()
            print('You pressed', ch)
            print('LEVEL -', self.hero.level+1)
            print(self.hero.x, self.hero.y)
            print(self.hero.future_image)


if __name__ == "__main__":
    game = Game()
    game.run()