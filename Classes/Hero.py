from Data.Objects import *

class Unit:
    def __init__(self, fields):
        self.x = None
        self.y = None
        self.fields = fields
        self.level = 0
        self.field = self.fields[self.level]
        self.image = '@'
        self.find_hero()
        self.money = 0
        self.heal_points = 50
        self.experience = 0
        self.hero_level = 1
        self.defend = 0
        self.attack = 5
        self.overhand = None
        self.work_field()

    def work_field(self):
        """

        """
        self.field = [list(line) for line in self.field]

    def next_level(self):
        """
        Переход на следущую локацию
        """
        self.level += 1
        self.field = self.fields[self.level]
        self.work_field()
        self.find_hero()

    def events(self, key):
        self.field[self.y][self.x] = '.'

        if key == 'w':
            if self.y != 0:
                if self.inspection():
                    self.y -= 1
        elif key == 's':
            if self.y != len(self.field)-1:

                    self.y += 1
        elif key == 'a':

                self.x -= 1
        elif key == 'd':

                self.x += 1

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
        self.inspection()
        self.field[self.y][self.x] = self.image

    def inspection(self):
        """
        Проверка на ключевые символы
        """
        for item in objects:
            if item['image'] == self.field[self.y][self.x]:
                return item['passable']
